#Menu based Bank Account Program using Classes

class BankAccount:
    number_of_accounts = 0  # class variable

    def __init__(self, account_no, holder_name, holder_address, account_type, balance=0):
        self.account_no = account_no
        self.holder_name = holder_name
        self.holder_address = holder_address
        self.account_type = account_type
        self.balance = balance
        BankAccount.number_of_accounts += 1

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance = {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance = {self.balance}")
        else:
            print("Insufficient balance!")

    def get_details(self):
        return {
            "Account No": self.account_no,
            "Name": self.holder_name,
            "Address": self.holder_address,
            "Type": self.account_type,
            "Balance": self.balance
        }


# Store accounts in a dictionary
accounts = {}

def menu():
    while True:
        print("\n--- Bank Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show Account Details")
        print("5. Show Total Accounts")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            acc_no = input("Enter Account Number: ")
            name = input("Enter Account Holder Name: ")
            address = input("Enter Address: ")
            acc_type = input("Enter Account Type (Savings/Current): ")
            balance = float(input("Enter Initial Balance: "))
            accounts[acc_no] = BankAccount(acc_no, name, address, acc_type, balance)
            print("Account created successfully!")

        elif choice == "2":
            acc_no = input("Enter Account Number: ")
            if acc_no in accounts:
                amt = float(input("Enter amount to deposit: "))
                accounts[acc_no].deposit(amt)
            else:
                print("Account not found!")

        elif choice == "3":
            acc_no = input("Enter Account Number: ")
            if acc_no in accounts:
                amt = float(input("Enter amount to withdraw: "))
                accounts[acc_no].withdraw(amt)
            else:
                print("Account not found!")

        elif choice == "4":
            acc_no = input("Enter Account Number: ")
            if acc_no in accounts:
                details = accounts[acc_no].get_details()
                for k, v in details.items():
                    print(f"{k}: {v}")
            else:
                print("Account not found!")

        elif choice == "5":
            print("Total number of accounts:", BankAccount.number_of_accounts)

        elif choice == "6":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice, try again!")


menu()
