import os
balance = 10000
attempts = 0 
success = True 

while success: 
    pin = input("Enter your PIN to withdraw/deposit cash or q to quit: ") 
     
    if pin == "4567": 
        print(f"{'-' * 20:^20}")
        print("Correct Pin Entered!") 
        print(f"{'-' * 20:^20}")
    
        print(f"You have {balance} baht in your account")
        break
    elif pin == "q":
        exit()

    else: 
        attempts += 1 
        print(f"Attempt# {attempts}.Incorrect PIN! Try Again")
        if attempts == 3: 
            success = False 
            print("Your account is locked. Please contact bank.")
            exit()

while success:

    choice = input("Press 1 to deposit or 2 to withdraw:")  
    if choice == "1":
        try:
            amount = int(input("Enter an amount to deposit:"))
            if amount <= 0:
                print("Deposit amount must be positive.")
            else:
                balance += amount
                print(f"{'-' * 43:^43}")
                print(f"|{'DEPOSIT FUND':^20}|{'BALANCE':^20}|")
                print(f"|{amount:^20}|{balance:^20}|")
                print(f"{'-' * 43:^43}")
                input("Press enter to contiune.")
                os.system("cls")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "2":
        try:
            amount = int(input("Enter an amount to withdraw:"))
            if amount <= 0:
                print("Withdrawal amount must be positive.")
            elif amount > balance:
                print("Your credit is not enough")
            else:
                balance -= amount
                print(f"{'-' * 43:^43}")
                print(f"|{'WITHDRAWAL FUND':^20}|{'BALANCE':^20}|")
                print(f"|{amount:^20}|{balance:^20}|")
                print(f"{'-' * 43:^43}")
                input("Press enter to continue.")
                os.system("cls")
        except ValueError:
            print("Invalid amount")
            
    else:
        print("Invalid choice.please select 1 or 2.")