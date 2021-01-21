Feature: Login in Web player

  Scenario Outline: sing in in web player <credentials>
    Given open main page web player <portal>
      Then write your user <login> and <password>
      Then click on button sing in
      Then click on tab radio
    Then click on button add radiostation
    Then enter information
    Then click save
    Then search radiostation
    #Then delete radiostation
	 Examples: Vary
	 				|credentials     |login         |password 	|portal                         |
					|valid    	     |admin 		|qweqwe123     |http://10.110.51.251/stalker_portal/|
