from flask import Flask, render_template, request, jsonify
import mysql.connector
import google.generativeai as genai
import json
import os

app = Flask(__name__)

def get_db_context():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="employee_db"
        )
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
        
        cursor.execute("SELECT * FROM departments")
        departments = cursor.fetchall()
        
        cursor.execute("SELECT * FROM attendance")
        attendance = cursor.fetchall()
        
        cursor.execute("SELECT * FROM salaries")
        salaries = cursor.fetchall()
        
        conn.close()
        
        return {
            "employees": employees,
            "departments": departments,
            "attendance": attendance,
            "salaries": salaries
        }
    except Exception as e:
        return {"error": str(e)}

@app.route('/')
def index():
    return render_template('index.html')

def mock_ai_response(user_message, db_context):
    msg = user_message.lower()
    if 'salary' in msg:
        salaries = "\n".join([f"- Employee {s['employee_id']}: ${s['net_salary']}" for s in db_context['salaries']])
        return f"Here are the salaries based on your database:\n{salaries}\n\n*(Offline Mock AI Mode)*"
    elif 'attendance' in msg:
        attendance = "\n".join([f"- Employee {a['employee_id']}: {a['status']} on {a['attendance_date']}" for a in db_context['attendance']])
        return f"Here is the recent attendance data:\n{attendance}\n\n*(Offline Mock AI Mode)*"
    elif 'department' in msg:
        deps = "\n".join([f"- {d['department_name']} (Head: {d['department_head']})" for d in db_context['departments']])
        return f"Here are the departments:\n{deps}\n\n*(Offline Mock AI Mode)*"
    else:
        emps = "\n".join([f"- {e['name']} (ID: {e['id']}, Dept: {e['department']})" for e in db_context['employees']])
        return f"Here are the employees in the system:\n{emps}\n\n*(Note: You are currently using the Offline Mock AI because a valid Gemini API key was not detected. Ask about 'salary', 'attendance', or 'department' to see specific data!)*"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    api_key = data.get('api_key')
    
    if not api_key:
        return jsonify({"error": "Please provide a Gemini API Key."}), 400
        
    db_context = get_db_context()
    
    if "error" in db_context:
        return jsonify({"error": f"Database error: {db_context['error']}"}), 500
        
    # If it's the strange AQ. key, fallback immediately so the app doesn't crash
    if api_key.startswith("AQ."):
        return jsonify({"response": mock_ai_response(user_message, db_context)})
        
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        system_prompt = f"""
        You are a highly capable AI assistant for an Employee Management System.
        Your task is to answer the user's questions based on the provided database context.
        Provide clear, concise, and helpful answers. Format your responses with markdown if appropriate (e.g., bullet points or tables for multiple employees).
        If the user asks for information not present in the context, politely inform them.
        
        Database Context (JSON):
        {json.dumps(db_context, default=str)}
        """
        
        prompt = system_prompt + f"\n\nUser Query: {user_message}"
        
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
        
    except Exception as e:
        # If API fails for any reason, fallback to Mock AI instead of crashing
        return jsonify({"response": mock_ai_response(user_message, db_context)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
