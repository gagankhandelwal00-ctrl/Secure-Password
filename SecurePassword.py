name = input("Enter your name:")
nickName = input("Enter your nickname:")
year = input("Enter your birth year:")

password  = name[:3]+nickName[1:4]+ year[::-1]
print(f"Your secure password is:{password}")