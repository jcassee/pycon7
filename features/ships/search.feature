Feature: Searching for ships

  Scenario: Search for a ship
    Given a ship named "Providence" with imo "12345"
     When you get the resource at "https://api.registronavale.com"
      And you follow the relation "http://rels.registronavale.com/search-ships" with parameters
          | param | value |
          | q     | Prov  |
      And you follow the relation "item"
      And you take the first resource
     Then the representation is
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
              },
              "http://rels.registronavale.com/owner-history": {
                "href": "https://api.registronavale.com/ship-owners-history/12345"
              }
            }
          }
          """
