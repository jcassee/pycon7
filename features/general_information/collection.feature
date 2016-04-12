Feature: Collections
  In many cases the API returns a collection of resources. The response will be a resources that embeds the collection elements using the `item` relation.

  Scenario: Getting a collection with elements
    Given a ship named "Providence" with imo "12345"
      And a ship named "Providence II" with imo "12346"
    When you search the registry with query "Providence"
     Then the profile is "http://profiles.registronavale.com/collection"
      And the representation is
          """json
          {
            "_links": {
              "profile": {
                "href": "http://profiles.registronavale.com/collection"
              },
              "self": {
                "href": "https://api.registronavale.com/search?q=Providence"
              }
            },
            "_embedded": {
              "item": [
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
                },
                {
                  "imo": 12346,
                  "name": "Providence II",
                  "_links": {
                    "profile": {
                      "href": "http://profiles.registronavale.com/ship"
                    },
                    "self": {
                      "href": "https://api.registronavale.com/ship/12346"
                    }
                  }
                }
              ]
            }
          }
          """

  Scenario: Getting an empty collection
    Given the registry contains no ships
    When you search the registry with query "Providence"
    Then the profile is "http://profiles.registronavale.com/collection"
     And the representation is
          """json
          {
            "_links": {
              "profile": {
                "href": "http://profiles.registronavale.com/collection"
              },
              "self": {
                "href": "https://api.registronavale.com/search?q=Providence"
              }
            }
          }
          """
