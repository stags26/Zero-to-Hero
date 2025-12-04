name = "ada Lovelace"
print (name.title())
print (name.upper())
print (name.lower())

first_name = "ada"
last_name = ("lovelace")
full_name = f"{first_name} {last_name}" #This variable captures the value of both variables (first_name and last_name) in a f string
print(full_name)
message = f"Hello, {full_name.title()}!" #This variable add "Hello" to the f string 
print(message)
