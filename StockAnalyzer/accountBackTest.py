class Account:
    def __init__(self):
        self.account = 1000.17
        self.shares = 0

    def buyShares(self, price):
        bid = self.account*0.05
        self.account = self.account - bid
        num_shares = bid/price
        self.shares = self.shares + num_shares
        print("\nBought: "+str(num_shares)+" shares\nat "+str(price)+" per share+\n"
                                                                     "Account Balance: "+str(self.account))

    def sellShares(self, price):
        if self.shares > 0:
            ask = self.shares * price
            self.account = self.account + ask
            print("\nSold: "+str(self.shares)+" shares\nat "+str(price)+" per share")
            print("Account Balance: "+str(self.account))
            self.shares = 0
