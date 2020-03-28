class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.data =[0]*size
        self.size = size
        self.head = -1
        self.tail = -1
        self.res = 0

    def next(self, val: int,) -> float:
        # //如果数据流为空
        if self.head ==-1:
            self.head=0
            self.tail=(self.tail+1)%self.size
            self.data[self.tail] = val
            self.res = val
            return self.res
        # //如果队列已满
        if (self.tail+1)%self.size ==self.head:
            self.head = (self.head+1)%self.size
            self.tail =(self.tail+1)%self.size
            self.data[self.tail] = val
            self.res = sum(self.data)/self.size
            return self.res
        self.tail =(self.tail+1)%self.size
        self.data[self.tail] = val
        self.res = sum(self.data)/(self.tail-self.head+1)
        # res=0
        # for i in range(0, len(self.data)):
        #     res +=self.data[i]
        # self.res = res/i
        return self.res