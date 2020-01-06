A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"

h1 = {A:[B], B:[C], C:[A]}
h2 = {A: [B, D], B: [C, E], C: [B], D: [E], E: [A, F], F: []}

def reachable(house, room):
    accessablerooms = house.get(room)
    return len(accessablerooms)

print(reachable(h2,B))
most = 0

def mostex(house):
    for room in h2:
        no = reachable(h2,room)
        if no > most:
            best = [room]
        elif no == most:
            best.append(room)

    return best


print(mostex(h2))

def maxto(house):
    maxtodic = {}
    exitsto = house.values()
    newexits = []
    for room in exitsto:
        newexits = newexits + room
    for key in newexits:
        if key not in maxtodic:
            maxtodic[key] = 1
        else:
            maxtodic[key] = maxtodic[key] + 1
    nu = 0
    for item in maxtodic:
        if maxtodic[item] > nu:
            nu = maxtodic[item]
            mostest = [item]
        elif maxtodic[item] == nu:
            mostest.append(item)
    return mostest

print(maxto(h2))


