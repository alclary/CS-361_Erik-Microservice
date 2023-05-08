# JSON Conversion Microservice

## About
This is a microservice impelmented to transforms JSON objects from the Sample Input to the Sample Output formatting, listed below.
This microservice uses synchronous ZeroMQ sockets for the requests/responses data transfer. Review the Sample Input / Sample Output sections to understand expected input/output results. Example calls and a UML sequence diagram are listed below to show how the server & client communcate.

### Sample Input:
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

### Sample Output:
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

### Sending/Receiving Data
Client can sends a JSON object using the call:
    **socket.send_json(input_data)**
    
Server receives data using the call:
    **request = socket.recv_json()**
Server then refactors the JSON object to the sample output formatting (seen above) and sends a JSON object back to the client using:
    **socket.send_json(output_data)**
    
Clients can receive the JSON object using the call:
    **message = socket.recv_json()**
    
### UML Sequence Diagram
 ![image](https://user-images.githubusercontent.com/67238817/236879142-eff1467e-1a6b-4973-b374-b0c5f4f7bb29.png)


