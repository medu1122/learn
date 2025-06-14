class QueueStack:
    def __init__ (self):
            self.input_stack = []
            self.output_stack = []

    def enqueue(self,item):
        self.input_stack.append(item)
    
    def dequeue(self):
        if not self.output_stack:
            if not self.input_stack:
                raise IndexError('Queue is empty') 
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop()
    
q = QueueStack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
    