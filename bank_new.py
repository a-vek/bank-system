import time
bank_dict = {}

class Bank:
    """This class for Creating Bank and store users details"""
    def __init__(self, name):
        self.bank_name = name
        self.users = {}

    def __repr__(self):
        return self.bank_name

    def add_user(self, username, pin):
        if self.users.get(username):
            raise UserExistsError
        user = User(username, pin)
        self.users[user.username] = user

    def get_user(self, username, pin):
        user = self.users.get(username)
        if not user:
            raise UserNotExistsError
        if user.pin != pin:
            raise UserPinNotMatchError
        return user

    def user_info(self,username,pin):
        user = self.get_user(username,pin)
        print(f"User's name is {user.username} and total amount in bank account is {user.total_amount}")

    def get_user_transaction(self, username, pin):
        user = self.get_user(username, pin)
        if not user.tr_history:
            print("There is no transaction history yet!!")
        else:
            while len(user.tr_history) > 5:
                user.tr_history.pop()
        print("Transactions: ", user.tr_history)
    
    def deposit(self,username,pin):
        user = self.get_user(username,pin)
        amount = int(input("Enter amount to be deposited : "))
        t_type = "Credit"
        before_balance = user.total_amount
        if amount > 0:
            user.total_amount += amount
            exact_time = time.asctime(time.localtime(time.time()))
            t1 = Transactions(amount,t_type,before_balance,exact_time)
            user.tr_history.insert(0, (t1.t_type, t1.amount, t1.exact_time))
            print("\n----------------------------------------------------------\n")
            print("Current balance in your account is: ", user.total_amount)
            print("\n----------------------------------------------------------\n")
        else:
            print("Invalid amount transaction aborted")

    def withdraw(self,username,pin):
        user = self.get_user(username,pin)
        amount = int(input("Enter amount you want to withdraw : "))
        t_type = "Debit"
        before_balance = user.total_amount
        if amount > 0 and amount <= user.total_amount:
            user.total_amount -= amount
            exact_time = time.asctime(time.localtime(time.time()))
            t2 = Transactions(amount,t_type,before_balance,exact_time)
            user.tr_history.insert(0, (t2.t_type, t2.amount, t2.exact_time))
            print("\n----------------------------------------------------------\n")
            print("Current balance in your account is: ", user.total_amount)
        else:
            print("Invalid amount transaction aborted")

class User:
    """This class creates new user"""
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin
        self.total_amount = 0
        self.tr_history = []

    def __repr__(self):
        return self.username

class Transactions:
    """This class created for make transactions"""
    def __init__(self, amount, t_type, before_bal,exact_time):
        self.amount = amount
        self.t_type = t_type
        self.before_bal = before_bal
        self.exact_time = exact_time

    def __repr__(self):
        return self.before_bal

if __name__ == "__main__":

    def new_bank():
        bank_name = str(input("Enter a New Bank Name: ")).title()

        if bank_name not in bank_dict.keys():
            bank = Bank(bank_name)
            bank_dict[bank_name] = bank
        else:
            print("Bank has been already added!!")
        print(bank_dict)
        
                
    def create_customer():
        bank_name = str(input("Enter a Bank Name: ")).title()

        if bank_name not in bank_dict.keys():
            new_bank()
        else:
            # while True:
                # user_input = input('''\n[Press 1] for Adding a new customer:  
                # \n[Press 2] Exit : ''')
                # if user_input == '1':
                username = str(input("Enter your good name: ")).title()
                while True:
                    try: 
                        pin = str(input("Please enter four digits: "))
                        int(pin)
                        if len(pin) > 4:
                            print("Incorrect")
                        elif len(pin) < 4:
                            print("Incorrect")
                        else:
                            break
                    except ValueError:  
                        print("Please input only numerical values ")
                bank_dict[bank_name].add_user(username=username,pin=pin)
                print(bank_dict[bank_name].users)
                # break
                    # bank_dict[bank_name] = Bank(bank_name).users
                # elif user_input == '2':
                #     break
    
    def login_customer():
        bank_name = str(input("Enter bank name: ")).title()
        username = str(input("Enter name : ")).title()
        pin = input("Enter pin : ")

        if bank_name in bank_dict:
            bank_obj = bank_dict[bank_name]
            # for key in user_dict:
            if username == bank_obj.get_user(username,pin).username and pin == bank_obj.get_user(username,pin).pin:
                    print("You are allowed to do transaction!!!")
                    while True:
                        after_login_input = input('''\n[Press 1] for Deposit 
                        \n[Press 2] for Withdrawl 
                        \n[Press 3] for Transaction History  
                        \n[Press 4] for General Details 
                        \n[Press 5] for Permanatly Close Account
                        \n[Press 6] for Logged Out \n''')
                        if after_login_input == '1':
                            bank_obj.deposit(username,pin)
                        elif after_login_input == '2':
                            bank_obj.withdraw(username,pin)
                        elif after_login_input == '3':
                            bank_obj.get_user_transaction(username, pin)
                        elif after_login_input == '4':
                            bank_obj.user_info(username,pin)
                        elif after_login_input == '5':
                            del bank_obj.users[username]
                            break
                        elif after_login_input == '6':
                            break
        else:
            print("Please provide true details!!")
        
    def bank_customer_list():
        bank_name = str(input("Enter existing bank : ")).title()
        if bank_name in bank_dict.keys():
            print(bank_dict[bank_name].users)
        else:
            print("This bank name is not exist!!")

    while True:
        user_main_input = input('''\n[Press 1] for Adding New Bank
        \n[Press 2] for Bank Customers
            \n[Press 3] for Creating New Customer
            \n[Press 4] for Loggin Existing Customer 
            \n[Press 5] for Exit \n''')
        if user_main_input == '1':
            new_bank()
        elif user_main_input == '2':
            bank_customer_list()
        elif user_main_input == '3':
            create_customer()
        elif user_main_input == '4':
            login_customer()
        elif user_main_input == '5':
            print('Exited!!')
            break
        else:
            print("Invalid Input!!!!")