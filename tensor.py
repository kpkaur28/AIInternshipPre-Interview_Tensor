import copy

class Tensor:
    def __init__(self, data, shape):
        self.data = data
        self.shape = shape

    def initializeTensor(self):
        tensor = []
        
        ##Corner case: If shape is empty list, we return an empty tensor
        if len(self.shape) == 0: 
            return tensor
    
        def rec(n,first):
            if first:
              temp = [0] * self.shape[n] 
              first = False
              tensor.append(temp)
            else:  
              te = []
              for i in range(self.shape[n]):
                tp = copy.deepcopy(tensor[0])
                te.append(tp)
              tensor.clear()
              tensor.append(te) 

            if n-1 == -1:
              return
            rec(n-1,first)
        
        rec((len(self.shape)-1),True)  
        return tensor[0]
    
    def fillData(self):
        tensor = self.initializeTensor()
        
        def dfs(L, counter):
            if counter == -1:
                return
            if not isinstance(L[0], list):
                for i in range(len(L)):
                    
                    if len(self.data) == 0:
                        return
                    L[i] = self.data.pop(0)
                return                
            
            for i in range(len(L)):
                dfs(L[i],counter-1)
            
        dfs(tensor, len(self.shape)-1)
        return tensor

  
    def printTensor(self):
        print(self.fillData())

data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
shape0 = [2,3,2]
data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]
shape1 = [5, 2]
tensor = Tensor(data0, shape0)

tensor.printTensor()
