def greeting_user(name,greeting="Hello"):
    return greeting+","+name+"!"
greeting1=greeting_user("Bob")
greeting2=greeting_user("Charlie","Hi")
print(greeting1)
print(greeting2)