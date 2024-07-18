from datetime import datetime

subtotal = float(input("please enter your subtotal: "))
discount = float(subtotal * 0.10)
tax = subtotal * 0.06

current_date = datetime.now(tz=None)
day = current_date.weekday()

if day == 1 and subtotal > 50:
    discount1 = subtotal - discount
    tax1 = float(discount1 * 0.06)
    price1 = float(discount1 + tax1)
    print(f"Discount amount: {discount:.2f}")
    print(f"Sales tax amount: {tax1:.2f}")
    print(f"Total: ${price1:.2f}")
elif day == 2 and subtotal > 50:
    discount2 = float(subtotal - discount)
    tax2 = float(discount2 * 0.06)
    price2 = float(discount2 + tax2)
    print(f"Discount amount: ${discount:.2f}")
    print(f"sales tax amount: ${tax2:.2f}")
    print(f"Total: ${price2:.2f}")
else:
    price3 = subtotal + tax
    print(f"Sales tax amount: {tax:.2f}")
    print(f"Total: {price3:.2f}")

