import sys
rows=[[0,1,2,3,4,5,6,7,8],
[9,10,11,12,13,14,15,16,17],
[18,19,20,21,22,23,24,25,26],
[27,28,29,30,31,32,33,34,35],
[36,37,38,39,40,41,42,43,44],
[45,46,47,48,49,50,51,52,53],
[54,55,56,57,58,59,60,61,62],
[63,64,65,66,67,68,69,70,71],
[72,73,74,75,76,77,78,79,80]]


cols = [[0,9,18,27,36,45,54,63,72],
[1,10,19,28,37,46,55,64,73],
[2,11,20,29,38,47,56,65,74],
[3,12,21,30,39,48,57,66,75],
[4,13,22,31,40,49,58,67,76],
[5,14,23,32,41,50,59,68,77],
[6,15,24,33,42,51,60,69,78],
[7,16,25,34,43,52,61,70,79],
[8,17,26,35,44,53,62,71,80]]

boxes = [[0,1,2,9,10,11,18,19,20],
[3,4,5,12,13,14,21,22,23],
[6,7,8,15,16,17,24,25,26],
[27,28,29,36,37,38,45,46,47],
[30,31,32,39,40,41,48,49,50],
[33,34,35,42,43,44,51,52,53],
[54,55,56,63,64,65,72,73,74],
[57,58,59,66,67,68,75,76,77],
[60,61,62,69,70,71,78,79,80]]

board = [1, 2, 3, 4, 5, 6, 7, 8, 9,
         'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
         'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
         'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
         'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
         'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
         'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
         'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
         'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']

i = 0


def solved():
    if "b" not in board:
        return True
    else:
        return False


def nextboard(board, i):
    boardlen = len(board)
    while 0 <= i < boardlen:
        if board[i] == "b":
            tofindrow = ([pos for row in rows if i in row for pos in row])
            rownum = rows.index(tofindrow)

            tofindcol = ([pos for col in cols if i in col for pos in col])
            colnum = cols.index(tofindcol)

            tofindbox = ([pos for box in boxes if i in box for pos in box])
            boxnum = boxes.index(tofindbox)

            childboard(board, rownum, colnum, boxnum, i)
        else:
            i = i + 1




def childboard(board, rownum, colnum, boxnum, i):
    indexes = (rows[rownum]) + (cols[colnum]) + (boxes[boxnum])
    nodups = list(set(indexes))
    nodups.remove(i)
    for num in range(1, 10):
        board[i] = num
        if validboard(board, nodups, num) is True:
            i = i + 1
            nextboard(board, i)
        elif num == 9:
            board[i] = "b"
            i = i - 1
            nextboard(board,i)
        else:
            continue


def validboard(board, nodups, num):
    for pos in nodups:
        if board[pos] == num:
            return False
        else:
            continue
    return True






def alltogethernow():
    if solved() is True:
        print("Solved")
        print(board)
    else:
        nextboard(board, i)


alltogethernow()
