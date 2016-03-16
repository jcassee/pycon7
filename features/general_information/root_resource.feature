Feature: The root resource
  The root resource is the only resource that is located by its URI. Its main purpose it to provide links to the different API components. Getting the root resource if often the first thing a client does when using the API.

  The URI of the root resource is https://api.registronavale.com.

  Scenario: Connecting to the API
     When you get the root resource
     Then the status is "200"
      And the "Content-Type" header is "application/hal+json"
      And the representation contains
          """json
          {
            "version": "0.1"
          }
          """
