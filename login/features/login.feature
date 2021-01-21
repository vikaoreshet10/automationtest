Feature: Login in ministra

  Scenario Outline: sing in in ministra <credentials>
     Given open main page ministra <portal>
      Then write your user <login> and <password>
      Then click on button sing in
      Then check login
	 Examples: Vary
	 				|credentials     |login         |password 	|portal                         |
					|valid    	     |admin 		|qweqwe123     |http://10.110.51.251/stalker_portal/|
                    |invalid         |emeralds      |1          |http://10.110.51.251/stalker_portal/|