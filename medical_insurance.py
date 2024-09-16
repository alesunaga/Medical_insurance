# Add your code here
#1 
medical_costs = {}

#2
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0

#3
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})

#4
#print(medical_costs)

#5
medical_costs["Vinay"] = 3325.0
#print(medical_costs)

#6
total_cost = 0
for cost in medical_costs.values():
  total_cost += cost

#7
average_cost = total_cost / len(medical_costs)
#print("Average Insurance Cost: " + str(average_cost))

#8
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

#9
zipped_ages = zip(names,ages)

#10
names_to_ages = dict(zipped_ages)
#print(names_to_ages)

#11
marina_age = names_to_ages.get("Marina", None)
#print("Marina's age is "+ str(marina_age))

#12
medical_records = {}

#13
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}

#14
names_2 = ["Vinay", "Connie", "Isaac", "Valentina"]
sex = ["Male", "Female", "Male", "Female"]
bmi = [26.9, 25.3, 20.6, 18.7]
child = [0, 3, 4, 1]
smoker = ["Non-smoker", "Non-smoker", "Smoker", "Non-smoker"]
insurance_cost = [3225.0, 8886.0, 16444.0, 6420.0]

zipped_data = zip(names_2, ages, sex, bmi, child, smoker, insurance_cost )

medical_records.update({
  names_2 : {
    "Age": ages,
    "Sex": sex,
    "BMI": bmi,
    "Children": child,
    "Smoker": smoker,
    "Insurance_cost": cost
  }
  for names_2, ages, sex, bmi, child, smoker, cost in zipped_data
})
#print(medical_records)

#16
#print("Connie's insurance cost is "+ str(medical_records["Connie"]["Insurance_cost"]) + " dollars.")

#17
medical_records.pop("Vinay")
print(medical_records)

#18
for pat in medical_records:
  patient_info = medical_records[pat]
  print(pat + " is a " + str(patient_info["Age"]) + " year old " + str(patient_info["Sex"]) + " " + str(patient_info["Smoker"]) + " with a BMI of " + str(patient_info["BMI"]) + " and insurance cost of " + str(patient_info["Insurance_cost"]))
