def wish_jacob_happy_birthday(age, name):
    # ASCII birthday cake icon
    birthday_icon = '''
         ,,,,,
        (∩_∩)
       _|_____|_
      | _______ |
     |::|~|~|~|::|
     |::|~|~|~|::|
     |::|_|_|_|::|
     |:::::::::::|
     `""""""""""""` 
    '''
    
    print(birthday_icon)
    print(f"# Celebrating {name}'s {age}th Orbit! 🎂")
    print("\nInitializing Birthday Sequence...")
    for i in range(age):
        print(f"Iteration {i+1}: Sending joyful bytes!")
    print(f"HAPPY {age}th BIRTHDAY, {name.upper()}!")
    print("Wishing you a year filled with positive code and zero bugs!")


# Call the function directly
wish_jacob_happy_birthday(27, "Jacob")
