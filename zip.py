names = [
    'Joe',
    'jean',
    'marcel',
    'eric',
    ]

birthyears=[
    1980,
    1972,
    2003,
    1956
    ]
#for i in range(len(names)):
for name, birthyear in zip(names, birthyears):
    print('%s born %s' % (name, birthyear))
    #print('%s born %d' % (names[i], birthyears[i]))

