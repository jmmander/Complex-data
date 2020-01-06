
arthur = "Arthur"
bill = "Bill"
charlie = "Charlie"
percy = "Percy"
fred = "Fred"
george = "George"
ron = "Ron"
ginny = "Ginny"
victoire = "Victorie"
rose = "Rose"
hugo = "Hugo"
james = "James"
albus = "Albus"
lily = "Lily"


family = [arthur, bill, charlie, percy, fred, george, ron, ginny, victoire, rose, hugo, james, albus, lily]
root = []
gen2 = []
gen3 = []

hered = {arthur: [bill, charlie, percy, fred, george, ron, ginny], bill: [victoire], ron: [rose, hugo], ginny: [james, albus, lily]}
patronus = {arthur: "weasel", bill: "Non-corporeal", charlie: "Non-corporeal", percy: "Non-corporeal", fred: "magpie", george: "magpie", george: "magpie", ron: "jack russel", ginny: "horse"}
wands = {charlie: "ash", ron: "willow", ginny: "yew"}

def findgen():
    for member in family:
        children = hered.values()
        allchild = []
        for sublist in children:
            for item in sublist:
                allchild.append(item)
        if member not in allchild:
            root.append(member)
            gen2 = hered.get(member)
    gen3 = list(set(family) - set(gen2) - set(root))
    return root, gen2, gen3

print(findgen())









