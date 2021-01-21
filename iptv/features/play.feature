Feature: Play valid channel

  Scenario Outline: Play valid channel link <credentials>
     Given I am login in web player <portal> and <login> and <password> and <licenses>
     Then Select channel from the list
     Then Press button Play
     Then Check TV guide

    Examples: Vary
             | credentials | login | password | portal                       | licenses     |
             | valid       | 12541 | 1        | http://10.110.51.251/player/ | 21957134FE09 |