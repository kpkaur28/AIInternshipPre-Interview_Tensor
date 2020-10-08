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

        ##Recurse through the shape to build an empty tensor with zeros
        def initialize(n,first):
            ## n represents index of shape variable recurring backwards
            ## first is a boolean value to check if tensor is initialized before
            if first:
              tensor.append([0] * self.shape[n])
              first = False
            
            else:  
              temp = []
              for i in range(self.shape[n]):
                ## Deep copy gives new object of the same type
                ## rather than references of the object
                temp.append(copy.deepcopy(tensor[0]))    
              tensor.clear()
              tensor.append(temp) 

            if n-1 == -1:
              return
            
            initialize(n-1,first)
        
        initialize((len(self.shape)-1),True)  
        return tensor[0]
    
    ##Fill the data in the empty tensor through recursion
    def fillData(self):
        tensor = self.initializeTensor()
        
        def populate(L):
            ##If the element is not a list, grab the element
            if not isinstance(L[0], list):
                for i in range(len(L)):
                    ##If data array is empty return an empty tensor with zeros
                    if len(self.data) == 0:
                        return
                    L[i] = self.data.pop(0)
                return                
            
            for i in range(len(L)):
                populate(L[i])
            
        populate(tensor)
        return tensor

  
    def printTensor(self):
        print(self.fillData())

data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
shape0 = [2,3,2]
tensor = Tensor(data0, shape0)
data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]
shape1 = [5, 2]
tensor1 = Tensor(data1, shape1)
tensor.printTensor()
tensor1.printTensor()
