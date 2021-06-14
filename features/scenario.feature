  Feature: Flight tickets
    As a user I want to find tickets for a plane from Kyiv to Berlin and back for 2021-07-05 and 2021-07-09

    Scenario: Find tickets for necessary date on Ryanair website if they are available
      Given a customer enters a browser
      When a customer clicks ryanair website link
      And sends a filled search form
      Then the customer finds the tickets if they are available