Feature: Getting information about companies that own ships

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
                "href": "https://api.registronavale.com/company-ships/1",
                "deprecation": "http://apidocs.registronavale.com/deprecation/ship-owner"
              },
              "http://rels.registronavale.com/owner-history": {
                "href": "https://api.registronavale.com/company-ships-history/1"
              }
            }
          }
          """

  Scenario: Get the ships owned by a company
    Given a company named "Rederij Joost"
      And a ship named "Providence" with imo "12345" owned by "Rederij Joost"
     When you get the company "Rederij Joost"
      And you follow the relation "http://rels.registronavale.com/owned-ships"
      And you follow the embedded relation "item"
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
              "http://rels.registronavale.com/ship-owner": {
                "href": "https://api.registronavale.com/company/2",
                "deprecation": "http://apidocs.registronavale.com/deprecation/ship-owner"
              },
              "http://rels.registronavale.com/owner-history": {
                "href": "https://api.registronavale.com/ship-owners-history/12345"
              }
            }
          }
          """
