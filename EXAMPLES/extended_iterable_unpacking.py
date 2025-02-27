values = ['a', 'b', 'c', 'd', 'e']  # values has 6 elements

x, y, *z = values  # * takes all extra elements from iterable
print(f"x: {x}    y: {y}    z: {z}\n")

x, *y, z = values  # * takes all extra elements from iterable
print(f"x: {x}    y: {y}    z: {z}\n")

*x, y, z = values  # * takes all extra elements from iterable
print(f"x: {x}    y: {y}    z: {z}\n")

people = [
    ('Bill', 'Gates', 'Microsoft'),
    ('Steve', 'Jobs', 'Apple'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey', 'Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linux', 'Torvalds', 'Linux'),
]

for *name, _ in people:  # name gets all but the last field
    print(name)
print()
