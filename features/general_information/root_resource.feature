Feature: The root resource
  The root resource is the only resource that is located by its URI. Its main purpose it to provide links to the different API components. Getting the root resource if often the first thing a client does when using the API.

  The URI of the root resource is https://api.registronavale.com.

  Scenario: Connecting to the API
     When you get the resource at "https://api.registronavale.com"
     Then the status is "200"
      And the "Content-Type" header is "application/hal+json"
      And the representation is
          """json
          {
            "version": "0.2",
            "_links": {
              "self": {
                "href": "https://api.registronavale.com/"
              },
              "http://rels.registronavale.com/ship-by-imo": {
                "href": "https://api.registronavale.com/ship/{imo}",
                "templated": true
              },
              "http://rels.registronavale.com/search-ships": {
                "href": "https://api.registronavale.com/search{?q}",
                "templated": true
              }
            }
          }
          """
