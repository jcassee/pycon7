Feature: Searching for ships

  Scenario: Search for ships
     When you get the resource at "https://api.registronavale.com"
      And you follow the relation "http://rels.registronavale.com/search-ships" with parameters
          | param | value         |
          | q     | search string |
     Then the status is "200"
      And the "Content-Type" header is "application/hal+json"
      And the profile is "http://profiles.registronavale.com/collection"


  Scenario: Search for a ship
    Given a ship named "Providence" with imo "12345"
     When you get the resource at "https://api.registronavale.com"
      And you follow the relation "http://rels.registronavale.com/search-ships" with parameters
          | param | value |
          | q     | Prov |
      And you follow the embedded relation "item"
      And you take the first resource
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
