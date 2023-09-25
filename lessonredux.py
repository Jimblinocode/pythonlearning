from queue import Queue
stack = Queue()

stack.put(7)
stack.put(55)
stack.put(244)

print(stack.get())
print(stack.get())
print(stack.get())