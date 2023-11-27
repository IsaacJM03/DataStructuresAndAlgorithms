from multiprocessing import Queue

customQueue = Queue(maxsize=5)
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
customQueue.put(4)
customQueue.put(5)
print(customQueue.get()) #peeking