Feature: Getting information about a ship owner

  Scenario: Get a ship's owner
    Given a company named "Rederij Joost"
      And a ship named "Providence" with imo "12345" owned by "Rederij Joost"
     When you get the ship "Providence"
      And you follow the embedded relation "http://rels.registronavale.com/owner"
     Then the profile is "http://profiles.registronavale.com/company"
      And the representation contains
          """json
          {
            "name": "Rederij Joost"
          }
          """
