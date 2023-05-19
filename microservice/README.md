# JSON Object Microservice

## About
This is a Python-based microservice that transforms JSON objects from a specific input format to the distinct output format described below. It utilizes synchronous ZeroMQ sockets for the data transfer between the server and the client. Please review the _Sample Input Data_ and  _Sample Output Data_ sections below to understand the expected input and output results. Example calls and a UML sequence diagram are also provided to illustrate the communication flow between the server and client. The microservice file is named _json_server.py_.

### Dependencies:
```
   import zmq        # ZeroMQ library for messaging and socket communication
   import json       # JSON library for wokring with JSON data
   import signal     # Allows for python signal handling 
   import sys        # Allows for manipulation of python runtime environment
```

### Sample Input Data:
The input JSON object should follow the structure below:

```json
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

### Sample Output Data:
The ouput JSON object will be in the following format:
```json
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
### Socket Setup 
Below is the ZeroMQ socket setup:

    PORT = 5557
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:" + str(PORT))
    
### Communcation of Data
1. The client sends the input JSON object to the server using **socket.send_json()** .
2. The server recieves the JSON object using the **socket.recv_json()** method.
3. The server process and transforms the received JSON object, creating a newly formatted JSON object.
4. The server sends this newly formatted output JSON object back to the client using the **socket.send_json()** method.
5. The client receives the output JSON object using **socket.recv_json()**.
    
### UML Sequence Diagram
 ![image](https://user-images.githubusercontent.com/67238817/236879142-eff1467e-1a6b-4973-b374-b0c5f4f7bb29.png)
 
### Citations
Referenced ZeroMQ socket template to setup synchronous json_server.py and json_client.py connection, found here: https://zguide.zeromq.org/docs/chapter1/


