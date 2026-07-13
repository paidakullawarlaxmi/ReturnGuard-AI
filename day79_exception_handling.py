
print("=== ReturnGuard AI ===")

try:
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    total = quantity * price

    print("Total Amount:", total)

except ValueError:
    print("❌ Please enter valid numbers.")

finally:
    print("Program Finished.")