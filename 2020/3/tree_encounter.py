
def main():
    file = open("geography_input.txt", "r")
    geography_map = file.readlines()

    geography_map = list(map(lambda x: x.strip(), geography_map))

    slope1 = tree_encountered(1, 1, geography_map)
    slope2 = tree_encountered(3, 1, geography_map)
    slope3 = tree_encountered(5, 1, geography_map)
    slope4 = tree_encountered(7, 1, geography_map)
    slope5 = tree_encountered(1, 2, geography_map)
    sum_slope = slope1*slope2*slope3*slope4*slope5
    print(f"The amount of trees discovered on slope 2 is {slope2}, the amount of trees discovered via the multiplication of all slopes is {sum_slope}.")
    

def tree_encountered(width, height, geo_map):
    x = 0
    tree_encountered = 0
    for line in range(0, len(geo_map), height):
        if geo_map[line][x] == '#':
            tree_encountered += 1
        x += width
        if x >= len(geo_map[line]):
            x -= len(geo_map[line])

    return tree_encountered
        


if __name__ == "__main__":
    main()
