import abc
import account
import datetime
from typing import Optional

class TransactionManager(abc.ABC):
  @abc.abstractmethod
  def log_transaction(self, transaction_type: str, amount: float):
    ...
  
  @abc.abstractmethod
  def show_transaction_history(self):
    ...

class Transaction:
  def __init__(self, from_account: 'account.Account',
               to_account: Optional['account.Account'],
               amount: float,
               transaction_type: str,
               timestamp: datetime
  ):
    self.__from_account = from_account
    self.__to_account = to_account
    self.__amount = amount
    self.__from_account.tranfer(self.__to_account, amount)
    self.__transaction_type = transaction_type
    self.__timestamp = timestamp
  
  def log_self(self):
    if self.__to_account:
      print(f"Time: {self.__timestamp}:\nTranfer type: {self.__transaction_type}\nAmount: ${self.__amount}\n"
            f"From account {self.__from_account.get_account_number()} to account {self.__to_account.get_account_number()}")
    else:
      print(f"{self.__timestamp}: {self.__transaction_type} of {self.__amount}"
            f"from account {self.__from_account}.")
  