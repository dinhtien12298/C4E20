map = {
    "size_x": 10,
    "size_y": 7
}

player = { "x":3, "y":4}

boxes = [
    {"x": 1,"y": 1},
    {"x": 2,"y": 2},
    {"x": 3,"y": 3}
]

destination = [
    {"x": 2,"y": 1},
    {"x": 3,"y": 2},
    {"x": 4,"y": 3}
]

walls = [
    {"x": 8,"y": 2},
    {"x": 8,"y": 5},
    {"x": 3,"y": 5}
]
playing = True
count = 0   # tao bien dem de kiem tra undo 1 lan
while playing:
    # print map
    for y in range(map['size_y']):
        for x in range(map['size_x']):

            player_is_here = False
            if y == player['y'] and x == player['x']:
                player_is_here = True

            box_is_here = False
            for box in boxes:
                if y == box['y'] and x == box['x']:
                    box_is_here = True

            destination_is_here = False
            for des in destination:
                if y == des['y'] and x == des['x']:
                    destination_is_here = True

            wall_is_here = False
            for wall in walls:
                if y == wall['y'] and x == wall['x']:
                    wall_is_here = True

            if player_is_here:
                print("P ", end='')
            elif box_is_here:
                print("B ", end='')
            elif destination_is_here:
                print("D ", end='')
            elif wall_is_here:
                print("O ", end='')
            else:
                print("_ ", end='')
        print()
    # end of print map

    # checkwin
    win = True
    for box in boxes:
        if box not in destination:
            win = False

    if win:
        print("YOU WIN!!")
        break
    
    dx = 0
    dy = 0

    move = input("What is your next move? W/A/S/D Or (Undo - Z - You can Undo only 1 time after a move) ").upper()
    if move == "W":
        dy = -1
        dx1 = 0
        dy1 = 1
        count = 0
    elif move == "S":
        dy = 1
        dx1 = 0
        dy1 = -1
        count = 0
    elif move == "A":
        dx = -1
        dx1 = 1
        dy1 = 0
        count = 0
    elif move == "D":
        dx = 1
        dx1 = -1
        dy1 = 0
        count = 0
    elif move == "Z":
        if count == 0:
            player['x'] += dx1
            player['y'] += dy1
            print("Undo Action!")
            count += 1
        else:
            print("You can Undo only 1 time after a move! Keep moving pleasee!")
    else:
        playing = False
    
    if 0 <= player['x'] + dx < map['size_x'] and 0 <= player['y'] + dy < map['size_y']:
        player['x'] += dx
        player['y'] += dy

    for box in boxes:
        # check box trung nhau
        if box['y'] == player['y'] and box['x'] == player['x'] and 0 <= box['x'] + dx < map['size_x'] and 0 <= box['y'] + dy < map['size_y']:
            box['x'] += dx
            box['y'] += dy
            # khong cho phep day 2 box
            if boxes[0] == boxes[1] or boxes[0] == boxes[2] or boxes[2] == boxes[1]:
                player['x'] -= dx
                player['y'] -= dy
                box['x'] -= dx
                box['y'] -= dy
            # khong cho phep day box vao wall
            elif box['y'] == wall['y'] and box['x'] == wall['x']:
                player['x'] -= dx
                player['y'] -= dy
                box['x'] -= dx
                box['y'] -= dy
                print("Oop, walll! :<")
        elif box['y'] == player['y'] and box['x'] == player['x']:
            player['x'] -= dx
            player['y'] -= dy