maxWeight = 20
inventory = {'default': 0}

def isOverloaded(a):
    return sum(inventory.values()) + a > maxWeight


while True:
    com = input('Choose a command(print number):\n1:add item\n2:delete item\n3:print items\n4:end program\n')
    if com == '1':
        name = input("Write item's name:")
        weight = float(input("Write item's weight:"))
        if weight <= 0:
            print('Weight should be a positive number')
        elif isOverloaded(weight):
            print('No space for this item')
        else:
            inventory[name] = weight
    elif com == '2':
        name = input("Write item's name:")
        if name == 'default':
            print('Permission denied')
        elif inventory.pop(name, -1) == -1:
            print('No item with name "{}"'.format(name))
    elif com == '3':
        for i in inventory.keys():
            if i != 'default':
                print('{}:{}'.format(i, inventory[i]))
    elif com == '4':
        break
    else:
        print('wrong command')
