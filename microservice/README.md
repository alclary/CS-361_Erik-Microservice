# JSON Object Microservice

## About
This microservice is impelmented to transforms JSON objects from the _Sample Input_ to the _Sample Output_ formatting, listed below.
It utilizes synchronous ZeroMQ sockets for the data transfer between the server and the client. Please review the _Sample Input_ and  _Sample Output_ sections below to understand the expected input and output results. Example calls and a UML sequence diagram are also provided to illustrate the communication flow between the server and client. The microservice file is listed as _json_server.py_.

### Dependencies:
```
   import zmq
   import json
   import signal
   import sys
```
### Socket Setup 

    PORT = 5557
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:" + str(PORT))

### Sample Input:
```json
input_data = 
{
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
```

### Sample Output:
```json
output_data = 
{
   "type": "object",
   "properties": {
    "section1": {
      "type": "null",
      "title": "section1_title",
      "description": "section1_desc_optional"
    },
    "checkbox1.1": {
      "type": "boolean",
      "title": "checkbox1.1_text",
      "description": "checkbox1_desc_optional"
    },
    "checkbox1.2": {
      "type": "boolean",
      "title": "checkbox1.2_text"
    }
   }
}
```

### Sending/Receiving Data
The client sends a JSON object using the following call:

    socket.send_json(input_data)
    
The server receives the data using the following call:

    request = socket.recv_json()
The server then refactors the JSON object to the sample output formatting (seen above) and sends a JSON object back to the client using:

    socket.send_json(output_data)
    
Clients can receive the JSON object using the call:

    Clients can receive the JSON object using the following call:

    
### UML Sequence Diagram
 ![image](https://user-images.githubusercontent.com/67238817/236879142-eff1467e-1a6b-4973-b374-b0c5f4f7bb29.png)
 
### Citations
Referenced ZeroMQ socket template to setup synchronous json_server.py and json_client.py connection, found here: https://zguide.zeromq.org/docs/chapter1/


