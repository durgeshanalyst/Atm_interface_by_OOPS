class Atm:
    def __init__(self): #constructor ad no need to call this function ad his is the super power.
        self.pin=''
        self.balance=0
        self.menu()


    def menu(self):
        user_input = input(""" 
        Hi , How may I help You?
        : press 1 for create pin
        : press 2 for change pin.
        : press 3 for checking the balance.
        : press 4 for withdraw.
        """)
        if user_input == '1':
            print('Lets create pin')
            self.create_pin()
            print('Your pin has been created')
            self.balance=input('Enter your balance pleae !')
            print('Thank you')
            self.menu()
        elif user_input == '2':
            print('Lets change your pin')
            self.change_pin()
            self.menu()
        elif user_input =='3':
            print('Okay')
            self.check_balance()
            self.menu()
        elif user_input == '4':
            self.withdraw()
            self.menu()
        else:
            print('Thank you for visitig')
            self.menu()
    def create_pin(self):
        self.pin=input('Enter your pin : ')
    def change_pin(self):
        update_pin=input('Enter your old pin : ')
        if update_pin == self.pin:
            print('Great Give me a moment !')
            self.pin=input('Enter your new pin : ')
            print('Your pin has successfully updated !!')
        else:
            print("sorry I can't help !")
        self.menu()
    def check_balance(self):
        check_pin=input('Enter your Atm Pin : ')
        if check_pin==self.pin:
            print("Your balance is " + self.balance)
        else:
            print('Wrong pin try again')
            
    def withdraw(self):
        withraw_pin=input('Enter your pin : ')
        if withraw_pin == self.pin:
            ask_money=input('Enter how much you want')
            if int(self.balance) >= int(ask_money):
                print('Hey buddy check your balance in account')
            else:
                print("Sorry you don't have sufficient money")
        else:
            print('Dusre ka Atm use kar rha hai kya bhai !')
        
obj=Atm()