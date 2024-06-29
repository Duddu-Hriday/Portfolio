from flask import Flask, render_template
from database import engine
from sqlalchemy import text

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


with engine.connect() as conn:
  result = conn.execution_options(stream_results=False).execute(text("select * from projects"))
  rows = result.fetchall()
  columns = result.keys()
  projects = []
  for row in rows:
    project = {col: getattr(row, col) for col in columns}
    projects.append(project)

  # print(rows_dicts)

@app.route('/projects')
def projects():
    return render_template('projects.html',projects = projects)


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
