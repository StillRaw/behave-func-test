Feature: Test values whether they are numeric or not.

  Scenario: val1 is not integer or float.
    Given Function runss
    When I input string "a" and numeric "10" to function
    Then I get result cautious "Values must be numeric!"

  Scenario: val2 is not integer or float.
    Given Function runss
    When I input string "10" and numeric "a" to function
    Then I get result cautious "Values must be numeric!"

  Scenario: val1 is whitespace.
    Given Function runss
    When I input string " " and numeric "10" to function
    Then I get result cautious "Values must be numeric!"

  Scenario: val2 is whitespace.
    Given Function runss
    When I input string "10" and numeric " " to function
    Then I get result cautious "Values must be numeric!"

  Scenario: val1 is null.
    Given Function runss
    When I input string "None" and numeric "10" to function
    Then I get result cautious "Values must be numeric!"

  Scenario: val2 is null.
    Given Function runss
    When I input string "10" and numeric "None" to function
    Then I get result cautious "Values must be numeric!"


