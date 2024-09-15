from typing import List
from transfer import Transaction
import account

class Customer:
  def __init__(self, name: str, contact_info: str, accounts: List['account.Account']):
    self.__name = name
    self.__contact_info = contact_info
    self.__accounts = accounts
    
  def set_name(self, name):
    self.__name = name
    
  def set_contact_info(self, contact_info):
    self.__contact_info = contact_info
  
  def get_name(self):
    return self.__name
  
  def get_contact_info(self):
    return self.__contact_info
  
  def add_account(self, account: 'account.Account'):
    if account not in self.__accounts:
      self.__accounts.append(account)
    else:
      raise ValueError("Account already added.")
  
  def view_accounts(self):
    print("Accounts:")
    for account in self.__accounts:
      print(f"Account type: {account.get_account_type()}\nAccount Number: {account.get_account_number()}\n"
            f"Balance: {account.get_balance()}")
  
  def view_transaction_history(self):
    Transaction.log_self()