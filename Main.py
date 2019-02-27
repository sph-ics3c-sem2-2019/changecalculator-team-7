#Change Calculator
# Read in a cost
# Read in the amount given
# Calculate the change
# Break the change into how many nickels, dimes, quarters
# loonies, toonies, $5s, $10s, $20s, $50s, $100s
# If amount is below the cost, say how much more they owe.
cost=float(input("How much does the item cost?"))
amount=float(input("How much is the payment?"))
change=amount - cost
print("your change is",change)
owe=change*-1
print("You owe", owe)
num100=change//100
print(num100,100,"x 100$")
change=change%100
num50=change//50
print(num50,50,"x 50$")
change=change%50
num20=change//20
print(num20,20,"x 20$")
change=change%20
num10=change//10
print(num10,10,"x 10$")
change=change%10
num5=change//5
print(num5,5,"x 5$")
change=change%5
num2=change//2
print(num2,2,"x 2$")
change=change%2
num1=change//1
print(num1,1,"x 1$")
change=change%1
numquarter=change//0.25
print(numquarter,0.25,"x quater")
change=change%0.25
numdime=change//0.10
print(numdime,0.10,"x dime")
change=change%0.10
numnickel=change//0.05
print(numnickel,0.05,"x nickel")
change=change%0.05

