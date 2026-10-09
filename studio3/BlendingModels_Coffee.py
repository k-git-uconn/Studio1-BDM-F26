
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

# declare decision variables
model.b = Var(domain=NonNegativeReals) # brazil
model.c = Var(domain=NonNegativeReals) # colombia
model.p = Var(domain=NonNegativeReals) # peru

# declare objective
model.cost = Objective(
                      expr = 0.5*model.b + 0.6*model.c + 0.7*model.p, # values come from the table
                      sense = minimize) # remember, you are minimizing cost!!!

# declare constraints
model.Constraint1 = Constraint(expr = model.b + model.c + model.p >= 4000000) # demand

# blending constraints
model.Constraint2 = Constraint(expr = -3*model.b + -18*model.c + 7*model.p >= 0) # aroma
model.Constraint3 = Constraint(expr = -1*model.b + 4*model.c + 2*model.p >= 0) # stength

# other constraints
model.Constraint4 = Constraint(expr = model.b <= 1500000) # b supply
model.Constraint5 = Constraint(expr = model.c <= 1200000) # c supply
model.Constraint6 = Constraint(expr = model.p <= 2000000) # p supply

model.pprint()

solver.solve(model).write()

# show the results
print("Cost = ", model.cost(), " USD")
print("Brazilian Beans = ", model.b(), " lb")
print("Colombian Beans = ", model.c(), " lb")
print("Peruvian Beans = ", model.p(), " lb")

print("**************************************************")
print("Demand Constraint:", model.Constraint1())
print("Aroma Constraint:", model.Constraint2()) # don't worry if these look funky! more below.
print("Stength Constraint", model.Constraint3()) # don't worry if these look funky!
print("B Supply Constraint:", model.Constraint4())
print("C Supply Constraint:", model.Constraint5())
print("P Supply Constraint", model.Constraint6())