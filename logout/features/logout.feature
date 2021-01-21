Feature: Logout from ministra

  Scenario Outline: sing in in ministra <credentials>
     Given open main page web player <portal>
      Then write your user <login> and <password>
      Then click on button sing in
      Then check login
    Then click to logout
	 Examples: Vary
	 				|credentials     |login         |password 	|portal                         |
					|valid    	     |admin 		|qweqwe123     |http://10.110.51.251/stalker_portal/|