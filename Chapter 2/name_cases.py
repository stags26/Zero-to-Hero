first_name = "Eric" #This part of the program changes the case of the text in the function (first_name)
print (f"Hello {first_name.lower()}, would you like to learn some Python today?")
print (f"Hello {first_name.upper()}, would you like to learn some Python today?")
print (f"Hello {first_name.title()}, would you like to learn some Python today?")

message = 'once said, "A person who never made a mistake never tried anything new."'
famous_person = "Albert Einstein"
print (f"{famous_person.title()} {message}")

first_name = "  Eric  " #This part of the program uses the different stripper functions
print (f"\t{first_name}")
print (f"\n{first_name}")
print (f"\n{first_name.lstrip()}")
print (f"\t\n{first_name.rstrip()}")
print (f"{first_name.strip()}")
