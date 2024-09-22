from lab1 import app
from flask import Response
import json
from datetime import datetime

@app.route('/healthcheck')
def healthcheck():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response = {
        "status": "OK",
        "timestamp": current_time
    }
    return Response(json.dumps(response), mimetype='application/json'), 200
