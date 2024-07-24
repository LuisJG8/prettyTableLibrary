# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

column1 = table.add_column("Pokemon Name", ["Pikachu\nSquirtle\nCharmander"])
column2 = table.add_column("Type", ["Electric\nWater\nFire"])
# row = table.add_row(row="nose")
# row3 = table.add_row(row="nose")
table.align = 'r'
print(table)