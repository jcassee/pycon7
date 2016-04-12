Feature: Getting information about a ship owner

  Scenario: Get a ship's owner
    Given a company named "Rederij Joost"
      And a ship named "Providence" with imo "12345" owned by "Rederij Joost"
     When you get the ship "Providence"
      And you follow the relation "http://rels.registronavale.com/ship-owner"
     Then the profile is "http://profiles.registronavale.com/company"
      And the representation is
          """json
          {
              "name": "Rederij Joost",
              "_links": {
                  "profile": {
                      "href": "http://profiles.registronavale.com/company"
                  },
                  "self": {
                      "href": "https://api.registronavale.com/company/1"
                  },
                  "http://rels.registronavale.com/owned-ships": {
                      "href": "https://api.registronavale.com/company-ships/1"
                  }
              }
          }
          """
