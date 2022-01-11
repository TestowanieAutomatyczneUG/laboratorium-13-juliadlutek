Feature: showing off behave

  Scenario: password is valid
      When we check password Password1$
      Then result is True

  Scenario: password has a number, cap and special character, but it's too short
      When we check password P1$
      Then result is False

  Scenario: password has enough length, cap and special character, but it doesn't have number
    When we check password Password$
    Then result is False

  Scenario: password has enough length, number and special character, but it doesn't have cap
    When we check password pasword1$
    Then result is False

  Scenario: password has enough length, number and cap, but it doesn't have special character
    When we check password Password1
    Then result is False

  Scenario: password is number
    When we check password 12345
    Then function raises ValueError

  Scenario: password is none
    When we check password None
    Then function raises ValueError

  Scenario: password is empty string
    When we check empty string
    Then function raises Exception


