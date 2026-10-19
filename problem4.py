total = 0
count = 0

for name, quantity, price in products:
    extendedprice = quantity * price
    total += extendedprice
    count += 1

    print(name, quantity, price, extendedprice)

average = total / count

print("Total:", total)
print("Number of orders:", count)
print("Average:", average)
