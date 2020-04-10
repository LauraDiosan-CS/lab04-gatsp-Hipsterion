from math import sqrt

def readData1(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['noNodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(",")
        for j in range(n):
            mat[-1].append(int(elems[j]))
    net["mat"] = mat
    f.close()
    return net

def parseFile(fileName):
    n = 51
    tpl = []
    with open(fileName, "r") as f:
        for line in range(n):
            lineargs = f.readline().split(" ")
            if lineargs[0][0] not in "NCTDE":
                node, x, y = lineargs
                tpl.append((int(node), int(x), int(y)))

    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for pct1 in tpl:
        for pct2 in tpl:
            matrix[pct1[0] - 1][pct2[0] - 1] = dist(pct1[1], pct2[1], pct1[2], pct2[2])
    return matrix

def readData2(fileName):
    f = open(fileName, "r")
    net = {}
    distances = parseFile(fileName)
    net["mat"] = distances
    n = len(distances)
    net["noNodes"] = n
    f.close()
    return net

def dist(x1, y1, x2, y2):
    return round(sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)))





