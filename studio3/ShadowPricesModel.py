
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

import pandas as pd

myHours = np.arange(1500,5000,100)
print(myHours)
myResults = pd.DataFrame() # empty place to store results

for a in myHours:
    # declare the model
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
    model.constraint1 = Constraint(
        expr = 4*model.chairs + 6*model.desks + 2*model.tables <= a) # fabrication hours
    model.constraint2 = Constraint(
        expr = 3*model.chairs + 5*model.desks + 7*model.tables <= 2400) # assembly hours
    model.constraint3 = Constraint(
        expr = 3*model.chairs + 2*model.desks + 4*model.tables <= 1500) # shipping
    model.constraint4 = Constraint(expr = model.chairs <= 360) # c demand
    model.constraint5 = Constraint(expr = model.desks <= 300) # d demand
    model.constraint6 = Constraint(expr = model.tables <= 100) # t demand

    # show the model you've created
    model.pprint()

    solver.solve(model).write()

    # results
    myX = pd.DataFrame([a, model.profit(), model.chairs(), model.desks(), model.tables()])
    myX=myX.T # transpose

    # store the profit
    # NOTE: DataFrame.append was removed in pandas 2.0 - pd.concat replaces it
    myResults = pd.concat([myResults, myX])


# Change the Column names
myResults = myResults.rename( {0:"Fabrication Hours", 1:"Profit",2:"Chairs", 3:"Desks" ,4:"Tables"}, axis='columns')
myResults.reset_index(drop=True, inplace=True)
print(myResults)

# make a nice plot
tmp = myResults.drop(['Profit'], axis=1)
tmp.plot(x='Fabrication Hours')
plt.show()

# add a column for marginal increase (per 100 hours)
myResults['ProfitDiff'] = myResults['Profit'].diff()

# if you wanted it by ONE HOUR
myResults['ProfitDiffOneHour'] = myResults['Profit'].diff()/myResults['Fabrication Hours'].diff()

# show the table
myResults

tmp = myResults.drop(['Profit','Chairs','Desks','Tables'], axis=1)
tmp.plot(x='Fabrication Hours', y='ProfitDiffOneHour')
plt.show()