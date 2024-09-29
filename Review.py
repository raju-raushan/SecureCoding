import os
import json
import subprocess
from flask import Flask, request

app = Flask(__name__)

# Route to execute system command
@app.route('/exec', methods=['POST'])
def exec_cmd():
    cmd = request.form.get('cmd')
    output = subprocess.check_output(cmd, shell=True)
    return output

# Route to get user data
@app.route('/user_data', methods=['GET'])
def get_user_data():
    user_id = request.args.get('user_id')
    with open(f"{user_id}.json", "r") as f:
        data = json.load(f)
    return data

# Route to log an event
@app.route('/log_event', methods=['POST'])
def log_event():
    event = request.form.get('event')
    with open("event_log.txt", "a") as f:
        f.write(f"{event}\n")
    return "Event logged."

if __name__ == "__main__":
    app.run(debug=True)
