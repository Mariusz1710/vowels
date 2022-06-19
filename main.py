from functions import del_vow, del_con

while True:
    text = input("Enter the text:  ")
    print("""What do you want to delete:
1. Vowels
2. Consonants
0. Exit""")

    choice = input()

    if choice == "1":
        print(del_vow(text))
    elif choice == "2":
        print(del_con(text))
    elif choice == "0":
        print("Thank you for using our program\nPlease come back soon!")
        exit()
    else:
        print("You have entered the wrong character")