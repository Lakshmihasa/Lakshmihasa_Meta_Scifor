class Bank:
    def __init__(self, account_number, pin, initial_balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = initial_balance

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount, entered_pin):
        if not self.check_pin(entered_pin):
            print("Invalid PIN.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def show_balance(self):
        print(f"Current balance: {self.balance}")

def main():
    account_number = input("Enter account number: ")
    pin = input("Set PIN: ")
    initial_balance = float(input("Enter initial balance: "))
    
    account = Bank(account_number, pin, initial_balance)
    
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            entered_pin = input("Enter PIN: ")
            account.withdraw(amount, entered_pin)
        
        elif choice == '3':
            account.show_balance()
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main