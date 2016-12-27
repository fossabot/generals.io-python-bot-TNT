
import generals


# 1v1 on north america server
g = generals.Generals('your userid', 'your username', '1v1')

# ffa on eu server
# g = generals.Generals('your userid', 'your username', region='eu')

# private game
# g = generals.Generals('your userid', 'your username', 'your gameid')

for update in g.get_updates():

    # get position of your general
    pi = update['player_index']
    y, x = update['generals'][pi]

    # move units from general to arbitrary square
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if (0 <= y+dy < update['rows'] and 0 <= x+dx < update['cols']
                and update_tile['grid'][y+dy][x+dx] != generals.MOUNTAIN):
            g.move(y, x, y+dy, x+dx)
            break
