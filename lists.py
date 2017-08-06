names = [
    'Joe',
    'jean',
    'marcel',
    'eric',
]


def last_letter(name):
    return name[-1]

names.sort(key=last_letter)
names.sort(key=lambda name: name[-1])
print(names)
