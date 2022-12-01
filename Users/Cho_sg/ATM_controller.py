class Bank:
    def __init__(self):
        self.bank_user_data = {}
        
    def add_user(self, card_num, pin_num, account, cash):
        self.bank_user_data[card_num] = {"pin":pin_num, "account":{account:cash}}
        
    def check_pin(self, card_num, pin_num):
        if card_num in self.bank_user_data and self.bank_user_data[card_num]["pin"] == pin_num:
            return self.bank_user_data[card_num]["account"]
        else:
            return None
    
    def update_account(self, card_num, account, amt):
        if self.bank_user_data[card_num]["account"][account] in self.bank_user_data[card_num]["account"]:
            self.bank_user_data[card_num]["account"][account] = amt
            return True
        else:
            return False

class Controller:
    def __init__(self, bank, cash):
        self.Bank = bank
        self.accounts = None
        self.total_cash = cash
    
    def check_user(self, card_num, pin):
        self.accounts = self.Bank.check_pin(card_num, pin)
        if self.accounts is None:
            print("incorrect")
            return 0
        else:
            print("correct")
            return 1
        
    
    def actions_account(self, card_num, account, action, cash = 0):
        if action == "See Balance":
            print("card_num:{}  account:{}  Balance:{}".format(card_num, account, self.accounts[account]))
            return self.accounts[account]
        elif action == "Withdraw":
            if self.accounts[account] >= cash and self.total_cash >= cash:
                    new_cash = self.accounts[account] - cash
                    self.accounts[account] = new_cash
                    self.total_cash -= cash
                    self.Bank.update_account(card_num, account, new_cash)
                    return 1
            else:
                if self.total_cash < cash:
                    print("No enough money in ATM")
                    return 0
                elif self.accounts[account] < cash:
                    print("No enough money in your account")
                return 0
        elif action == "Deposit":
            new_cash = self.accounts[account] + cash
            self.total_cash += cash
            self.accounts[account] = new_cash
            self.Bank.update_account(card_num, account, new_cash)
            return 1
        else:
            return 0
                
    
if __name__=="__main__":
    bank = Bank()
    atm = Controller(bank,0)
    atm.check_user(123,0)
    
    test_bank = Bank()
    test_atm = Controller(test_bank, 10000)
    test_bank.add_user(123456, 123, "red", 1000)
    test_bank.add_user(9876, 567, "blue", 1000)
    test_atm.check_user(123456, 123)
    test_atm.actions_account(123456, "red", "Deposit", 1000)
    test_atm.actions_account(123456, "red", "See Balance")
    test_atm.actions_account(123456, "red", "Withdraw", 1000)
    test_atm.actions_account(123456, "red", "See Balance")
    test_atm.check_user(9876, 5678)
    test_atm.check_user(9876, 567)
    test_atm.actions_account(9876, "blue", "See Balance")
    test_atm.actions_account(9876, "blue", "Withdraw", 500)
    test_atm.actions_account(9876, "blue", "See Balance")
    test_atm.actions_account(9876, "blue", "Withdraw", 500)
    test_atm.actions_account(9876, "blue", "See Balance")
    test_atm.actions_account(9876, "blue", "Withdraw", 500)
