Feature: The API

  Scenario: Connecting to the API
     When you send a GET request to the root resource
     Then the status is "200"
      And the "Content-Type" header is "application/hal+json"
      And the JSON response contains
          """
          {
            "hello": "world!"
          }
          """
