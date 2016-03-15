Feature: Searching for ships

  Scenario: Search for ships
     When you get the root resource
      And you follow the link relation "http://rels.registronavale.com/search-ships" with parameters
          | param | value         |
          | q     | search string |
     Then the status is "200"
      And the "Content-Type" header is "application/hal+json"
      And the profile is "http://profiles.registronavale.com/collection"

  Scenario: Search for a ship
    Given a ship named "Providence" with imo "12345"
     When you get the root resource
      And you follow the link relation "http://rels.registronavale.com/search-ships" with parameters
          | param | value |
          | q     | Prov |
      And you follow the embedded relation "item"
      And you take the first resource
     Then the profile is "http://profiles.registronavale.com/ship"
      And the representation contains
            """
            {
              "imo": 12345,
              "name": "Providence"
            }
            """
