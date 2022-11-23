class bank_account:
    def __init__(self,account_no):
        self.account_no = account_no
        # self.branch_name = "warora"
    def display(self):

        print(f"account number is {self.account_no}\nbranch name is Warora ")

class credit_card(bank_account):
    def __init__(self,account_no):
        super().__init__(account_no)
        # self.account_no = account_no
        print("Card number")

a = credit_card(2382308502385)
a.display()