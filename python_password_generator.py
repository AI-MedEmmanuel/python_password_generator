#importing my module 
import random

#creating my list
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
symbols = ['@', '#', '$', '%', '^', '&', '&', '*', '(', ')', '-', '=', '+']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#adding the list all together
all_char = lowercase_letters + uppercase_letters + symbols + digits

#prompt questions
password_prompt = int(input("How many characters do you want in your password? "))
password_num = int(input("How many passwords do you want? "))

#outer for-loop
for _ in range(password_num):
    password = []

    #inner for-loop
    for _ in range(password_prompt):
        option = random.choice(all_char)
        password.append(option)
        
    #shuffling the password       
    random.shuffle(password)
    final_password = "". join(password)
    print(f"Your password 🔐 is ---> {final_password}")
