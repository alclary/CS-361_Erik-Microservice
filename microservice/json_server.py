import zmq
import json
import signal
import sys

# cite: https://zguide.zeromq.org/docs/chapter1/
# Set up the ZeroMQ context and socket
PORT = 5557
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:" + str(PORT))
interrupted = False  # used for CTRL+C signal handling

# function to handle http requests
def handle_request(request):
    input_data = request

    # init. output_data format
    output_data = {
        "type": "object",
        "properties": {}
    }

  # data transformation - populates 'output_data':
    # loop over 'sections' to modify data
    for sect_index, sect in enumerate(input_data["sections"]): 
        
      # create key 
      sect_key = f"section{sect_index + 1}"

      # create section's type, title 
      sect_data = {
        "type": "null",
        "title": sect["sectionTitle"]
      }

      # append 'description' if it exists
      descript = sect.get("sectionDesc")
      if descript != "NULL" and descript is True:
          sect_data["description"] = descript

      # combine with output_data
      output_data["properties"][sect_key] = sect_data

      # nested loop over sect's 'checkItems' 
      for check_index, check_item in enumerate(sect["checkItems"]):
          
          # create key
          check_key = f"checkbox{sect_index + 1}.{check_index + 1}"

          # create checkbox's type, title and description
          checkbox_data = {
              "type": "boolean",
              "title": check_item["checkboxText"]
          }

          # append 'description' if it exists
          descript = check_item.get("checkboxDesc")
          if descript != "NULL" and descript is True:
              checkbox_data["description"] = descript

          # combine with output_data
          output_data["properties"][check_key] = checkbox_data

    output_data = json.dumps(output_data)
    return (output_data)

# will cause the stop of server if CTRL+C hit in terminal
def signal_handler(signum, frame):
    print("Server stopped")
    sys.exit(0)

print(f"json conversion server running on port #{PORT} ....")
signal.signal(signal.SIGINT, signal_handler)

# infinite loop to process .recv / .send 
while True:

    try:
        # Wait for an incoming request, zmq.NOBLOCK allows for signal interruption prior to recieved request
        request = socket.recv_json(zmq.NOBLOCK)

        # data transformation
        response = handle_request(request)

        # Send the response back to the client
        socket.send_json(response)
        print("response sent successfully")
    
    # check for server termination using CTRL+C
    except zmq.ZMQError as error:
        if interrupted:
            break
        else:
            continue

