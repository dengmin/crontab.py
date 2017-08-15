
from flask import request, render_template
from manage import app

@app.route('/')
def index():
    jobs = app.scheduler.get_jobs()
    print(jobs)
    return  render_template('index.html')