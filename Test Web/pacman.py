from random import choice

map = {
    "size_x": 4,
    "size_y": 4
}

players = [
    { "x":1, "y":1}
]

foods = [
    {"x": 0,"y": 0},
    {"x": 1,"y": 0},
    {"x": 0,"y": 1}
]

ghostes = [
    {"x": 3,"y": 0},
    {"x": 3,"y": 3}
]

playing = True
while playing:
    # print map
    for y in range(map['size_y']):
        for x in range(map['size_x']):

            player_is_here = False
            for player in players:
                if y == player['y'] and x == player['x']:
                    player_is_here = True

            food_is_here = False
            for food in foods:
                if y == food['y'] and x == food['x']:
                    food_is_here = True

            ghost_is_here = False
            for ghost in ghostes:
                if y == ghost['y'] and x == ghost['x']:
                    ghost_is_here = True

            if player_is_here:
                print("P ", end='')
            elif ghost_is_here:
                print("G ", end='')
            elif food_is_here:
                if ghost_is_here:
                    print("G ", end='')
                else:
                    print("F ", end='')
            else:
                print("_ ", end='')
        print()
    # end of print map

    # check win
    win = True
    if len(foods) != 0:
        win = False

    if win:
        print("YOU WIN!!")
        break
    
    # check lose
    lose = False
    if len(players) == 0:
        lose = True

    if lose:
        print("YOU LOSE!!")
        break

    dx = 0
    dy = 0

    move = input("Your next move: ").upper()
    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1
    else:
        playing = False

    # Ghost move random
    dx_ghost = 0
    dy_ghost = 0

    dx_ghost = choice(range(-(map['size_x'] - 1),map['size_x'] - 1))
    dy_ghost = choice(range(-(map['size_y'] - 1),map['size_y'] - 1))

    for ghost in ghostes:
        if 0 <= ghost['x'] + dx_ghost < map['size_x'] and 0 <= ghost['y'] + dy_ghost < map['size_y'] and {"x": ghost['x'] + dx_ghost,"y": ghost['y'] + dy_ghost} not in ghostes:
            ghost['x'] += dx_ghost
            ghost['y'] += dy_ghost

    for player in players:
        if 0 <= player['x'] + dx < map['size_x'] and 0 <= player['y'] + dy < map['size_y']:
            player['x'] += dx
            player['y'] += dy

    for food in foods:
        if food['y'] == player['y'] and food['x'] == player['x']:
            foods.remove(food)

    for player in players:
        if player['y'] == ghost['y'] and player['x'] == ghost['x']:
            players.remove(player)