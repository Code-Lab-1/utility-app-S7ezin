#	A menu of drinks and snacks
menu = [
    { 
    'product' : 'Water',
    'price' : 1,
     },

      { 
    'product' : 'Tea',
    'price' : 1,
     },

      { 
    'product' : 'Coffee',
    'price' : 2,
     },

      { 
    'product' : 'Smoothies',
    'price' : 10,
     },

      { 
    'product' : 'Cola',
    'price' : 3,
     },

      { 
    'product' : 'Sandwich',
    'price' : 3,
     },

      { 
    'product' : 'Croissant',
    'price' : 2,
     },
 
      { 
    'product' : 'Potato chips',
    'price' : 2,
     },

     
      { 
    'product' : 'Pizza',
    'price' : 4,
     },

     
      { 
    'product' : 'Burger',
    'price' : 5,
     },

          { 
    'product' : 'Iced Coffee',
    'price' : 3,
     },   

      { 
    'product' : 'Popcorn ',
    'price' : 5,
     },   ]

#user can choose anything from the given menu.
def menu():
  print("WELCOME")
  print("\nMENU")
  print("\nProduct      Price        Code\n")
  print("Water        1.00 dhs       1")
  print("Tea          1.00 dhs       2")
  print("Coffee       2.00 dhs       3")
  print("Smoothies    10.00 dhs      4")
  print("Cola         3.00 dhs       5")
  print("Sandwich     3.00 dhs       6")
  print("Croissant    2.00 dhs       7")
  print("Potato chips 2.00 dhs       8")
  print("Pizza        4.00 dhs       9")
  print("Burger       5.00 dhs       10")
  print("Iced Coffee  3.00 dhs       11")
  print("Popcorn      5.00 dhs       12")

# ask the user to type the code from the menu to get their item
  x=float(input("\nTYPE YOUR CODE"))

  if x==1:
    A=1
# this shows what item you have selected
    print("\nYou have selected Water")
# it tells the users the price of their selected product
    print("insert amount 1 dhs")
# user needs to enter their amount
    inp=float(input("\nENTER YOUR AMOUNT"))
    if inp >= A:
      print("\nPAYMENT COMPLETED")
      print("\nCash = ",inp)
# "change" shows the balance amount returned by the machine
      change=inp-A
      print("Change = :",change)
      print("Please recieve your balance amount")
# if the user enters lesser amount it asks for balance amount 
    elif inp < A:
      print("insufficient Funds")
      return menu()
    else:
      print("Error")
      return menu()
# ask the user if they would like to have anything else
    inp=input("would you like to have anything else")
# if the user opted yes
    if inp=="yes":
       return menu()
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
# if the user opted no      
    else:
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
# same code used for above output
  elif x==2:
    B=1
    print("\nYou have selected Tea")
    print("\ninsert amount 1 dhs")
    inp=float(input("ENTER YOUR AMOUNT"))
    if inp >= B:
      print("\nPAYMENT COMPLETED")
      print("\nyou have entered",inp)
      change=inp-1
      print("please recieve your Balance:",change)
    elif inp < B:
      print("insufficient Funds")
      return menu()
    else:
      print("Error")
      return menu()
    inp=input("would you like to have anything else")
    if inp=="yes":
       return menu()
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
      
    else:
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")

  elif x==3:
    C=2
    print("\nYou have selected Coffee")
    print("\ninsert amount 2 dhs")
    inp=float(input("ENTER YOUR AMOUNT"))
    if inp >= C:
      print("\nPAYMENT COMPLETED")
      print("\nyou have entered",inp)
      change=inp-C
      print("please recieve your Balance:",change)
    elif inp < C:
      print("insufficient Funds")
      return menu()
    else:
      print("Error")
      return menu()
    inp=input("would you like to have anything else")
    if inp=="yes":
       return menu()
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
      
    else:
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")

  elif x==4:
    D=10
    print("\nYou have selected Smoothies")
    print("\ninsert amount 10 dhs")
    inp=float(input("ENTER YOUR AMOUNT"))
    if inp >= D:
      print("\nPAYMENT COMPLETED")
      print("\nyou have entered",inp)
      change=inp-D
      print("please recieve your Balance:",change)
    elif inp < D:
      print("insufficient Funds")
      return menu()
    else:
      print("Error")
      return menu()
    inp=input("would you like to have anything else")
    if inp=="yes":
       return menu()
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
      
    else:
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
  
  elif x==5:
    E=3
    print("\nYou have selected Cola")
    print("\ninsert amount 3 dhs")
    inp=float(input("ENTER YOUR AMOUNT"))
    if inp >= E:
      print("\nPAYMENT COMPLETED") 
      print("\nyou have entered",inp)
      change=inp-E
      print("please recieve your Balance:",change)
    elif inp < E:
      print("insufficient Funds")
      return menu()
    else:
      print("Error")
      return menu()
    inp=input("would you like to have anything else")
    if inp=="yes":
       return menu()
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
      
    else:
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")

  elif x==6:
    F=3
    print("\nYou have selected Sandwich")
    print("\ninsert amount 3 dhs")
    inp=float(input("ENTER YOUR AMOUNT"))
    if inp >= F:
      print("\nPAYMENT COMPLETED")
      print("\nyou have entered",inp)
      change=inp-F
      print("please recieve your Balance:",change)
    elif inp < F:
      print("insufficient Funds")
      return menu()
    else:
      print("Error")
      return menu()
    inp=input("would you like to have anything else")
    if inp=="yes":
       return menu()
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
      
    else:
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")

  elif x==7:
    G=2
    print("\nYou have selected Croissant")
    print("\ninsert amount 2 dhs")
    inp=float(input("ENTER YOUR AMOUNT"))
    if inp >= G:
      print("\nPAYMENT COMPLETED")
      print("\nyou have entered",inp)
      change=inp-G
      print("please recieve your Balance:",change)
    elif inp < G:
      print("insufficient Funds")
      return menu()
    else:
      print("Error")
      return menu()
    inp=input("would you like to have anything else")
    if inp=="yes":
       return menu()
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
      
    else:
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
   

  elif x==8:
    H=2
    print("\nYou have selected Potato chips")
    print("\ninsert amount 2 dhs")
    inp=float(input("ENTER YOUR AMOUNT"))
    if inp >= H:
      print("\nPAYMENT COMPLETED")
      print("\nyou have entered",inp)
      change=inp-H
      print("please recieve your Balance:",change)
    elif inp < H:
      print("insufficient Funds")
      return menu()
    else:
      print("Error")
      return menu()
    inp=input("would you like to have anything else")
    if inp=="yes":
       return menu()
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
      
    else:
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")

  elif x==9:
    I=4
    print("\nYou have selected Pizza")
    print("\ninsert amount 4 dhs")
    inp=float(input("ENTER YOUR AMOUNT"))
    if inp >= I:
      print("\nPAYMENT COMPLETED")
      print("\nyou have entered",inp)
      change=inp-I
      print("please recieve your Balance:",change)
    elif inp < I:
      print("insufficient Funds")
      return menu()
    else:
      print("Error")
      return menu()
    inp=input("would you like to have anything else")
    if inp=="yes":
       return menu()
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
      
    else:
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")

  elif x==10:
    J=5
    print("\nYou have selected Burger")
    print("\ninsert amount 5 dhs")
    inp=float(input("ENTER YOUR AMOUNT"))
    if inp >= J:
      print("\nPAYMENT COMPLETED")
      print("\nyou have entered",inp)
      change=inp-J
      print("please recieve your Balance:",change)
    elif inp < J:
      print("insufficient Funds")
      return menu()
    else:
      print("Error")
      return menu()
    inp=input("would you like to have anything else")
    if inp=="yes":
       return menu()
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
      
    else:
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")

  elif x==11:
    K=3
    print("\nYou have selected Iced Coffee")
    print("\ninsert amount 3 dhs")
    inp=float(input("ENTER YOUR AMOUNT"))
    if inp >= K:
      print("\nPAYMENT COMPLETED")
      print("\nyou have entered",inp)
      change=inp-K
      print("please recieve your Balance:",change)
    elif inp < K:
      print("insufficient Funds")
      return menu()
    else:
      print("Error")
      return menu()
    inp=input("would you like to have anything else")
    if inp=="yes":
       return menu()
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
      
    else:
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")

  elif x==12:
    L=3
    print("\nYou have selected Popcorn")
    print("\ninsert amount 5 dhs")
    inp=float(input("ENTER YOUR AMOUNT"))
    if inp >= L:
      print("\nPAYMENT COMPLETED")
      print("\nyou have entered",inp)
      change=inp-L
      print("please recieve your Balance:",change)
    elif inp < L:
      print("insufficient Funds")
      return menu()
    else:
      print("Error")
      return menu()
    inp=input("would you like to have anything else")
    if inp=="yes":
       return menu()
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
      
    else:
       print("\nYOUR ITEM HAS BEEN DISPENSED!")
       print("----------THANK YOU FOR SHOPPING----------")
       print("------------HAVE A NICE DAY-------------")
     
# if user enters the wrong code from the given menu    
# it prints "ERROR" and gives the user chances to input the code again 
  else : 
    print("ERROR")
    #return menu()

# at the end it print a message to show the users that their items has been dispensed
menu()




#the end