UNQ AI Internship Pre-Interview Test Assignment:


Using Python, construct a class without importing any modules (such as numpy) given the following guidelines:
1. Given 2 inputs, data and shape, construct a tensor using nested lists.
2. A tensor is a general term for n-dimension matrix. (order goes scalar, vector, matrix, tensor)
3. Data and shape inputs are given as lists of numbers. Data can be any number (float, int, etc.), but shape needs to be a list of positive integers.
4. Data and shape inputs can be lists of any length.
5. If shape is empty list, the output tensor should also be an empty list
6. The constructed tensor can be saved as an instance variable, printed in standard output, or both.
7. If too many data numbers, cut it off after the tensor fills up. If not enough, pad the tensor w/ zeroes.


Examples:

class Tensor():
  ...
  
  def __init__(self, data, shape):
    self.data = data
    self.shape = shape
    self.tensor = ...

  def shape_data(self, ...):  ## 'shape_data' is an example. feel free to name it whatever you want.
    ...

  ...


>>> data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
>>> shape0 = [2, 3, 2]
>>> tensor0 = Tensor(data0, shape0)

output:
[[[0, 1], [2, 3], [4, 5]], [[0.1, 0.2], [-3, 0], [0, 0]]]



>>> data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]
>>> shape1 = [5, 2]
>>> tensor1 = Tensor(data1, shape1)

output:
[[0, 1], [2, 3], [4, 5], [0.1, 0.2], [-3, -2]]


REMEMBER NOT TO IMPORT ANY MODULES OR LIBRARIES SUCH AS NUMPY OR SCIPY.
