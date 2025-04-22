class bank():
    
    def _init_(self,uid,pin):
        self.uid=uid
        self.pin=pin
        self.balence=0
        self.his={}
        self.i=1
        self.j=1 
        
    def deposit(self,amount):
        self.balence=self.balence+amount
        self.his["deposited {}".format(self.j)]=amount
        #print(self.balence)
    def withdrow(self,amount,p):
       
        if p==self.pin:
            if self.balence<amount:
                print("youre available balence is",self.balence,"\nis less than",amount)
            else:
                self.balence=self.balence-amount
                print("withdrowed amount",amount,"\nremaining amount is",self.balence)
                
                self.his["withdrowed {}".format(self.i)]=amount
                self.i=self.i+1
        else:print("enter currect pin")
                
    def histery(self):
        print(self.his)
    def check(self,pin):
        if pin==self.pin:
            print(self.balence)
        else:print("enter currect pin")
   


k=(input("ent uid : "))
I=int(input("passwerd : "))
b=bank()
while True:
    k=int(input("select : \n1) histery \n2) withdrowed\n3) deposit\n 4) check balence\n0-to QUIT  \nENTER CHOICE : "))
    if k>4 or k<0:
        print("enter valid input(1,2,3)")
    elif k==1:
        b.histery()
    elif k==2:
        amount=int(input("enter amout to be withdrawed : "))
        pin=int(input("enter pin"))
        b.withdrow(amount,pin)
    elif k==3:
        amount=int(input("enter amount to be deposited : "))
        b.deposit(amount)
    elif k==4:
        pin=int(input("enter pin"))
        b.check(pin)
    elif k==0:
        break