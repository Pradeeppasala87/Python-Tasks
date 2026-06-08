import streamlit as st
import mysql.connector
from mysql.connector import Error
import pandas as pd

# Database Configuration
DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = "1234"
DB_NAME = "employee_management_system"

# App Title
st.set_page_config(page_title="Employee Database Bot", page_icon="🤖")
st.title("🤖 Employee Database Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello! I am connected to the Employee Management Database. You can ask me to 'list employees', 'list departments', 'show attendance', or 'show salaries'."
    })

# Database connection helper
@st.cache_resource
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None

def fetch_data(query):
    conn = get_db_connection()
    if conn and conn.is_connected():
        try:
            return pd.read_sql(query, conn)
        except Exception as e:
            return str(e)
    return "Could not connect to database."

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask me about the database... (e.g. 'list employees')"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Bot response logic
    response_content = ""
    prompt_lower = prompt.lower()
    
    with st.chat_message("assistant"):
        if "employee" in prompt_lower:
            st.markdown("Here are the employees in the database:")
            df = fetch_data("SELECT e.id, e.first_name, e.last_name, d.department_name FROM employees e LEFT JOIN departments d ON e.department_id = d.id")
            if isinstance(df, pd.DataFrame) and not df.empty:
                st.dataframe(df, use_container_width=True)
                response_content = "Displayed employees."
            elif isinstance(df, pd.DataFrame) and df.empty:
                st.markdown("*No employees found in the database.*")
                response_content = "No employees found."
            else:
                st.markdown(f"Error: {df}")
                response_content = str(df)
                
        elif "department" in prompt_lower:
            st.markdown("Here are the departments:")
            df = fetch_data("SELECT * FROM departments")
            if isinstance(df, pd.DataFrame) and not df.empty:
                st.dataframe(df, use_container_width=True)
                response_content = "Displayed departments."
            else:
                st.markdown("*No departments found or error occurred.*")
                response_content = "No departments found."
                
        elif "salar" in prompt_lower:
            st.markdown("Here are the salaries:")
            df = fetch_data("SELECT s.id, e.first_name, e.last_name, s.salary_amount, s.effective_date FROM salaries s JOIN employees e ON s.employee_id = e.id")
            if isinstance(df, pd.DataFrame) and not df.empty:
                st.dataframe(df, use_container_width=True)
                response_content = "Displayed salaries."
            else:
                st.markdown("*No salary data found.*")
                response_content = "No salaries found."
                
        elif "attend" in prompt_lower:
            st.markdown("Here is the attendance record:")
            df = fetch_data("SELECT a.id, e.first_name, e.last_name, a.date, a.status FROM attendance a JOIN employees e ON a.employee_id = e.id")
            if isinstance(df, pd.DataFrame) and not df.empty:
                st.dataframe(df, use_container_width=True)
                response_content = "Displayed attendance."
            else:
                st.markdown("*No attendance data found.*")
                response_content = "No attendance found."
                
        else:
            response_content = f"I am a simple database bot. I don't understand '{prompt}'. Try asking for 'employees', 'departments', 'salaries', or 'attendance'."
            st.markdown(response_content)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response_content})
