import json
from datetime import datetime
from flask import Flask, request
app = Flask(__name__)

@app.route('/api')
def render():
    """ a module that extract query parameters from the URL """
    slack_name = request.args.get('slack_name')
    track =  request.args.get('track')
    if slack_name and track:
        data = {

            "slack_name": slack_name,
            "current_day": datetime.now().strftime('%A'),
            "utc_time": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "track": track,
            "github_file_url": "https://github.com/Rashnotech/HNG_backend/blob/main/app.py",
            "github_repo_url": "https://github.com/Rashnotech/HNG_backend",
            "status_code": 200
        }
        response = json.dumps(data)
        return response, 200, {'Content-Type': 'application/json'}
    else:
        data = {'error': 'Missing parameter.', 'status_code': 400}
        response = json.dumps(data)
        return response, 400, {'Content-Type': 'application/json'}