a = "bottles of milk on the wall,"
b = "bottles of milk."
c = "Take one down and pass it around,"
d = "No more bottles of milk on the wall, no more bottles of milk."
e = "Go to the store and buy some more,"
f = "bottle of milk on the wall,"
g = "bottle of milk."

def number_of_bottles():
    # https://github.com/RianGallagher/Beginner-projects-solutions/blob/master/99bottles.py
    for i in range(99, 0, -1):
        if(i == 2):
            print("{} bottles of milk on the wall,{} bottles of milk, take one down, pass it around, {} bottle of milk on the wall".format(i, i, i-1))
        elif(i == 1):
            print("{} bottle of milk on the wall,{} bottle of milk.".format(i, i))
            print("Take one down and pass it around, no more bottles of milk on the wall.")
            print("No more bottles of milk on the wall, no more bottles of milk.")
            print("Go to the store and buy some more,{} bottles of milk on the wall.".format(i))
        else:
            print("{} bottles of milk on the wall,{} bottles of milk, take one down, pass it around, {} bottles of milk on the wall".format(i, i, i-1))



number_of_bottles()
