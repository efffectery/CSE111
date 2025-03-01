from datetime import datetime

date = datetime.now()
day = date.weekday()
day = 1

subtotal = float(input("Enter the subtotal: "))

if day == 1 or day == 2 and subtotal >= 50:
    total = subtotal * 0.9
    dicount_amount = subtotal * 0.1
    sales_tax = total * 0.06
    total += sales_tax
    print(f"discont amount {dicount_amount}")
    print(f"Sales Tax: {sales_tax}")
    print(f"Total: {total}")
else:
    total = subtotal
    sales_tax = subtotal * 0.06
    total += sales_tax
    print(f"Sales Tax: {sales_tax}")
    print(f"Total: {total}")
    

