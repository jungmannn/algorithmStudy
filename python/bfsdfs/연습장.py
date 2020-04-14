from queue import Queue
q = Queue()

q.put((1, 0))

i, j = q.get()

print(i)
print(j)