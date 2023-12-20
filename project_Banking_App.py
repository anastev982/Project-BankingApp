class Bank:
    
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
    
  def deposit(self, amount):
    self.balance += amount

  def withdrow(self, amount):
    if self.balance >= amount:
      self.balance -= amount
      
    else:
      self.balance < amount
      print("You dont have enough money on your account")
      
def start():
    account_number = int(input("Please enter your account number"))
    initial_balance = int(input("Enter your balance: "))
    bank = Bank(account_number, initial_balance)
    
    while True:
      print("Deposit")
      print("Withdrow")
      print("Balance")
      print("Exit")
    
      selection = input("Please select one of the options:")
    
      if selection == "Deposit":
        amount = int(input("Please enter the amount you will deposit: "))
        bank.deposit(amount)
        
        if amount in range(10, 100000):
          print("Money have been placed on your account")
        else:
          print("Error")  
      
          
      elif selection == "Withdrow":
        amount = int(input("What is amount to withdrow?"))
        bank.withdrow(amount)
        
        if amount in range(10, 1000):
          print("You can take your money")
        else:
          print("You do not have enoph money on your account")  
        
      
      elif selection == "Balance":
        print(f"Your balance is: {bank.balance}")
        
      
      elif selection == "Exit":
        break
    
start()         