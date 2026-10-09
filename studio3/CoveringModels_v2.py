
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
model.s = Var(domain=NonNegativeReals) # s for seeds
model.r = Var(domain=NonNegativeReals) # r for raisin
model.f = Var(domain=NonNegativeReals) # flakes
model.p = Var(domain=NonNegativeReals) # pecans
model.w = Var(domain=NonNegativeReals) # walnuts # bounds=(0.15,Inf))

# declare objective
model.cost = Objective(
                      expr = 4*model.s + 5*model.r + 3*model.f + 7*model.p + 6*model.w, # values come from the table
                      sense = minimize)

# declare constraints
model.Constraint1 = Constraint(expr = 10*model.s + 20*model.r + 10*model.f + 30*model.p + 20*model.w >= 16) # vitamins
model.Constraint2 = Constraint(expr = 5*model.s + 7*model.r + 4*model.f + 9*model.p + 2*model.w >= 10) # minerals
model.Constraint3 = Constraint(expr = 1*model.s + 4*model.r + 10*model.f + 2*model.p + 1*model.w >= 15) # protein
model.Constraint4 = Constraint(expr = 500*model.s + 450*model.r + 160*model.f + 300*model.p + 500*model.w >= 600) # calories

# adding bound
model.Constraint5 = Constraint(expr = 1*model.s >= 0.15) # some seeds (at least 0.15 pounds of seeds)
model.Constraint6 = Constraint(expr = 1*model.r >= 0.15) # some raisins
model.Constraint7 = Constraint(expr = 1*model.f >= 0.15) # some flakes
model.Constraint8 = Constraint(expr = 1*model.p >= 0.15) # some flakes
model.Constraint9 = Constraint(expr = 1*model.w >= 0.15) # some walnuts

model.pprint()

# solve it
solver.solve(model).write()

# show the results
print("Cost = ", model.cost(), ' USD')
print("Seeds = ", model.s(), ' pounds')
print("Raisins = ", model.r(), ' pounds')
print("Flakes = ", model.f(), ' pounds')
print("Pecans = ", model.p(), ' pounds')
print("Walnuts = ", model.w(), ' pounds')

print("**************************************************")
# can we show how the constraints were satisfied?
print("Vitamin Content: ", model.Constraint1())
print("Minerals Content: ",model.Constraint2())
print("Protein Content: ",model.Constraint3())
print("Calories Content: ",model.Constraint4())
print("Seeds Supply Constraint:", model.Constraint5(),' pounds')
print("Raisins Supply Constraint:", model.Constraint6(),' pounds')
print("Flakes Supply Constraint:", model.Constraint7(),' pounds')
print("Pecans Supply Constraint:", model.Constraint8(),' pounds')
print("Walnuts Supply Constraint:", model.Constraint9(),' pounds')