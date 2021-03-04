class Queue:

    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)


    def dequeue(self):
        return self.data.pop(0)


    def is_empty(self):
        return not bool(len(self.data))



    # 삭제 없이 단순히 맨 뒤의 data 값을 리턴
    def get_rear(self):
        if self.is_empty():
            return None
        else:
            return self.data[-1]

    # 삭제 없이 단순히 맨 앞의 data 값을 리턴
    def get_front(self):
        if self.is_empty():
            return None
        else:
            return self.data[0]

    def __repr__(self):
        return ''.format(self.data)

q = Queue()
q.enqueue(1) # q.data = [1]
print(q.data)
q.enqueue(2) # q.data = [1, 2]
print(q.data)
q.get_front() # 1
print(q.get_front())
q.get_rear() # 2
print(q.get_rear())
q.dequeue() # 1, q.data = [2]
print(q.data)
q.dequeue() # 2, q.data = []
print(q.get_rear())