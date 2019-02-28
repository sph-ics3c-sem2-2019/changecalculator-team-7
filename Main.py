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
if change>0:
    print("Your change is",change)
owe=change*-1
if owe>0:
    print("You owe", owe)
else:
    num100=change//100
    if num100>0:
        print(num100,"x 100$")
    change=change%100
    num50=change//50
    if num50>0:
        print(num50,"x 50$")
    change=change%50
    num20=change//20
    if num20>0:
        print(num20,"x 20$")
    change=change%20
    num10=change//10
    if num10>0:
        print(num10,"x 10$")
    change=change%10
    num5=change//5
    if num5>0:
        print(num5,"x 5$")
    change=change%5
    num2=change//2
    if num2>0:
        print(num2,"x 2$")
    change=change%2
    num1=change//1
    if num1>0:
        print(num1,"x 1$")
    change=change%1
    numquarter=change//0.25
    if numquarter>0:
        print(numquarter,"x quater")
    change=change%0.25
    numdime=change//0.10
    if numdime>0:
        print(numdime,"x dime")
    change=change%0.10
    numnickel=change//0.05
    if numnickel>0:
        print(numnickel,"x nickel")
    change=change%0.05


