d = {'k1':'value1','k2':'value2','k3':'value3'}
print(d)
print(d['k1'])

salaries = {'Raju':230,'Shyam':200,'Baburao':25}
print(salaries['Raju'])
salaries['Raju'] = salaries['Raju'] - 29 
print(salaries['Raju'])


salaries = {'Raju':['radha','meena','shiela'],'Shyam':['Anuradaha','meri anuradha'],'Baburao':25}
print(salaries['Shyam'][1])

salaries = {'Raju':{'haan chal':'baap ko mat sikha'},'Shyam':{'meri anuradha':'sharif hai','21 din ma paisa':'double'},'Baburao':{'kidney':'ma heart attack'}}
print(salaries['Shyam']['meri anuradha'])
print(salaries.keys())
print(salaries.values())
print(salaries.items())
