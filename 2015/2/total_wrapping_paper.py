import pdb

def main():
    file = open("wrapping paper.txt", "r")
    boxes = file.readlines()
    file.close()

    total_wrapping_paper = 0
    feet_of_ribbon = 0
    for box in boxes:
        box = box.split('x')

        # turn the box into ints
        box = list(map(int, box))
        
        # [ l*w, w*h, l*h ]
        elements = [box[0] * box[1], box[1] * box[2], box[0] * box[2]]

        # slack is smallest element
        elements.sort()

        total = (2 * elements[0] + 2 * elements[1] + 2 * elements[2]) + elements[0]

        total_wrapping_paper += total

        box.sort()
        
        ribbon_wrap = box[0] * 2 + box[1] * 2
        ribbon_bow = box[0]*box[1]*box[2]
        
        feet_of_ribbon += ribbon_wrap + ribbon_bow
        
    print(f"The amount of wrapping paper needed is {total_wrapping_paper} square feet, the amount of ribbon needed is {feet_of_ribbon} feet.")    


if __name__ == "__main__":
    main()
