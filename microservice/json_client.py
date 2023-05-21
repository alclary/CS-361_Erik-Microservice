# This is a test file for sending data to 'json_server.py'

import json
import asyncio
from websockets.sync.client import connect

# cite: https://zguide.zeromq.org/docs/chapter1/
# Set up the ZeroMQ context and socket
HOST = 'localhost'
PORT = 5557

def send():
    input_data = {
    "sections": [
        {
        "checkItems": [
            {
            "checkboxText": "checkbox1.1_text",
            "checkboxDesc": "checkbox1.1_desc_optional"
            },
            {
            "checkboxText": "checkbox1.2_text"
            }
        ],
        "sectionTitle": "section1_title",
        "sectionDesc": "section1_desc_optional"
        }
    ]
    }

    with connect(f"ws://{HOST}:{PORT}") as websocket:
        websocket.send(json.dumps(input_data))
        message = websocket.recv()
        print(f"Received reply [ {message} ]")

send()