def main():
    x = 0
    y = 0
    x1 = 0
    y1 = 0
    grid_number = [x, y]
    grid = [grid_number]
    file = open("movement_input.txt", "r")
    movement = file.readline()
    file.close()
    
    for move in range(0, len(movement), 2):
        if(movement[move] == "\n"):
            break
        
        santa_move = movement[move]
        robot_move = movement[move + 1]
        if(santa_move == ">"):
            x+=1
        elif(santa_move == "<"):
            x-=1
        elif(santa_move == "^"):
            y+=1
        elif(santa_move == "v"):
            y-=1

        if(robot_move == ">"):
            x1+=1
        elif(robot_move == "<"):
            x1-=1
        elif(robot_move == "^"):
            y1+=1
        elif(robot_move == "v"):
            y1-=1

        if(grid.count([x, y]) == 0):
            grid.append([x , y])

        if(grid.count([x1, y1]) == 0):
            grid.append([x1 , y1])

    
    print(f"The amount of houses visited by santa and robosanta is {len(grid)}.")


if __name__ == "__main__":
    main()
