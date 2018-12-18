inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
# yeu cau 1
inventory['pocket'] = []

# yeu cau 2
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# yeu cau 3
for key, value in inventory.items():
    if key == 'backpack':
        del value[1]

# yeu cau4
inventory['gold'] += 50

for key1, value1 in inventory.items():
    print(key1, value1)
