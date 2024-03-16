import pulp

# create model
model = pulp.LpProblem(name="Maximize Production", sense=pulp.LpMaximize)

lemonade = pulp.LpVariable("lemonade", lowBound=0, cat="Integer")
juice = pulp.LpVariable("juice", lowBound=0, cat="Integer")

# resource limitation
model += 2 * lemonade + 1 * juice <= 100 # water limit
model += 1 * lemonade <= 50 # sugar limit
model += 1 * lemonade <= 30 # lemon juice limit
model += 2 * juice <= 40 # fruit pure limit

# maximize function 
model += lemonade + juice

# Solve
model.solve()


# Print result
print(f"Lemonade {lemonade.varValue}")
print(f"Fruit juice {juice.varValue}")
print(f"Total {model.objective.value()}")
