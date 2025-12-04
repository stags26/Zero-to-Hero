pizzas = ['pepperoni', 'cheese', 'white']
for pizza in pizzas:
    #print (pizza)
    print (f"One of my favorite kinds of pizza is {pizza.title()}")
print (f"There are many different kinds of pizza but my favorites are {','.join(pizza.title() for pizza in pizzas[:-1])} and {pizzas[-1].title()}.")
print ("I really like pizza!")