# coffee-machine

My take on the coffee machine working "algorithm".
It imitates the work of a coffee machine.
First it asks user for a type of coffee.
Then it checks if there are enough resources available.
If so, then asks user to "insert" coins.
Then it calculates if user input enough to pay for the coffee.
If not then the money is "given back" to the user.
Otherwise, it checks if user should be given change, 
and if so it prints the amount that should be returned.

If there are insufficient resources for a selected coffe then a message
saying so is printed.

There are 2 additional prompts for "maintenance"
- report, prints amount of resources:
  - water
  - milk
  - coffee
  - money
- off, terminates the program, which imitates the possibility of turning the
machine off