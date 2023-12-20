class Bank:
    
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
    
  def deposit(self, amount):
    self.balance += amount

  def withdrawal(self, amount):
    if self.balance >= amount:
      self.balance -= amount
      
    else:
      print("You dont have enough money on your account")
       
def start():

    account_number = int(input("Please enter your account number"))
    initial_balance = int(input("Enter your balance: "))
    
    bank = Bank(account_number, initial_balance)
    
    while True:
      print("1.Deposit")
      print("2.Withdrawal")
      print("3.Balance")
      print("4.Exit")
    
      selection = input("Please select one of the options:")
    
      if selection == "1":
           amount = int(input("Please enter the amount you will deposit: "))
           bank.deposit(amount)
           
           if amount in range(10, 100000):
            print("Money have been placed on your account")   
           else:
            print("Error!Please try again")
            
            continue
        
      elif selection == "2":
          amount = int(input("What is amount you would like to withdraw?"))
          bank.withdrawal(amount)
        
          if amount in range(10, 1000):
              print("You can take your money")
          else:
              print("You do not have enough money on your account")  
              continue
            
      elif selection == "3":
       print(f"Your balance is: {bank.balance}")
      
      elif selection == "4":
         print("Thank you for using our bank") 
         
         break
    
start()         