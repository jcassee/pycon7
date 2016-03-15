Feature: Ships registry

  Scenario: Connecting to the API
     When you send a GET request to "https://api.registronavale.com"
     Then the status is "200"
      And the "Content-Type" header is "application/json"
      And the JSON response contains
          """
          {
            "hello": "world!"
          }
          """

  Scenario: Search for a ship using it's IMO-number
    Given a ship named "Providence" with imo "12345"
     When you send a GET request to "https://api.registronavale.com"
      And you follow the link relation "http://rels.registronavale.com/get-by-imo" with parameters
          | param | value |
          | imo   | 12345 |
     Then the status is "200"
      And the "Content-Type" header is "application/json"
      And the JSON response contains
          """
          {
            "imo": 12345,
            "name": "Providence"
          }
          """

  Scenario: Search for a ship using a IMO-number that does not exist
    Given the registry contains no ships
     When you send a GET request to "https://api.registronavale.com"
      And you follow the link relation "http://rels.registronavale.com/get-by-imo" with parameters
          | param | value |
          | imo   | 12345 |
     Then the status is "404"
