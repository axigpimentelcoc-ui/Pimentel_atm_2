import datetime

users = {}


def print_receipt(name, transaction_type, amount, balance):
    """Generates and saves a transaction receipt."""
    transaction_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    receipt_text = (
        "\n--- ATM RECEIPT ---\n"
        f"Client: {name}\n"
        f"Date & Time: {transaction_time}\n"
        f"Transaction Type: {transaction_type}\n"
        f"Amount: ₱{amount:.2f}\n"
        f"New Balance: ₱{balance:.2f}\n"
        "--------------------\n"
    )

    print(receipt_text)

    file_name = f"{name.lower().replace(' ', '_')}_receipts.txt"
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(receipt_text)


def create_account():
    print("\n=== CREATE NEW ACCOUNT ===")
    acc_num = input("Enter a new account number: ")
    if acc_num in users:
        print("⚠️ Account number already exists!\n")
        return

    pin = input("Set a 4-digit PIN: ")
    name = input("Enter your name: ")
    users[acc_num] = {"pin": pin, "balance": 0, "name": name}
    print(f"\n✅ Account created successfully for {name}!")
    print(f"Your account number is {acc_num}. Please remember your PIN.\n")


def check_balance(account):
    balance = users[account]['balance']
    name = users[account]['name']
    print(f"\n {name}, your current balance is ₱{balance:.2f}\n")


def deposit(account):
    try:
        amount = float(input("Enter amount to deposit: ₱"))
        if amount <= 0:
            print("⚠️ Invalid amount. Please enter a positive number.\n")
            return
        users[account]['balance'] += amount
        new_balance = users[account]['balance']
        print(
            f"✅ ₱{amount:.2f} deposited successfully! New balance: ₱{new_balance:.2f}\n")
        print_receipt(users[account]['name'], "Deposit", amount, new_balance)
    except ValueError:
        print("⚠️ Invalid input! Please enter a number.\n")


def withdraw(account):
    try:
        amount = float(input("Enter amount to withdraw: ₱"))
        if amount <= 0:
            print("⚠️ Invalid amount. Please enter a positive number.\n")
            return
        if amount > users[account]['balance']:
            print("❌ Insufficient balance!\n")
        else:
            users[account]['balance'] -= amount
            new_balance = users[account]['balance']
            print(
                f"✅ ₱{amount:.2f} withdrawn successfully! New balance: ₱{new_balance:.2f}\n")
            print_receipt(users[account]['name'],
                          "Withdrawal", amount, new_balance)
    except ValueError:
        print("⚠️ Invalid input! Please enter a number.\n")


def change_pin(account):
    old_pin = input("Enter your current PIN: ")
    if old_pin == users[account]['pin']:
        new_pin = input("Enter your new 4-digit PIN: ")
        confirm = input("Confirm your new PIN: ")
        if new_pin == confirm:
            users[account]['pin'] = new_pin
            print("✅ PIN changed successfully!\n")
        else:
            print("⚠️ PINs do not match!\n")
    else:
        print("❌ Incorrect current PIN!\n")


def atm_menu(account):
    """Main ATM menu after login"""
    while True:
        print(f"\n===== ATM MENU ({users[account]['name']}) =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(account)
        elif choice == "2":
            deposit(account)
        elif choice == "3":
            withdraw(account)
        elif choice == "4":
            change_pin(account)
        elif choice == "5":
            print(" Logging out...\n")
            break
        else:
            print("⚠️ Invalid option. Please try again.\n")


def main():
    print("===== WELCOME TO UNIVERSAL ATM =====")

    while True:
        print("\n1. Create New Account")
        print("2. Login to Existing Account")
        print("3. Exit")
        option = input("Choose an option (1-3): ")

        if option == "1":
            create_account()

        elif option == "2":
            acc_num = input("Enter your account number: ")
            if acc_num in users:
                for _ in range(3):
                    pin = input("Enter your PIN: ")
                    if pin == users[acc_num]['pin']:
                        print(f"\n✅ Welcome, {users[acc_num]['name']}!\n")
                        atm_menu(acc_num)
                        break
                    else:
                        print("❌ Incorrect PIN! Try again.")
                else:
                    print("⚠️ Too many failed attempts. Returning to main menu.\n")
            else:
                print("⚠️ Account not found! Please create an account first.\n")

        elif option == "3":
            print(" Thank you for using Universal ATM. Goodbye!\n")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
