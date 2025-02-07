class Queue:
    def __init__(self):
        self.queue_size = 7
        self.Q = [None] * self.queue_size
        self.head = 1
        self.tail = 1

    def isEmpty(self):
      pass

    def enqueue(self, item):

      self.Q[self.tail-1] = item
      if self.tail == self.queue_size:
        self.tail = 1
      else:
        self.tail += 1
      print(f"enqueuing {item}, head {self.head}, tail {self.tail}")
