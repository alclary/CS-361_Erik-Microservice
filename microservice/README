# JSON Conversion Microservice

## About
This is a microservice impelmented to transforms JSON objects from the sample input to a sample output formatting, listed below.
This microservice uses synchronous ZeroMQ sockets for the request/response data transfer. 




#### Sample Input:
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

# send data      
socket.send_json(input_data)


#### Sample Output:
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
