import requests
from flask import Flask, render_template, request


app = Flask(__name__)

mock_data = ["mama", "mila", "ramu"]


@app.get("/")
def choice():
    actions = ["/random_int", "/random_item_from_list", "/current_date"]
    return render_template("actions.html", actions=actions)

@app.post("/actions")
def action_check():
    
    form_result = request.form["action"]
    print(form_result)
    response = requests.get("http://127.0.0.1:8080" + f"{form_result}").json()
    return render_template("output.html", result=response)
