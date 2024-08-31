#define the menu of restaurant
menu={
    "pizza": 200,
    "burger": 50,
    "fries": 20,
    "soda": 10,
    "pasta":50
}
#greet
print("welcom to home resturant")
print("pizza: Rs 40\n burger: Rs 50 \n fries: Rs 20 \n  soda: Rs 10 \n pasta: Rs 50 ") 
order_total=0
#ask for order
item1=input("enter the name of item you want to order= ")
if item1 in menu :
    order_total+=menu[item1]
    print("your item {item1} has been added to your order ")
else:
    print(f"ordered item {item1} is not avaiable yet!" )

another_order=input ("do you want to add another item? (yes/no)")
if another_order == "yes" :
    item2=input("enter the name of second item=")
    if item2 in menu:
        order_total=order_total+menu[item2]
        print(f"item {item2} has been added to order")
    else:
        print(f"ordered item {item2} is not available yet!")
print(f"The total amount of item is {order_total}")