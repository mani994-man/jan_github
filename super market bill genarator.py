import datetime

name=input("enter your name:")
#list of items
lists='''
Rice RS 20/kg
sugar RS 30/kg
salt RS 10/kg
oil RS 100/ltr
milk RS 50/ltr
panner RS 110/kg
boost RS 90/each
maggie RS 50/kg
closeup RS 20/each

'''
price=0
price_list=[]
total_price=0
Final_final_price=0
i_list=[]
q_list=[]
p_list=[]

#rates for items
items={'Rice':20,
       'sugar':30,
       'salt':10,
       'oil':100,
       'milk':50,
       'panner':110,
       'boost':90,
       'maggie':50,
       'closeup':20}
option=int(input("do you want to see the list of items? press:1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy items press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your item:")
        quantity=int(input("enter the quantity:"))
        if item in items.keys():
            price=quantity*(items[item]) 
            price_list.append((item,quantity,items,price))
            total_price+=price
            i_list.append(item)
            q_list.append(quantity)
            p_list.append(price)
            gst=(total_price*5)/100
            final_amount=gst+total_price
        else:
            print("item not available")
    else:
        print("invalid input")
    inp=input("do you want to continue shopping? press 1 for yes or 2 for no:")
    if inp=='2':
        if final_amount!=0:
            print(25*"=","mani supermarket",25*"=")
            print(25*" ","parajapadu")
            print("name:",name,30*" ","date:",datetime.datetime.now())
            print(75*"-")
            print("sno",12*" ","items",5*" ","quantity",5*" ","price")
            for i in range(len(price_list)):
                 print(i,8*' ',5*" ",i_list[i],8*' ',q_list[i],3*' ',8*" ",p_list[i])
            print(75*"-")
            print(50*" ","total_amount:","Rs",total_price)
            print("gst_amount",50*" ","RS",gst)
            print(50*" ","final_amount:","Rs",final_amount)
            print(75*"-")
            print(20*" ","thank you for shopping")
            print(75*"-")
        break
             
                 
            
            
         
            
        
    




