import logging
import sys

logging.basicConfig(filename='atm.log', level=logging.INFO,
                    format='%(asctime)s %(message)s')


class ATM:
    def __init__(self):
        self.balance = 0
        self.tax_threshold = 5000000

    def deposit(self, amount):
        if amount % 50 != 0:
            logging.error("Deposit amount should be a multiple of 50")
            return
        self.balance += amount
        logging.info(f"Deposited {amount} u.e. Current balance: "
                     f"{self.balance}")
        self._apply_tax()

    def withdraw(self, amount):
        if amount % 50 != 0:
            logging.error("Withdrawal amount should be a multiple of 50")
            return
        if amount > self.balance:
            logging.error("Insufficient funds")
            return
        fee = amount * 0.015
        if fee < 30:
            fee = 30
        elif fee > 600:
            fee = 600
        self.balance -= (amount + fee)
        logging.info(f"Withdrew {amount} u.e. Fee: {fee} u.e. "
                     f"Current balance: {self.balance}")
        self._apply_tax()

    def exit(self):
        sys.exit()

    def _apply_tax(self):
        if self.balance > self.tax_threshold:
            tax = self.balance * 0.1
            self.balance -= tax
            logging.info(f"Tax for wealth exceeding 5 mln: {tax} u.e. "
                         f"Current balance: {self.balance}")


def main():
    atm = ATM()
    while True:
        action = input("Enter action (deposit, withdraw, exit): ")
        if action == "deposit":
            amount = int(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif action == "withdraw":
            amount = int(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif action == "exit":
            atm.exit()
        else:
            logging.error("Invalid action")


if __name__ == "__main__":
    main()
