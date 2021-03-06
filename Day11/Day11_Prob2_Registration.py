from IntCode import intcode_day11 as intcode


def join_list(lst, string=', '):
    """
    :param lst: List to be joined
    :param string: String that will be used to join the items in the list
    :return: List after being converted into a string
    """
    lst = str(string).join(str(x) for x in lst)
    return lst


robot_program = [3, 8, 1005, 8, 332, 1106, 0, 11, 0, 0, 0, 104, 1, 104, 0, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 108, 1, 8, 10, 4, 10, 101, 0, 8, 28, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 101, 0, 8, 51, 1, 1103, 5, 10, 1, 1104, 9, 10, 2, 1003, 0, 10, 1, 5, 16, 10, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 108, 0, 8, 10, 4, 10, 1001, 8, 0, 88, 1006, 0, 2, 1006, 0, 62, 2, 8, 2, 10, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 102, 1, 8, 121, 1006, 0, 91, 1006, 0, 22, 1006, 0, 23, 1006, 0, 1, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 101, 0, 8, 155, 1006, 0, 97, 1, 1004, 2, 10, 2, 1003, 6, 10, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 108, 0, 8, 10, 4, 10, 1002, 8, 1, 187, 1, 104, 15, 10, 2, 107, 9, 10, 1006, 0, 37, 1006, 0, 39, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 108, 0, 8, 10, 4, 10, 102, 1, 8, 223, 2, 2, 17, 10, 1, 1102, 5, 10, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 108, 0, 8, 10, 4, 10, 1001, 8, 0, 253, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 1002, 8, 1, 276, 1006, 0, 84, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 1008, 8, 0, 10, 4, 10, 1001, 8, 0, 301, 2, 1009, 9, 10, 1006, 0, 10, 2, 102, 15, 10, 101, 1, 9, 9, 1007, 9, 997, 10, 1005, 10, 15, 99, 109, 654, 104, 0, 104, 1, 21102, 1, 936995738516, 1, 21101, 0, 349, 0, 1105, 1, 453, 21102, 1, 825595015976, 1, 21102, 1, 360, 0, 1105, 1, 453, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 1, 21102, 46375541763, 1, 1, 21101, 0, 407, 0, 1105, 1, 453, 21102, 1, 179339005019, 1, 21101, 0, 418, 0, 1106, 0, 453, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 0, 21102, 825012036372, 1, 1, 21102, 441, 1, 0, 1105, 1, 453, 21101, 988648461076, 0, 1, 21101, 452, 0, 0, 1105, 1, 453, 99, 109, 2, 22102, 1, -1, 1, 21102, 40, 1, 2, 21102, 484, 1, 3, 21101, 0, 474, 0, 1106, 0, 517, 109, -2, 2105, 1, 0, 0, 1, 0, 0, 1, 109, 2, 3, 10, 204, -1, 1001, 479, 480, 495, 4, 0, 1001, 479, 1, 479, 108, 4, 479, 10, 1006, 10, 511, 1102, 1, 0, 479, 109, -2, 2105, 1, 0, 0, 109, 4, 2102, 1, -1, 516, 1207, -3, 0, 10, 1006, 10, 534, 21101, 0, 0, -3, 21202, -3, 1, 1, 22101, 0, -2, 2, 21102, 1, 1, 3, 21102, 553, 1, 0, 1106, 0, 558, 109, -4, 2106, 0, 0, 109, 5, 1207, -3, 1, 10, 1006, 10, 581, 2207, -4, -2, 10, 1006, 10, 581, 22102, 1, -4, -4, 1105, 1, 649, 21202, -4, 1, 1, 21201, -3, -1, 2, 21202, -2, 2, 3, 21101, 0, 600, 0, 1105, 1, 558, 21201, 1, 0, -4, 21101, 0, 1, -1, 2207, -4, -2, 10, 1006, 10, 619, 21101, 0, 0, -1, 22202, -2, -1, -2, 2107, 0, -3, 10, 1006, 10, 641, 22102, 1, -1, 1, 21102, 1, 641, 0, 106, 0, 516, 21202, -2, -1, -2, 22201, -4, -2, -4, 109, -5, 2105, 1, 0]

# Initial value for the Intcode
memory = robot_program[:]
com_pos = 0
rel_bas = 0

# Initial values for the panels and robot
total_list, order_list = [], []
white_list, black_list = [[0, 0]], []
coords = [0, 0]
directions = ['up', 'right', 'down', 'left']
looking = 0

while True:
    # See the color of the panel
    if white_list.__contains__(coords):
        color = [1]
    else:
        color = [0]
    # Get the robot's action
    memory, outputs, com_pos, rel_bas = intcode(memory, color, com_pos, rel_bas)

    # Evaluate the outputs
    if outputs.__contains__(-1):
        break
    else:
        # Paint the tile
        if outputs[0] == 0:
            if coords in white_list:
                white_list.remove(coords[:])
            if coords not in black_list:
                black_list += [coords[:]]
        elif outputs[0] == 1:
            if coords in black_list:
                black_list.remove(coords[:])
            if coords not in white_list:
                white_list += [coords[:]]

        # Save the current coordinates
        if coords not in total_list:
            total_list += [coords[:]]
        order_list += [coords[:]]

        # Change the direction in which the robot is looking
        if outputs[1] == 0:
            looking += -1
        elif outputs[1] == 1:
            looking += 1
        if looking == 4:
            looking = 0
        elif looking == -5:
            looking = -1

        # Walks in the direction it's looking
        if directions[looking] == 'up':
            coords[1] += 1
        elif directions[looking] == 'down':
            coords[1] += -1
        elif directions[looking] == 'right':
            coords[0] += 1
        elif directions[looking] == 'left':
            coords[0] += -1

image = []
image += [[]] * 50
for c in range(0, len(image)):
    image[c] = ['.'] * 20

for item in total_list:
    if white_list.__contains__(item):
        image[item[0]+ 10][item[1]-1] = '#'

for item in image:
    print(join_list(item, ' '))
