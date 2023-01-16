Feature: Test listing odd numbers between two given numbers by including given numbers.

  Scenario Outline: num1 and num2 are positive integers and num1<num2.
    Given Function runs
    When I input "1" and "10" to function
    Then I get result <List>
    Examples: Output Variables
      | List        |
      | [1,3,5,7,9] |
  Scenario Outline: num1 and num2 are positive floats and num1<num2.
    Given Function runs
    When I input "1.2" and "10.5" to function
    Then I get result <List>
    Examples: Output Variables
      | List      |
      | [3,5,7,9] |
  Scenario Outline: num1 and num2 are positive floats and num1>num2.
    Given Function runs
    When I input "10.5" and "1.2" to function
    Then I get result <List>
    Examples: Output Variables
      | List      |
      | [3,5,7,9] |
  Scenario Outline: num1 and num2 are positive floats and num1>num2.
    Given Function runs
    When I input "10.5" and "1.2" to function
    Then I get result <List>
    Examples: Output Variables
      | List      |
      | [3,5,7,9] |
  Scenario Outline: num1 and num2 are negative integers and num1<num2.
    Given Function runs
    When I input "-10" and "-1" to function
    Then I get result <List>
    Examples: Output Variables
      | List                |
      | [-9, -7, -5, -3,-1] |
  Scenario Outline: num1 and num2 are negative floats and num1<num2.
    Given Function runs
    When I input "-10.5" and "-1.2" to function
    Then I get result <List>
    Examples: Output Variables
      | List             |
      | [-9, -7, -5, -3] |
  Scenario Outline: num1 and num2 are negative integer and num1>num2.
    Given Function runs
    When I input "-1" and "-10" to function
    Then I get result <List>
    Examples: Output Variables
      | List                |
      | [-9, -7, -5, -3,-1] |
  Scenario Outline: num1 and num2 are negative floats and num1>num2.
    Given Function runs
    When I input "-1.2" and "-10.5" to function
    Then I get result <List>
    Examples: Output Variables
      | List             |
      | [-9, -7, -5, -3] |
  Scenario Outline: num1 and num2 is integer odd number num1=num2.
    Given Function runs
    When I input "-1" and "-1" to function
    Then I get result <List>
    Examples: Output Variables
      | List |
      | [-1] |
  Scenario Outline: num1 and num2 is integer even number num1=num2.
    Given Function runs
    When I input "2" and "2" to function
    Then I get result <List>
    Examples: Output Variables
      | List                                  |
      | ["No value found in given interval."] |