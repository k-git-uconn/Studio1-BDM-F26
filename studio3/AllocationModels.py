
# Import modules
import pandas as pd
from pylab import *
import pyomo
from pyomo.environ import *

# Specify the CBC solver path
cbc_path = r"D:\Users\ccs\miniforge3\envs\optimization\Library\bin\cbc.exe"

# Connect Pyomo to CBC
solver = SolverFactory("cbc", executable=cbc_path)

# Verify installation
print("Pyomo is installed. Version:", pyomo.__version__)
print("CBC available:", solver.available())

from pyomo.environ import *

model = ConcreteModel()

model.chairs = Var(domain=NonNegativeReals) # could try NonNegativeIntegers here too!
model.desks = Var(domain=NonNegativeReals) # d for desks
model.tables = Var(domain=NonNegativeReals) # t for tables

# declare objective
model.profit = Objective(
                      expr = 15*model.chairs + 24*model.desks + 18*model.tables, # values come from the table
                      sense = maximize)

# write the constraints one by one, don't forget LHS vs. RHS
# it's OK to have mixed constraints (LHS <= RHS vs. LHS >= RHS)!!!
model.constraint1 = Constraint(expr = 4*model.chairs + 6*model.desks + 2*model.tables <= 1850) # fabrication hours
model.constraint2 = Constraint(expr = 3*model.chairs + 5*model.desks + 7*model.tables <= 2400) # assembly hours
model.constraint3 = Constraint(expr = 3*model.chairs + 2*model.desks + 4*model.tables <= 1500) # shipping
model.constraint4 = Constraint(expr = model.chairs <= 360) # c demand
model.constraint5 = Constraint(expr = model.desks <= 300) # d demand
model.constraint6 = Constraint(expr = model.tables <= 100) # t demand

# show the model you've created
model.pprint()

cbc_path = r"D:\Users\ccs\miniforge3\envs\optimization\Library\bin\cbc.exe"
#            solver          path the solver
SolverFactory('cbc', executable=cbc_path).solve(model).write()

print("Profit = ", model.profit(), " per week")

print("Chairs = ", model.chairs(), " units per week")
print("Desks = ", model.desks(), " units per week")
print("Tables = ", model.tables(), " units per week")

print("**********************************************************")
print("Fabrication = ", model.constraint1(), "hours")
print("Assembly = ", model.constraint2(), "hours")
print("Shipping = ", model.constraint3(), "hours")
print("Chairs = ", model.constraint4(), " units per week")
print("Desks = ", model.constraint5(), " units per week")
print("Tables = ", model.constraint6(), " units per week")
print("**********************************************************")


