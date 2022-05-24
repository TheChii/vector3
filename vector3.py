class vector3:
    def __init__(self, *args):
        self.values = []
        for x in args:
            self.values.append(x)
        

    def __str__(self):
        return f'{self.values}'

    def __repr__(self):
        return f"{self.values}"

    def add(self, value):
        for x in range(3):
            self.values[x] += value

    def substract(self, value):
        for x in range(3):
            self.values[x] -= value

    def multiply(self, value):
        for x in range(3):
          self.values[x] *= value

    def divide(self, value):
        for x in range(3):
          self.values[x] /= value

    def swap(self, a, b):
        self.values[a] = self.values[a] ^ self.values[b]
        self.values[b] = self.values[b] ^ self.values[a]
        self.values[a] = self.values[a] ^ self.values[b]

    def sort(self, ascending = True):
        self.values = sorted(self.values, reverse = ascending)
      
    def vmax(self):
        return max(self.values)
    def vmin(self):
        return min(self.values)

    def vsum(self):
        return sum(self.values)
    def vproduct(self):
        p = 1
        for x in range(3):
            p*= self.values[x]
        return p

    def at(self, pos):
        return self.values[pos]

    def to_list(self):
        new_list = []
        for x in self.values:
          new_list.append(x)
        return new_list

    def change(self, val, pos=0):
        if(type(val) == "<class 'list'>"):
          for x in range(pos, len(val)):
            self.values[x] = val[x]
        else:
          self.values[pos] = val
          
    def clear(self):
        self.values = [None, None, None]

    def all(self, value):
      self.values=[value, value, value]
    def zero(self):
      self.values=[0,0,0]


    def distance(self, second):
      dist = pow(pow(self.values[0]-second.values[0], 2) + pow(self.values[1]-second.values[1], 2) + pow(self.values[2] - second.values[2], 2) ,1/2)

      return dist

    def abs(self):
      from ctypes import cdll
      math_lib = cdll.LoadLibrary(r"C:\Users\Theodor\source\repos\qmath\x64\Debug\qmath.dll")
      abs = math_lib.abs
      for x in range(3):
        self.values[x] = abs(self.values[x])
          
    def negative(self):
      for x in range(3):
        if(self.values[x]>0):
            self.values[x] = -self.values[x]

    def inverse(self):
      for x in range(3):
        self.values[x] = -self.values[x]
    
    def magnitude(self):
        from ctypes import cdll
        math_lib = cdll.LoadLibrary(r"C:\Users\Theodor\source\repos\qmath\x64\Debug\qmath.dll")
        sqrt = math_lib.sqrt
        x = self.values[0]
        y = self.values[1]
        z = self.values[2]
        return sqrt(x*x+y*y+z*z)

    def x(self):
        return self.values[0]
    def y(self):
        return self.values[1]
    def z(self):
        return self.values[2]
    
    def up(self, value=1):
        self.values[1]+=value
    def down(self, value=1):
        self.values[1]-=value
    def left(self, value=1):
        self.values[0]-=value
    def right(self,value=1):
        self.values[0]+=value
    def back(self, value=1):
        self.values[2]-=value
    def forward(self, value=1):
        self.values[2]+=value

