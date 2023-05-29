Feature: Register Account functionality

  @regi1
  Scenario: Register with mandatory fields
    Given I navigate to Register page
    When I enter details into mandatory fields
    And I select privacy policy checkbox
    And I click on continue button
    Then Account should get created

  @regi2
  Scenario: Register with all fields
    Given I navigate to Register page
    When I enter details into all fields
    And I select privacy policy checkbox
    And I click on continue button
    Then Account should get created

  @regi3
  Scenario: Register with a duplicate email address
    Given I navigate to Register page
    When I enter details into all fields except email field
    And I enter existing accounts email into email field
    And I select privacy policy checkbox
    And I click on continue button
    Then Proper warning message informing about duplicate account should be displayed

  @regi4
  Scenario: Register without providing any details
    Given I navigate to Register page
    When I dont enter any details in fields
    And I click on continue button
    Then Proper warning messages for every mandatory fields should be displayed
