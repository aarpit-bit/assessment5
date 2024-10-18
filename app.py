# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# # In-memory storage for tasks
# tasks = []

# @app.route('/')
# def index():
#     return render_template('index.html', tasks=tasks)

# @app.route('/add', methods=['POST'])
# def add_task():
#     task_content = request.form.get('task')
#     if task_content:
#         tasks.append(task_content)
#     return redirect(url_for('index'))

# @app.route('/delete/<int:task_id>')
# def delete_task(task_id):
#     if 0 <= task_id < len(tasks):
#         tasks.pop(task_id)
#     return redirect(url_for('index'))

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    if task_content:
        tasks.append(task_content)
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        updated_content = request.form.get('task')
        if updated_content:
            tasks[task_id] = updated_content
        return redirect(url_for('index'))
    
    task = tasks[task_id]
    return render_template('edit.html', task=task, task_id=task_id)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5050 , debug=True)
