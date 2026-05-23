# Import Flask modules
from flask import Flask, render_template, request

# Create Flask application
app = Flask(__name__)

# Store tasks in a list
tasks = []


# ---------------- HOME PAGE ----------------

# Route for home page
@app.route('/')
def home():

    # Get search value from URL
    search = request.args.get('search')

    # If user searches something
    if search:

        # Filter matching tasks
        filtered_tasks = [
            task for task in tasks
            if search.lower() in task.lower()
        ]

    # If no search
    else:
        filtered_tasks = tasks

    # Send data to index.html
    return render_template(
        'index.html',
        tasks=filtered_tasks
    )


# ---------------- ADD TASK PAGE ----------------

# Route for add task page
@app.route('/add', methods=['GET', 'POST'])
def add_task():

    # Check if form submitted
    if request.method == 'POST':

        # Get task from input box
        task = request.form.get('task')

        # Check task is not empty
        if task:

            # Add task into list
            tasks.append(task)

        # Show success message
        return render_template(
            'add_tasks.html',
            message="Task Successfully Added!"
        )

    # Open add task page
    return render_template('add_tasks.html')


# ---------------- RUN APPLICATION ----------------

# Start Flask server
if __name__ == '__main__':
    app.run(debug=True)
