totaltuition = 0
count = 0

for name, district, credits in students:
    if district == "I":
        tuition = credits * 250
    else:
        tuition =credits * 500

    totaltuition += tuition
    count += 1

    print(name, district, credits, "Tuition:", tuition)

print("Total tuition:", totaltuition)
print("Number of students:", count)
  
      
