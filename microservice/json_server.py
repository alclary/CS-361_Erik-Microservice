import zmq
import json

# cite: https://zguide.zeromq.org/docs/chapter1/
# Set up the ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

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

      # nested loop over sect's 'checkItems' to modify data
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


print("json conversion server running....")
# infinite loop to process .recv / .send 
while True:
    # Wait for an incoming request
    request = socket.recv_json()

    # data transformation
    response = handle_request(request)

    # Send the response back to the client
    socket.send_json(response)
    print("response sent successfully")

