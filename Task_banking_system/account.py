import abc
import transfer

class Account(abc.ABC):
  def __init__(self, account_number: int, balance: float, account_type: str) -> None:
    self.set_account_number(account_number)
    self.set_balance(balance)
    self.set_account_type(account_type)
    self._transaction_history = []
  
                              # Set and Get  
  def set_account_number(self, account_number):
    if not isinstance(account_number, int):
      raise ValueError("Account number must be whole number.")
    if account_number < 0:
      raise ValueError("Account number must be positiv number.")
    self._account_number = account_number
  
  def set_balance(self, balance):
    if balance < 0:
      raise ValueError("Balance can't be negativ.")
    self._balance = balance
  
  def set_account_type(self, account_type):
    if not isinstance(account_type, str):
      raise ValueError("Account type must be string.")
    self._account_type = account_type
  
  def get_account_number(self):
    return self._account_number
  
  def get_balance(self):
    return self._balance
  
  def get_accounttype(self):
    return self._account_type
  
  def log_transaction(self, transaction_type: str, amount: float):
    transaction = f"{transaction_type} of ${amount} (Balance: {self._balance}.)"
    self._transaction_history.append(transaction)
    print(f"Transaction: {transaction}.")
  
  def show_transaction_history(self):
    if self._transaction_history:
      print("Transaction History")
      for transaction in self._transaction_history:
        print(transaction)
    else:
      print("Trnasaction history is empty")

                            # Abstract Methods
  @abc.abstractmethod
  def deposit(self, amount: float):
    ...
  
  @abc.abstractmethod
  def withdraw(self, amount: float):
    ...
  
  @abc.abstractmethod
  def tranfer(self, destination: 'Account', amount: float):
    ...
  
  @abc.abstractmethod
  def show_balance(self):
    ...
  
  @abc.abstractmethod
  def get_account_type(self):
    ...
#---------------------------------------------------------------------------------------------
class CheckingAccount(Account):
  def __init__(self, account_number: int, balance: float, overdraft_limit: float = 500.0):
    super().__init__(account_number, balance, "Checking")
    self._overdraft_limit = overdraft_limit
  
  def deposit(self, amount: float):
    if amount <= 0:
      raise ValueError("Only positive number.")
    self._balance += amount
  
  def withdraw(self, amount: float):
    if amount <= 0:
      raise ValueError("Only positive number.")
    if self._balance - amount < -self._overdraft_limit:
      raise ValueError("Exceeds overdraft limit.")
    self._balance -= amount
    self.log_transaction("Withdraw", amount)
      
  def tranfer(self, destination: Account, amount: float):
    if amount <= 0:
      raise ValueError("Only positive number.")
    if self._balance - amount < -self._overdraft_limit:
      raise ValueError("Exceeds overdraft limit.")

    self.withdraw(amount)
    destination.deposit(amount)
    self.log_transaction('Transfer', amount)

  def show_balance(self):
    print(f"Account {self._account_number}\nBalance: {self._balance}")
  
  def get_account_type(self):
    return self._account_type

#----------------------------------------------------------------------------------------
class SavingsAccount(Account):
  def __init__(self, account_number: int, balance: float, account_type: str, interest_rate: float=0.0):
    super().__init__(account_number, balance, "Savings")
    self.set_interest_rate(interest_rate)
  
  def set_interest_rate(self, interest_rate: float):
      if interest_rate < 0:
        raise ValueError("Interest rate must be positiv number.")
      self._interest_rate = interest_rate
  
  def get_interest_rate(self):
    return self._interest_rate
  
  def confirm_interest(self):
    interest = self._balance * (self._interest_rate / 100)
    self._balance += interest
    
  def deposit(self, amount: float):
    if amount <= 0:
      raise ValueError("Only positive number.")
    self._balance += amount
    self.log_transaction('Deposit', amount)
  
  def withdraw(self, amount: float):
    if amount <= 0:
      raise ValueError("Only positive number.")
    if self._balance - amount < -self._overdraft_limit:
      raise ValueError("Exceeds overdraft limit.")
    self._balance -= amount
    self.log_transaction('Withdraw', amount)
      
  def tranfer(self, destination: Account, amount: float):
    if amount <= 0:
      raise ValueError("Only positive number.")
    if self._balance - amount < -self._overdraft_limit:
      raise ValueError("Exceeds overdraft limit.")

    self.withdraw(amount)
    destination.deposit(amount)
    self.log_transaction('Transfer', amount)
  
  def show_balance(self):
    print(f"Account {self._account_number}\nBalance: {self._balance}")
  
  def get_account_type(self):
    return self._account_type

#---------------------------------------------------------------------------------
class JointAccount(Account):
  def __init__(self, account_number: int, balance: float, joint_owners: list[str]):
    super().__init__(account_number, balance, 'Joint')
    self._joint_owners = joint_owners

  def add_owner(self, customer_name: str):
    if isinstance(customer_name, str):
      if customer_name in self.__joint_owners:
        raise ValueError("Customer is already an owner.")
      self._joint_owners.append(customer_name)
      print(f"Customer: {customer_name} added as a joint owner to account {self._account_number}.")
    else:
      raise ValueError("Customer name can't contain any symbols or numbers.")
  
  def get_owner(self):
    return self._joint_owners  
  def deposit(self, amount: float):
    if amount <= 0:
      raise ValueError("Only positive number.")
    self._balance += amount
  
  def withdraw(self, amount: float):
    if amount <= 0:
      raise ValueError("Only positive number.")
    if self._balance - amount < -self._overdraft_limit:
      raise ValueError("Exceeds overdraft limit.")
    self._balance -= amount
      
  def tranfer(self, destination: Account, amount: float):
    if amount <= 0:
      raise ValueError("Only positive number.")
    if self._balance - amount < -self._overdraft_limit:
      raise ValueError("Exceeds overdraft limit.")

    self.withdraw(amount)
    destination.deposit(amount)
  
  def show_balance(self):
    print(f"Account {self._account_number}\nBalance: {self._balance}")
  
  def get_account_type(self):
    return self._account_type