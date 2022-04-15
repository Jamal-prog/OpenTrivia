
#!/usr/bin/env python3
"""Receiving JSON from GET request | Jamal Hawkins"""
import requests
import os
import html
from flask import Flask
from flask import request
from flask import redirect 
from flask import jsonify
from flask import Flask
from flask import render_template
from flask import url_for

# creating the Flask
app= Flask(__name__)

# grabs request from trival api
resp = requests.get("https://opentdb.com/api.php?amount=1&category=21&difficulty=easy").json()

# makes a root route to return login.html which is the home page

@app.route("/login")
@app.route("/")
def index():
    return render_template("login.html")

    # makes a route to set user by entered name if not entered user will be guest

@app.route("/setuser", methods =["POST"])
def setuser():
    if request.method == "POST":
        if request.form.get("nm") != "":
            user = request.form.get("nm")
        else:
            user = "Guest"
    elif request.method == "GET":
        if request.args.get("nm"):
            user = request.args.get("nm") 
        else: 
            user = "defaultuser" 
        if request.args.get("api"):
            return redirect(url_for("apijson"))
    return redirect(url_for("answer", username = user)) 

    
# makes route to produce question
@app.route("/question/<username>", methods =[ "GET"])
def answer(username):
   # grabs question, answers
    question = html.unescape(resp['results'][0]['question'])
    correct =  resp['results'][0]['correct_answer']
    other =  resp['results'][0]['incorrect_answers']
    # creates a empty list
    ans = []
    # append correct answer to list
    ans.append(correct)
    # put other items from list in the empty list
    for x in other:
        ans.append(x)


    if request.method == "GET":
        if request.args.get("nm"):
            corr = request.args.get("nm") 
            if corr == correct:
               return render_template("answer.html", answer = corr)
            else:
               return render_template("answer.html", answer = "wrong")
        if request.args.get("api"):
            return redirect(url_for("apijson"))

    return render_template("project.html", name = username, question = question, answers = ans)
 


@app.route("/apijson")
def apijson():
    resp = requests.get("https://opentdb.com/api.php?amount=1&category=21&difficulty=easy").json()
    # return legal JSON
    question = resp['results'][0]['question']
    correct =  resp['results'][0]['correct_answer']
    other =  resp['results'][0]['incorrect_answers']
    print(question)
    return jsonify(resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
    os.system("clear")