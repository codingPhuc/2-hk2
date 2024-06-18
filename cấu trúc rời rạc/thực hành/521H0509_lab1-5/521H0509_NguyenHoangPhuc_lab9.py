import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def draw(A1, vertexs):
    G1 = nx.from_numpy_array(A1)
    pos = nx.spring_layout(G1)
    nx.draw_networkx(
        G1, pos=pos, with_labels=True, labels={a: b for a, b in enumerate(vertexs)}
    )
    edge_labels = nx.draw_networkx_edge_labels(G1, font_size=8, pos=pos, label_pos=0.5)
    plt.axis("equal")
    plt.show()

#====================Ex1a====================
def mPlus(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise Exception("len A not equal len B")

    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

#====================Ex1b====================
def mMinus(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise Exception("len A not equal len B")
    return [[A[j][i] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

#====================Ex1c====================
def mMultiply(A, B):
    if len(A[0]) != len(B):
        raise Exception("don't multiply matrix")

    C = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(C)):
        for j in range(len(C[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

##====================Ex1d====================
def mTranspose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def toLoE(A):
    n = len(A)
    edgeList = [[] for i in range(n)]
    for i in range(n):
        listTemp = []
        for j in range(n):
            if A[i][j] != 0:
                listTemp.append(j)
        edgeList[i] = listTemp
    return edgeList


# 1a
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]
print("Ex 1a.", mPlus(A, B))
# fig = plt.figure("1a")
# draw(np.array(mPlus(A, B)), "ab")

# 1b
A = [[2, 2], [2, 3]]
B = [[1, 1], [3, 3]]
print("Ex 1b.", mMinus(A, B))
# fig = plt.figure("Ex 1b")
# draw(np.array(mMinus(A, B)), "ab")

# 1c
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]
print("Ex 1c. A x B", mMultiply(A, B))

A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]
print("Ex 1c. B x A", mMultiply(B, A))

# 1d
# A = [[1, 2], [4, 3]]
# print("1d.", mTranspose(A))
# plt.savefig("Ex1d.png")
# draw(np.array(mTranspose(A)), "ab")

# 1e
# A = [[1, 2], [3, 4]]
# B = [[2, 0], [1, 2]]
# print("1e.", mMultiply(A, B))
# print("1e.", mMultiply(B, A))

# 1f
# A = [[1, 4, 6, 10], [2, 7, 5, 3]]
# B = [[1, 4, 6], [2, 7, 5], [9, 0, 11], [3, 1, 0]]
# print("1f.", mMultiply(A, B))

#====================Ex2====================
A = [
    [0, 0, 3, 0, 1],
    [0, 0, 5, 3, 0],
    [3, 5, 0, 1, 0],
    [0, 3, 1, 0, 2],
    [1, 0, 0, 2, 0],
]
fig = plt.figure("Ex 2a")
draw(np.array(A), "abcde")

A = [
    [0, 0, 0, 0, 1, 1],
    [0, 0, 5, 3, 0, 0],
    [0, 5, 0, 1, 0, 0],
    [0, 3, 1, 0, 2, 3],
    [1, 0, 0, 2, 0, 6],
    [1, 0, 0, 3, 6, 0],
]
fig = plt.figure("Ex 2b")
draw(np.array(A), "abcdef")

def getVertexs(lines):
    vertexs = set()
    for source, dest, weight in lines:
        # print(source, dest, weight)
        vertexs.add(source)
        vertexs.add(dest)

    return [v for v in vertexs]

#====================Ex3====================
lines = [
    ("A", "C", 5),
    ("A", "D", 3),
    ("B", "C", 3),
    ("B", "D", 2),
    ("C", "D", 1),
    ("C", "E", 3),
    ("D", "E", 1),
    ("D", "F", 3),
    ("E", "F", 4),
]
vertexs = getVertexs(lines)
vertexs.sort()
alphabet = "".join(vertexs)
mapAlphabet = {alphabet[i]: i for i in range(len(alphabet))}
n = len(alphabet)
A = [[0 for _ in range(n)] for _ in range(n)]
for line in lines:
    A[mapAlphabet[line[0]]][mapAlphabet[line[1]]] = line[2]
fig = plt.figure("Ex 3a")
draw(np.array(A), "abcdef")

lines = [
    ("A", "C", 2),
    ("A", "D", 3),
    ("A", "E", 3),
    ("B", "C", 3),
    ("B", "D", 2),
    ("C", "D", 2),
    ("C", "E", 8),
    ("C", "F", 6),
    ("D", "F", 5),
    ("E", "F", 3),
]
vertexs = getVertexs(lines)
vertexs.sort()
alphabet = "".join(vertexs)
# print(alphabet)
mapAlphabet = {alphabet[i]: i for i in range(len(alphabet))}
n = len(alphabet)
A = [[0 for j in range(n)] for i in range(n)]
for line in lines:
    A[mapAlphabet[line[0]]][mapAlphabet[line[1]]] = line[2]
fig = plt.figure("Ex 3b")
draw(np.array(A), "abcdef")


#====================Ex4====================
A = [
    [0, 0, 0, 0, 1, 1],
    [0, 0, 5, 3, 0, 0],
    [0, 5, 0, 1, 0, 0],
    [0, 3, 1, 0, 2, 3],
    [1, 0, 0, 2, 0, 6],
    [1, 0, 0, 3, 6, 0],
]
print("Ex4")
edgeList = toLoE(A)
for i in range(len(edgeList)):
    print(i, "->", edgeList[i])

##====================Ex5====================
# lists = [
#     "Monkeys",
#     "Apes",
#     "Gorillas",
#     "Primates",
#     "Mice",
#     "Squirrels",
#     "Beavers",
#     "Rodents",
#     "Crocodiles",
#     "Komodo dragons",
#     "Lizards",
#     "Reptiles",
#     "Coconut trees",
#     "Grasses",
#     "Oaks",
#     "Plants",
#     "Mushrooms",
#     "Molds",
#     "Yeasts",
#     "Fungi",
#     "Mammals",
#     "Animals",
#     "Multicellular organisms",
#     "Unicellular organisms",
# ]
# G = nx.Graph()

# # G = nx.

# G.add_nodes_from(lists)
# G.add_edges_from(
#     [("Monkeys", "Primates"), ("Apes", "Primates"), ("Gorillas", "Primates")]
# )
# G.add_edges_from(
#     [("Mice", "Rodents"), ("Squirrels", "Rodents"), ("Beavers", "Rodents")]
# )
# G.add_edges_from(
#     [
#         ("Crocodiles", "Reptiles"),
#         ("Komodo dragons", "Reptiles"),
#         ("Lizards", "Reptiles"),
#     ]
# )
# G.add_edges_from(
#     [("Coconut trees", "Plants"), ("Grasses", "Plants"), ("Oaks", "Plants")]
# )
# G.add_edges_from([("Mushrooms", "Fungi"), ("Molds", "Fungi"), ("Yeasts", "Fungi")])
# G.add_edges_from([("Primates", "Mammals"), ("Rodents", "Mammals")])
# G.add_edges_from(
#     [("Mammals", "Animals"), ("Rodents", "Animals"), ("Reptiles", "Animals")]
# )
# G.add_edges_from(
#     [
#         ("Animals", "Multicellular organisms"),
#         ("Plants", "Multicellular organisms"),
#         ("Mushrooms", "Multicellular organisms"),
#         ("Molds", "Multicellular organisms"),
#     ]
# )
# G.add_edges_from(
#     [
#         ("Yeasts", "Unicellular organisms"),
#         ("Rodents", "Animals"),
#         ("Reptiles", "Animals"),
#     ]
# )

# nx.draw(G, with_labels=True, node_size=10, linewidths=10)
# plt.show()
