#4-10
animals = ['fish', 'sharks', 'dolphins']
for animal in animals:
    #print (animal)
    print (f"{animal.title()} would be a cool pet!")
print ("\nAny type of fish would make a great pet!")  #end of original exercise

animals.append('whales')
animals.append('shrimp')
animals.append('crabs')
print(animals[:3])
print(animals[1:5])
print(animals[3:])
print("\n")

#4-11
pizzas = ['pepperoni', 'cheese', 'white']
for pizza in pizzas:
    #print (pizza)
    print (f"One of my favorite kinds of pizza is {pizza.title()}")
print (f"There are many different kinds of pizza but my favorites are {','.join(pizza.title() for pizza in pizzas[:-1])} and {pizzas[-1].title()}.")
print ("I really like pizza!")  #end of original exercise

friends_pizza = pizzas[:]
friends_pizza.append('pineapple')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(f"{pizza.title()}")

print("\nMy friends favorites pizzas are: ")
for pizza in friends_pizza:
    print(f"{pizza.title()}")

print("\n")

#4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food.title())

print("\nMy friend's favorite foods are:")
for food in friends_foods:
    print(food.title())

print("\n")

#4-13
buffet_items = ('steak', 'potatoes', 'beans', 'gravy', 'carrots')
#buffet_items[0] = 'corn'

for item in buffet_items:
    print(item)

print("\n")

buffet_items = ('corn', 'chicken', 'beans', 'gravy', 'carrots')
for item in buffet_items:
    print(item)
