Feature: showing off behave

  Scenario: add student to empty list
     Given we have empty list
      When we add student to list
      Then there is one student on list

  Scenario: add more students to list
     Given we have list with one student
      When we add student to list
      Then there are two students on list

  Scenario: delete only student in list
    Given we have list with one student
    When we delete student from list
    Then student list is empty

  Scenario: delete one of students in list
    Given we have list with two students
    When we delete student from list
    Then there is one student on list


  Scenario: check id of only student in list
    Given we have empty list
    When we add student to list
    Then student with id 1 exists
