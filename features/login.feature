Feature: Login Functionality

  @login
  Scenario: Login with valid credentials
    Given I navigated to Login page
    When I enter valid email and valid password into the fields
    And I clicked on Login button
    Then I should get logged in

  @login1
  Scenario: Login with invalid email and valid password
    Given I navigated to Login page
    When I enter invalid email and valid password into the fields
    And I clicked on Login button
    Then I should get proper warning message

  @login2
  Scenario: Login with valid email and invalid password
    Given I navigated to Login page
    When I enter valid email and invalid password into the fields
    And I clicked on Login button
    Then I should get proper warning message

  @login3
  Scenario: Login with invalid credentials
    Given I navigated to Login page
    When I enter invalid email and invalid password into the fields
    And I clicked on Login button
    Then I should get proper warning message

  Scenario: Login without any credentials
    Given I navigated to Login page
    When I dont enter any email and password into the fields
    And I clicked on Login button
    Then I should get proper warning message



