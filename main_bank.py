import sys
from bank_account import BankAccount
from bank_account import Insufficient_error
def main():
    account = BankAccount(100)
    if len(sys.argv) < 2:
        print("usage: python main-0.py <command>: <amount>")
        print("commands: deposit, withdraw, display")
        sys.exit(1)
    command, *params = sys.argv[1].split(":")
    amount = float(params[0]) if params else None
    if command == "deposit" and amount is not None:
        account.deposit(amount)
    elif command == "withdraw" and amount is not None:
        try:
            if amount > account.show_balance(): 
                raise Insufficient_error(amount) 
            account.withdraw(amount)
        except Insufficient_error as e:
            print(f"Sorry! You don't have up to {e.amount}") 
    elif command == "display" and amount is not None:
        account.display_balance()
if __name__ == "__main__":
    main()
    
    