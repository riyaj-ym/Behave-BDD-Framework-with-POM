Feature: Search functionality

  @search1
  Scenario: Search for valid product
    Given I got navigated to Home page
    When I enter valid product say "Hp" into Search box field
    And I click on Search button
    Then Valid product should get displayed in Search results

  @search2
  Scenario: Search for invalid product
    Given I got navigated to Home page
    When I enter invalid product say "Honda" into Search box field
    And I click on Search button
    Then Proper message should be displayed in Search results

  Scenario: Search without entering any product
    Given I got navigated to Home page
    When I don't enter any product into Search box field
    And I click on Search button
    Then Proper message should be displayed in Search results



