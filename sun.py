food={1:"idly",2:"dosa",3:"bonda",4:"puri"}
print(food)
a=int(input("enter the least like food:"))
if a in food:
    food.pop(a)
print(food)
