def main():
    owed = float(input("How much change is owed? "))
    quarters = owed // .25
    dimes = (owed % .25) // .10
    nickels = ((owed % .25) % .10) // .05
    pennies = (((owed % .25) % .10) % .05) // .01
    if quarters > 0:
        print("You need", quarters, "quarters.")
    if dimes > 0:
        print("You need", dimes, "dimes.")
    if nickels > 0:
        print("You need", nickels, "nickels.")
    if pennies > 0:
        print("You need", pennies + 1, "pennies.")
main()
