#Bean Calculator
#An XR Studios project

#Calculates how many beans you have based on weight.



#Print the intro.
print("\033[32m\n          Welcome to the\n Black Bean Calculation Protocol")
print("\033[31m=====================================")
print("\033[36m    Made by Space Yeti Studios\n           (Jackson M.)\n\n")


input("       Press enter to start.")

#Ask the user how many pounds of black beans they have.

weight_of_beans = float(input("\n\n\033[34m  How many pounds of black beans\n           do you have?\n           (In pounds)\033[31m\n               "))



try:
  amount_of_beans = weight_of_beans * 11339.8
  print("\033[32mYou have about", amount_of_beans, "black beans.")
except:
  print("\033[31mError! Please enter a number.")
