fruit_count = 1
l = [5,3,6,2,4]
size = len(l)
if size <5:
    l.append(fruit_count)
    l.sort(reverse = True)
    position = l.index(fruit_count)
    print(f"Congratulations you are on the top 5 at position {position + 1}")
    

else:
    if fruit_count > min(l):
        l.append(fruit_count)
        l.sort(reverse = True)
        l.pop()
        position = l.index(fruit_count)
        print(f"Congratualations you are on the top 5 at position {position + 1}")
        print("")
    else:
        print(f"You lose, your total points are {fruit_count} and you are not at top 5")

        



