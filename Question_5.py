def full_name():
    firstName= input("Enter first name:")
    lastName= input("Enter last name:")
    f=firstName[::-1]
    l=lastName[::-1]
    print(f,"",l)

full_name()