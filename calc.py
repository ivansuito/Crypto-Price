print("Crypto calculator by Ivan")

for x in range(999):
    q1 = float(input("\nYour actual amount: "))
    q2 = float(input("\nActual crypto price: "))
    q3 = float(input("\nHypothetical crypto price: "))
    opr = q1 * q3
    total = opr / q2
    print("\n>", total, "<")
    if q1 == "exit":
        break
    if q2 == "exit":
        break
    if q3 == "exit":
        break
    input("\nPress ENTER to continue...")