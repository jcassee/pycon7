Feature: Ships registry

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

  Scenario: Search for a ship using it's IMO-number
    Given a company named "Rederij Joost"
      And a ship named "Providence" with imo "12345" owned by "Rederij Joost"
     When you send a GET request to the root resource
      And you follow the link relation "get-ship" with parameters
          | param | value |
          | imo   | 12345 |
     Then the status is "200"
      And the "Content-Type" header is "application/hal+json"
      And the JSON response contains
          """
          {
            "imo": 12345,
            "name": "Providence"
          }
          """

  Scenario: Search for a ship that does not exist
    Given the registry contains no ships
     When you send a GET request to the root resource
      And you follow the link relation "get-ship" with parameters
          | param | value |
          | imo   | 12345 |
     Then the status is "404"

#  Scenario: Search for a ship
#    Given a company named "Rederij Joost"
#    And a ship named "Providence" with imo "12345" owned by "Rederij Joost"
#     When you send a GET request to the root resource
#      And you follow the link relation "search-ships" with parameters
#          | param | value |
#          | q     | Prov |
#     Then the status is "200"
#      And the "Content-Type" header is "application/hal+json"
#      And the JSON response contains
#            """
#            {
#              "imo": 12345,
#              "name": "Providence"
#            }
#            """
