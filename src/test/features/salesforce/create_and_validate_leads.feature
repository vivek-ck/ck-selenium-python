Feature: Salesforce user must be able to login to the application and create Leads

  Scenario Outline: Login to SalesForce application and create Leads
    Given the SalesForce login page is opened
    When the user logs in with credentials
    And the user navigates to the Leads page
    And the user creates new lead with Salutation "<salutation>", LastName "<lastName>", Company "<company>"
    Then the Lead with name "<lastName>" should be present in the Leads list

    Examples: 
      | salutation | lastName | company  |
      | Mr.        | test0026 | company1 |
      # | Ms.        | test0007 | company2 |
      # | Mrs.       | test0008 | company1 |
      # | Dr.        | test0009 | company2 |