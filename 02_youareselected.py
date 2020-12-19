letter= ''' Dear, <|NAME|> 
You are selected!
dated: <|DATE|>
'''
name = input("Enter your Name: ")
date = input("Ente the date: ")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)