totalbonus = 0

for name, salary in employees:
    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10

    bonus = salary * rate
    totalbonus += bonus

    print(name, "Salary:", salary, "Bonus:", bonus)
    
print(f"Total bonuses paid: ${totalbonus:,.2f}")
