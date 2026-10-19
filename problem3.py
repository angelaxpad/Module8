totalbonus = 0

print(f"{'Employee':<15}{'Salary':>12}{'Bonus':>12}")
print("-" * 39)

for name, salary in employees:
    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10

    bonus = salary * rate
    totalbonus += bonus

    print(f"{name"<15}${salary:>1,.2f}${bonus:>10,.2f}")

print("-" * 39)
print(f"Total bonuses paid: ${totalbonus:,.2f}")
