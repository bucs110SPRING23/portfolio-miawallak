amount = float(input("Enter the amount:" ))
rate = input("Enter the exchange rate: ")
new_amount = amount * rate
minus_fees = new_amount - 3
print("Your result minus a $3 convenience fee is ", minus_fees)