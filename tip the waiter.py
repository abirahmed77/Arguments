def calculateBill(b,tp):
    
    total = b * (1+ (0.01*tp))
    return total

bill = int(input("Enter the Bill amount: "))
tipPerc = float(input("Enter the Tip amount: "))

total = calculateBill(bill, tipPerc)

print(f"\n\nTotal bill with tip: {total}")
print(f"Total tip: {total-bill}")