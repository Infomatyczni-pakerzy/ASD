from queue import PriorityQueue


Q = PriorityQueue()
Q.put((2, (69, 96) ))
Q.put((1, (63, 36) ))
Q.put((6, (6, 2) ))
Q.put((0, (0, 0) ))

while not Q.empty():
    item = Q.get()[1]
    print(item)