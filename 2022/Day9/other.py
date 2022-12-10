DirectionList = []
with open("input/input.txt", "r") as data:
    for t in data:
        Line = t.strip().split()
        A, B = Line
        NewTuple = (A, int(B))
        DirectionList.append(NewTuple)

DirectionDict = {"U": (0,1), "D": (0,-1), "L": (-1,0), "R": (1,0)}
HeadLocation = (0,0)
TailLocation = (0,0)
TailBeenSet = set()
TailBeenSet.add((0,0))
for D, N in DirectionList:
    dx, dy = DirectionDict[D]
    for n in range(N):
        HX, HY = HeadLocation
        TX, TY = TailLocation
        HX, HY = HX+dx, HY+dy
        if abs(HX-TX) >= 2 or abs(HY-TY) >= 2:
            TailLocation = HeadLocation
            TailBeenSet.add(TailLocation)
        HeadLocation = (HX, HY)

Part1Answer = len(TailBeenSet)

KnotList = []
for t in range(10):
    KnotList.append((0,0))

TailBeenSet.clear()
TailBeenSet.add((0,0))

for D, N in DirectionList:
    dx, dy = DirectionDict[D]
    for n in range(N):
        HX, HY = KnotList[0]
        HX, HY = HX+dx, HY+dy
        KnotList[0] = (HX,HY)
        for k in range(9):
            HX, HY = KnotList[k]
            TX, TY = KnotList[k+1]
            if abs(HX-TX) >= 2 or abs(HY-TY) >= 2:
                tdx, tdy = 1,1
                if HX-TX == 0:
                    tdx = 0
                elif HX-TX < 0:
                    tdx = -1
                if HY-TY == 0:
                    tdy = 0
                elif HY-TY < 0:
                    tdy = -1
                TX, TY = TX+tdx, TY+tdy
                KnotList[k+1] = (TX,TY)
                if k == 8:
                    TailBeenSet.add((TX,TY))

Part2Answer = len(TailBeenSet)

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")