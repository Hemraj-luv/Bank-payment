# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 23:36:43 2019

@author: Hemraj
"""
def payment():
    class Bill:
        def __init__(self,items,price):
            self.items=items
            self.price=price
            self.total=0
            for i in self.price:
                self.total+=i
        def display(self):
            print('\n  ITEM\t\t\t PRICE')
            for i in range(len(self.items)):
                print(self.items[i],'\t',self.price[i])
            print('*******************************')
            print('total= ',self.total)
            
    class Cash_payment(Bill):
        def __init__(self,items,price,deno,value):
            Bill.__init__(self,items,price)
            self.deno=deno
            self.value=value
        def show_cashpayment_details(self):
            Bill.display(self)
            for i in range(len(deno)):
               print(deno[i],'*',value[i],'=',deno[i]*value[i])
    class Cheque_payment(Bill):
        def __init__(self,items,price,cno,name):
            Bill.__init__(self,items,price)
            self.cno=cno
            self.name=name
        def show_check_payment_details(self):
            Bill.display(self)
            print('CHEQUE NUMBER ',self.cno)
            print('BANK NAME ',self.name)
    items = ['External Hard Disk','RAM','printer','Pen Drive']
    price=[5000,2000,6000,800]
    option= int(input('would u like to pay by cheque or by Cash :\n\t1.cheque\n\tplease enter :'))
    if option ==1:
        name=input('enter the name of your Bank:')
        cno=input('enter the cheque number :')
        Cheque=Cheque_payment(items,price,cno,name)
        Cheque.show_check_payment_details()
    elif option ==2:
        deno=[10,20,50,100,500,2000]
        value=[1,1,120,40,5,6]
        cp=Cash_payment(items,price,deno,value)
        cp.show_cashpayment_details()
    else:
        name=input('enter the name of your Bank:')
        cno=input('enter the cheque number :')
        a=Cheque_payment(items,price,cno,name)
        a.show_check_payment_details()
payment()