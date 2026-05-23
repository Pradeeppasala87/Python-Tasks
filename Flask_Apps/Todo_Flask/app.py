# ============================================================
# 📝 SIMPLE FLASK TODO APP
# ============================================================

# Import Flask modules

try:
    from flask import Flask, render_template, request, redirect, url_for

except ImportError as e:

    raise ImportError(

        "Flask is not installed. Install it with 'pip install flask' and try again."

    ) from e


# Create Flask application

app = Flask(__name__)


# Store tasks temporarily in list

tasks = []


# ============================================================
# 🏠 HOME PAGE
# ============================================================

@app.route('/')
def home():

    # Get search text from URL

    search = request.args.get('search', '')

    # If search box has value

    if search:

        # Filter matching tasks

        filtered_tasks = [

            task for task in tasks

            if search.lower() in task['title'].lower()

        ]

    else:

        filtered_tasks = tasks

    # Open home page

    return render_template(

        'index.html',

        tasks=filtered_tasks

    )


# ============================================================
# ➕ ADD TASK PAGE
# ============================================================

@app.route('/add', methods=['GET', 'POST'])
def add_task():

    # If form submitted

    if request.method == 'POST':

        # Get task from form

        task = request.form.get('task')

        # Check task exists

        if task and task.strip():

            # Add into list

            tasks.append({

                "title": task.strip(),

                "completed": False

            })

        # Redirect to home page

        return redirect(url_for('home'))

    # Open add task page

    return render_template('add_tasks.html')


# ============================================================
# ✏️ EDIT TASK
# ============================================================

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_task(index):

    if request.method == 'POST':

        updated_task = request.form.get('task')

        if updated_task and updated_task.strip():

            tasks[index]['title'] = updated_task.strip()

        return redirect(url_for('home'))

    return render_template(

        'edit_task.html',

        task=tasks[index],

        index=index

    )


# ============================================================
# 🗑️ DELETE TASK
# ============================================================

@app.route('/delete/<int:index>')
def delete_task(index):

    if 0 <= index < len(tasks):

        tasks.pop(index)

    return redirect(url_for('home'))


# ============================================================
# ✅ COMPLETE TASK
# ============================================================

@app.route('/complete/<int:index>')
def complete_task(index):

    tasks[index]['completed'] = True

    return redirect(url_for('home'))


# ============================================================
# 🚀 RUN APPLICATION
# ============================================================

if __name__ == '__main__':

    app.run(

        host='127.0.0.1',

        port=5001,

        debug=True

    )