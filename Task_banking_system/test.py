from transfer import Transaction
import customer
import datetime
from account import SavingsAccount, CheckingAccount, JointAccount

acc1 = CheckingAccount(101, 1000.0)
acc2 = CheckingAccount(102, 5000.0)
acc1.tranfer(acc2, 1500.0)
acc1.show_balance()
acc2.show_balance()
new_customer = customer.Customer('Bob','bob#gmail.com',[acc1, acc2])
print()
new_customer.view_accounts()
acc1.deposit(10000.0)
acc2.show_balance()
save_account = SavingsAccount(111,10000.0,'Savings',15)
new_customer.add_account(save_account)
save_account.confirm_interest()
new_customer.view_accounts()
tr = Transaction(acc1,acc2,1222,'gift',datetime.datetime.today())
tr.log_self()
acc2.show_balance()
new_customer._Customer__accounts[0].show_balance()
