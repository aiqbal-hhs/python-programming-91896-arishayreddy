#This is my age
my_age = 16
#Ask user for thier age
your_age = int(input("What is your age? " ))
#If age is 16 then we are the same age
if your_age == 16:
  print("We're the same age") 
 #If age is greater than 20, they would have gone past their high school years
elif your_age > 20 :
  print("You've finished High School a few years ago")
elif your_age < 16:
  print("You are younger than me")
else: 
  print("I'm {}".format(my_age))
