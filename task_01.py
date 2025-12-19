import pulp

# Selecting LpMaximize
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Setting lowBound and cat
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# main part
model += lemonade + fruit_juice, "Total_Production"

model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Limit"
model += 1 * lemonade <= 50, "Sugar_Limit"
model += 1 * lemonade <= 30, "Lemon_Juice_Limit"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Limit"

# solve
model.solve()

# Results
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade Quantity: {int(lemonade.varValue)} units.")
print(f"Fruit Juice Quantity: {int(fruit_juice.varValue)} units.")
print(f"Total Ammount of produced products: {int(pulp.value(model.objective))} units.")