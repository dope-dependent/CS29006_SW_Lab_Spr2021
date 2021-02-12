# In this python file, only the definations for the magic functions and the basic operations
# for the question segments are provided. There may be the need to add new functions or overload 
# existing ones as per the question requirements.

class Vector:
        
    def __init__(self, *args): 

        # if arg is an int(dimension)
        if isinstance(args[0], int): 
            self._coords = [0]*args[0]

        # if arg is a list
        if isinstance(args[0], list):
            # Only initialize if all the members are integer
            all_integers = True
            for i in range (0, len(args[0])):
                if not isinstance(args[0][i], int):
                    all_integers = False

            if all_integers: 
                self._coords = args[0]
    
    def __len__(self):
        # return the dimension of the vector
        return int(len(self._coords))

    def __getitem__(self, j):
        # return the jth coordinate of the vector
        return self._coords[j]

    def __setitem__(self, j, val):
        # set the jth coordinate of vector to val
        assert j >= 0 and j < len(self)
        self._coords[j] = val

    def __add__(self, other):
        # u + v
        assert len(other) == len(self)
        final = Vector(len(other))
        for i in range(0,len(other)):
            final[i] = other[i] + self[i]
        
        return final

    def __eq__(self, other):
        # return True if vector has same coordinates as other
        assert len(other) == len(self)
        value = True
        for i in range(0, len(other)):
            if other[i] != self[i]:
                value = False
                break
        return value

    def __ne__(self, other):
        # return True if vector differs from other
        return not self == other
    
    def __str__(self):
        # return the string representation of a vector within <>
        stringlist =  [ str(i) for i in self._coords ]
        final = ",".join(stringlist)
        return "<" + final + ">"

    def __sub__(self, other):
        # returns u - v, solution for question 2
        assert len(other) == len(self)
        final = Vector(len(other))
        for i in range(0,len(other)):
            final[i] = other[i] - self[i]
        
        return final
    
    def __neg__(self):
        # Soln for Qs. 3, returning the negative of a vector
        return Vector(len(self)) - self
    
    def __rmul__(self, value):
        final = Vector(len(self))
        for i in range(0,len(self)):
            final[i] = value*self[i]
        return final 
    
    def __mul__(self, other):
        # Soln for Qs. 4, 5 and 6
        if isinstance(other, int):        # If the vector is multiplied by a constant
            return other*self
        else:
        # Now other is a vector, and it should be of the same dimensions
            assert len(other) == len(self)
            final = 0
            for i in range(0, len(other)):
                final += (self[i]*other[i])
            
            return final
    
def main():
    v1 = Vector(5)
    v2 = Vector (7)
    v4 = Vector([2,3,4,5,6])
    v3 = Vector([1,2,3,4,5])  
    v6 = Vector([1,2,3,4,5])  
    v5 = v3*v4
    print(v5)


if __name__ == '__main__':
    main()