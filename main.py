# Python Banking Programme

#User balance
balance = 0

#Show user their balance
def show_balance():
    print(f"Your balance is: £{balance:.2f}")

#Make a deposit
def deposit():
    amount = float(input(f"Enter the amount you will like to deposit: "))
    if amount < 0:
        print("That's not a valid amount")
    else:
        return amount

#Make a withdraw
def withdraw():
    amount = float(input(f"Enter the amount you will like to withdraw: "))
    if amount < 0:
        print("That's not a valid amount")
    else:
        return amount

is_running = True

while is_running:
    print("-----Banking Programme-----")
    print("-----Enter 1. Show balance-----")
    print("-----Enter 2. Deposit balance-----")
    print("-----Enter 3. Withdraw balance-----")
    print("-----Enter 4. To quit the programme-----")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 4:
        break
    elif choice == 1:
        show_balance()
    elif choice == 2:
        balance += deposit()
        print(f"Your updated balance is now: £{balance}")
    elif choice == 3:
        amount = withdraw()
        if amount is not None and amount <= balance:
            balance -= amount
            print(f"You have withdrawn £{amount}. Your new balance is £{balance}")
        else:
            print(f"You do not have enough amount to withdraw")