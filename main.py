from flask import Flask, render_template, request, redirect, send_file
from so import get_jobs as get_so_jobs
from wework import get_jobs as get_ww_jobs
from remoteok import get_jobs as get_ok_jobs
from export import save_to_file

app = Flask("Find Job")

db = {}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/jobs.html")
def jobs():
  word = request.args.get("word")
  if word:
    word = word.lower()
    fromDb = db.get(word)
    if fromDb:
      jobs = fromDb
    else:
      jobs = get_so_jobs(word) + get_ww_jobs(word) + get_ok_jobs(word)
      db[word] = jobs
  else:
    redirect("/")
  return render_template("jobs.html", word=word, jobs=jobs, numResult = len(jobs))

@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file("result.csv", attachment_filename=f"{word}_result.csv", as_attachment=True)
  except:
    return redirect("/")