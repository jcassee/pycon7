Feature: Getting a ship

  Scenario: Get a ship using it's IMO-number
    Given a ship named "Providence" with imo "12345"
     When you get the root resource
      And you follow the link relation "http://rels.registronavale.com/get-ship" with parameters
          | param | value |
          | imo   | 12345 |
     Then the status is "200"
      And the "Content-Type" header is "application/hal+json"
      And the profile is "http://profiles.registronavale.com/ship"
      And the representation contains
          """
          {
            "imo": 12345,
            "name": "Providence"
          }
          """

  Scenario: Use an IMO-number that does not exist
    Given the registry contains no ships
     When you get the root resource
      And you follow the link relation "get-ship" with parameters
          | param | value |
          | imo   | 12345 |
     Then the status is "404"
