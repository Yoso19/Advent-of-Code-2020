def conway_cubes():
    with open('day17.txt') as flat_region_file:
        lines = [line.strip() for line in flat_region_file.readlines()]

    cycles = 6
    active = []
    for j in range(len(lines)):
        for i in range(len(lines[0])):
            if lines[j][i] == '#':
                active.append((j,i,0,0))

    for i in range(6):
        to_activate = []
        to_deactivate = []
        for y in range(-6, 14):
            for x in range(-6, 14):
                for z in range(-7,8):
                    for w in range(-7,8):
                        alive = check(y,x,z,w,active)
                        if (y,x,z,w) not in active:
                            if alive == 3:
                                to_activate.append((y,x,z,w))
                        else:
                            if not (alive == 2 or alive == 3):
                                to_deactivate.append((y,x,z,w))
        for cell in to_deactivate:
            active.remove(cell)
        active.extend(to_activate)

    print(len(active))

def check(x,y,z,w,active):
    alive = 0
    for x_ in range(x-1,x+2):
        for y_ in range(y-1,y+2):
            for z_ in range(z-1,z+2):
                for w_ in range(w-1,w+2):
                    if (x_,y_,z_,w_) in active and (x_,y_,z_,w_) != (x,y,z,w):
                        alive += 1
    return alive


if __name__ == '__main__':
    conway_cubes()