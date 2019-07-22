usernameinput = input("username :")
passwordinput = input("password:")
if usernameinput=="Chananya" and passwordinput =="361255":
 print("Welcome to Chananya Shop")
 print("What do want to buy something?")
 print("This is all Menu in Chananya Shop")
 print("--------------------")
 print("1.Water    10 THB")
 print("2.Candy     5 THB")
 print("3.Milk     15 THB")
 print("4.Lay      20 THB")
 print("5.Pen      10 THB")
 print("-------------------")
 Item=int(input("Do you want to buy? "))
    
 if   Item==1:
  cost1=10
  print("Your Item:",Item," = ",cost1,"THB")
 elif Item==2:
  cost1=5
  print("Your Item:",Item," = ",cost1,"THB")
 elif Item==3:
  cost1=15
  print("You Item:",Item," = ",cost1,"THB")
 elif Item==4:
  cost1=20
  print("Your Item:",Item," = ",cost1,"THB")
 elif Item==5:
  cost1=10
  print("Your Item:",Item," = ",cost1,"THB")
 amount1=int(input("Do you want to amount? "))
       
 if   Item==1:
  cost1=10
  print("Total:",Item," = ",cost1*amount1,"THB")
 elif Item==2:
  cost1=5
  print("Total:",Item," = ",cost1*amount1,"THB")
 elif Item==3:
  cost1=15
  print("Total:",Item," = ",cost1*amount1,"THB")
 elif Item==4:
  cost1=20
  print("Total:",Item," = ",cost1*amount1,"THB")
 elif Item==5:
  cost1=10
  print("Total:",Item," = ",cost1*amount1,"THB")
 Item=int(input("Do you want to buy? "))
        
 if   Item==1:
  cost2=10
  print("Your Item:",Item," = ",cost2,"THB")
 elif Item==2:
  cost1=5
  print("Your Item:",Item," = ",cost2,"THB")
 elif Item==3:
  cost2=15
  print("Your Item:",Item," = ",cost2,"THB")
 elif Item==4:
  cost2=20
  print("Your Item:",Item," = ",cost2,"THB")
 elif Item==5:
  cost2=10
  print("Your Item:",Item," = ",cost2,"THB")
 else:
  print("You not Item: ")
 amount2=int(input("Do you want to amount? "))
       
 if   Item==1:
  cost2=10
  print("Total:",Item," = ",cost2*amount2,"THB")
 elif Item==2:
  cost2=5
  print("Total:",Item," = ",cost2*amount2,"THB")
 elif Item==3:
  cost2=15
  print("Total:",Item," = ",cost2*amount2,"THB")
 elif Item==4:
  cost2=20
  print("Total:",Item," = ",cost2*amount2,"THB")
 elif Item==5:
  cost2=10
  print("Total:",Item," = ",cost2*amount2,"THB")
 Item=int(input("Do you want to buy? "))
        
 if   Item==1:
  cost3=10
  print("Your Item:",Item," = ",cost3,"THB")
 elif Item==2:
  cost3=5
  print("Your Item:",Item," = ",cost3,"THB")
 elif Item==3:
  cost3=15
  print("Your Item:",Item," = ",cost3,"THB")
 elif Item==4:
  cost3=20
  print("Your Item:",Item," = ",cost3,"THB")
 elif Item==5:
  cost3=10
  print("Your Item:",Item," = ",cost3,"THB")
 else:
  print("You not Item: ")
 amount3=int(input("Do you want to amount? "))
        
 if   Item==1:
  cost3=10
  print("Total:",Item," = ",cost3*amount3,"THB")
 elif Item==2:
  cost3=5
  print("Total:",Item," = ",cost3*amount3,"THB")
 elif Item==3:
  cost3=15
  print("Total:",Item," = ",cost3*amount3,"THB")
 elif Item==4:
  cost3=20
  print("Total:",Item," = ",cost3*amount3,"THB")
 elif Item==5:
  cost3=10
  print("Total:",Item," = ",cost3*amount3,"THB")
  print("All Total:",Item," = ",cost1*amount1+cost2*amount2+cost3*amount3,"THB")
else:
 print("Error")
        