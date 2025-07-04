balance = 10000
attempts = 0 
success = True 

while success: 
    pin = input("Enter your PIN: ") 
     
    if pin == "4567": 
        print("Correct Pin Entered!") 
        print(f"You have {balance} baht in your account")
        break

    else: 
        print("Incorrect PIN!! Try Again.") 
        attempts += 1 
        print(f"You try {attempts} time ")
        if attempts == 3: 
            success = False 
            print("Your account is locked. Please contact bank.")
            exit()

while True:

    choice = input("Press 1 to deposit or 2 to withdraw:")  
    if choice == "1":
        try:
            amount = int(input("Enter an amount to deposit:"))
            if amount < 0:
                print("Deposit amount must be positive.")
            else:
                balance += amount
                print(f"|     DEPOSIT FUND    |  BALANCE   |\n|        {amount}         |   {balance}    |")
                input("Press enter to contiune.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "2":
        try:
            amount = int(input("Enter an amount to withdraw:"))
            if amount < 0:
                print("Withdrawal amount must be positive.")
            elif amount > balance:
                print("Your credit is not enough")
            else:
                balance -= amount
                print(f"|     WITHDRAW FUND   | BALANCE   |\n|       {amount}          |   {balance}    |")
                input("Press enter to continue.")
        except ValueError:
            print("Invalid amount")
            
    else:
        print("Invalid choice.please select 1 or 2.")


                


        