import sys

from random import randint

choice = int(input("Введите длину пароля: "))

choice_num_chr = input("Делать ли фильтрацию по цифрам? (y, n): ")

if choice_num_chr.lower() == "y":
    choice_num_chr = True
elif choice_num_chr.lower() == "n":
    choice_num_chr = False
else:
    print("Необходимо ввести лишь 'y' или 'n'")
    exit()
    
password = ""
if choice_num_chr == True:
    for i in range(choice):
        if randint(1, 2) == 1:
            password += chr(randint(33, 47))
        else:
            password += chr(randint(58, 126))
else:
    for i in range(choice):
        password += chr(randint(33, 126))

            
print("Сгенерированный пароль: ", password)