


WA = ("A", "S", [])
WB = ("B", "G", [])
WG = ("G", "S", [WA])
WF = ("F", "R", [WB])
WE = ("E", "R", [])
WD = ("D", "H", [])
WC = ("C", "R", [])
WJ = ("J","R",[WE, WF, WG])
WI = ("I", "H", [])
WH = ("H", "S", [WC, WD])
WK = ("K", "G", [WH, WI, WJ])

listofwiz = [WA, WB, WC, WD, WE, WF, WG, WH, WI, WJ, WK]

#wizdic = {WK : ("K", "G", [WH, WI, WJ]), WH:("H", "S", [WC, WD]), WI:("I", "H", []), WJ: ("J","R",[WE, WF, WG]), WC: ("C", "R", []), WD: ("D", "H", []), WE: ("E", "R", []), WF:("F", "R", [WB]), WG: ("G", "S", [WA]), WB : ("B", "G", []),  WA: ("A", "S", [])}



def samehouse():
    for wiz in listofwiz:
        if len(wiz[2]) != 0:
            for child in wiz[2]:
                if child[1] == wiz[1]:
                    print(wiz, child)



(samehouse())




