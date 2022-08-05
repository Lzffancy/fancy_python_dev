"""
小明过桥

"""

class FamilyBridge():

    family = {
              'p1s':1,
              'p3s':3,
              'p6s':6,
              'p8s':8,
              'p12s':12,
              }
    def __init__(self):
        self.totall_time = 0

    def across_time(self,x,y):
        one_time = x + y
        self.totall_time += one_time
        if x>y:
            return y
        else:
            return x



if __name__ == '__main__':
    pass
