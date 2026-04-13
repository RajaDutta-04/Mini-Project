import math

# ---------- Square Check ----------
def checkSquare(squarelist, squareIdx,pattern_str):
    idx1 = squarelist[0].find(pattern_str)
    if idx1 == -1:
        return 0

    for i, el in enumerate(squarelist):
        if el.find(pattern_str) != idx1:
            print("Horizontal line at row:", squareIdx[i])
            return 0

    return 1


# ---------- Pattern Detection ----------
def pattern(rowCheck, rowIdx, colCheck, colIdx,pattern_str):

    if not rowIdx and not colIdx:
        print("No Pattern Detected")
        return

    if len(rowIdx) == 1 and rowCheck[0].find(pattern_str) != -1:
        print("Horizontal line at index:", rowIdx[0])

    if len(colIdx) == 1 and colCheck[0].find(pattern_str) != -1:
        print("Vertical line at index:", colIdx[0])

    count = 1
    squarelist = [rowCheck[0]] if rowCheck else []
    squareIdx = [rowIdx[0]] if rowIdx else []

    for i in range(len(rowIdx) - 1):

        if rowIdx[i] + 1 == rowIdx[i+1]:
            count += 1
            squarelist.append(rowCheck[i+1])
            squareIdx.append(rowIdx[i+1])

            if count == len(pattern_str):
                if checkSquare(squarelist, squareIdx,pattern_str):
                    print("Square Detected at rows:", squareIdx)

                # Sliding window
                count -= 1
                squarelist.pop(0)
                squareIdx.pop(0)

        else:
            print("Horizontal line at row:", rowIdx[i])
            count = 1
            squarelist = [rowCheck[i+1]]
            squareIdx = [rowIdx[i+1]]


# ---------- Runs Test ----------
def is_non_random(el):
    n1 = el.count('1')
    n2 = el.count('0')
    length = len(el)
    if n1 == 0 or n2 == 0:
        return True if n2 == 0 else False

    runs = 1
    for i in range(1, len(el)):
        if el[i] != el[i-1]:
            runs += 1

    return (runs / len(el) < 0.5) and (n1 >= n2 and n1 >= length//2)


def checkRandomness(data_list, rowCheck, rowIdx, colCheck, colIdx,pattern_str):
    print("----------------Row Wise Runs Test-----------------")

    for i, el in enumerate(data_list):
        print(el)

        if is_non_random(el):
            if(el.find(pattern_str) != -1):
                print("Non-Random")
                rowCheck.append(el)
                rowIdx.append(i+1)
        else:
            print("Random")

    print("-------------------------x--------------------------")
    print("----------------Column Wise Runs Test-----------------")

    # Efficient transpose
    i = 0
    cols = len(data_list[0])
    rows = len(data_list)
    TransList = []
    while i < cols:
        newlist = []
        for el in data_list:
            newlist.append(el[i])
        i+=1
        TransList.append(newlist)
    for i in range(0,len(TransList)):
        num = ''
        for j in range(0,len(TransList[i])):
            num += TransList[i][j]
        TransList[i] = num

    for i, el in enumerate(TransList):
        print(el)

        if is_non_random(el):
            if(el.find(pattern_str) != -1):
                print("Non-Random")
                colCheck.append(el)
                colIdx.append(i+1)
        else:
            print("Random")

    print("-------------------------x--------------------------")


# ---------- MAIN ----------
data_list = []
rowCheck = []
rowIdx = []
colCheck = []
colIdx = []

with open("output.txt", "r") as f:
    data_list = [line.strip() for line in f]

length = len(data_list[0])
pattern_str = ''
for i in range(0,length//2): #We consider atleast 50% length of 1s
    pattern_str += '1'

checkRandomness(data_list, rowCheck, rowIdx, colCheck, colIdx,pattern_str)

print("Rows:", rowCheck)
print("Row Indices:", rowIdx)
print("Cols:", colCheck)
print("Col Indices:", colIdx)

pattern(rowCheck, rowIdx, colCheck, colIdx,pattern_str)