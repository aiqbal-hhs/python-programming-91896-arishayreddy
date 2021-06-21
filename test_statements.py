Delivery = 10
Pizza_Price = 15
num_pizza = int(input("How many pizzas do you want?"))
order_total = num_pizza * Pizza_Price
if num_pizza > 3:
    print("The delivery cost is ${}".format(Delivery))
    print("You get Free Delivery!")
    print("Order Total ${}".format(order_total))
    order_total += Delivery
if num_pizza < 3:
        print("Pizza night!")
        print("Order Total ${}".format(order_total))

print("Hello")

ans = input("Who is the current PM of NZ?  \n A. Jacinda Ardern \n B. Judith Collins ").lower()
if ans.lower() == "A":
  print("Correct!")
if ans.lower() == "B":
  print("Incorrect")


print("Hello")
# Integer input question answer
ans = int(input("Who is the current PM of NZ?  \n A. Jacinda Ardern \n B. Judith Collins "))
if ans == 1:
  print("Correct!")
if ans == 2:
  print("Incorrect")
