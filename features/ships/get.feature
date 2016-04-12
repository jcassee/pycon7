Feature: Getting a ship

  Scenario: Get a ship using it's IMO-number
    Given a ship named "Providence" with imo "12345"
     When you get the resource at "https://api.registronavale.com"
      And you follow the relation "http://rels.registronavale.com/ship-by-imo" with parameters
          | param | value |
          | imo   | 12345 |
     Then the profile is "http://profiles.registronavale.com/ship"
      And the representation is
          """json
          {
              "imo": 12345,
              "name": "Providence",
              "_links": {
                  "profile": {
                      "href": "http://profiles.registronavale.com/ship"
                  },
                  "self": {
                      "href": "https://api.registronavale.com/ship/12345"
                  }
              }
          }
          """

  Scenario: Use an IMO-number that does not exist
    Given the registry contains no ships
    When you get the resource at "https://api.registronavale.com"
      And you follow the relation "http://rels.registronavale.com/ship-by-imo" with parameters
          | param | value |
          | imo   | 12345 |
     Then the status is "404"
