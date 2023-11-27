import queue as q

q1 = q.Queue(maxsize=3)
print(q1.empty())

q1.put(1)
q1.put(2)
q1.put(3)
print(q1.full())
print(q1.get()) #dequeueing
print(q1.qsize())