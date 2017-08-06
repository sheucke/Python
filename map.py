names = [
    'Joe',
    'jean',
    'marcel',
    'eric',
    ]
#Create a new list in which all first letters are capitalized
#new_names=[]
#for name in names:
 #   new_names.append(name.capitalize())

#new_names = map(lambda name: name.capitalize(), names)
#new_names = filter(lambda name: name.startswith('j'), names)
new_names=[name.capitalize() for name in names if name.startswith('j')]
#Print the new names out

for name in new_names:
    print(name)

new_names=[]
for name in names:
    if name.startswith('j'):
        new_names.append(name)

for name in new_names:
    print('\n',name)
