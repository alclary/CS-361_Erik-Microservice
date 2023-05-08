import zmq
import json

# cite: https://zguide.zeromq.org/docs/chapter1/
# Set up the ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5557")

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

# send data      
socket.send_json(input_data)

# get the transformed data as a reply
message = socket.recv_json()
print(f"Received reply [ {message} ]")


