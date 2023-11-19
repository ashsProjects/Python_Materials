
class Polynomial:
    zero=0
    
    # coef is a list of coefficients
    # creates a polynomial of degree n-1
    def __init__(self,coef):
        self.coef=coef
        self.n=len(self.coef)
    
    # tostring
    def __repr__(self):
        return f"Polynomial: {self.n} {self.coef}"

    # overloads [] operator (allows indexing and slicing of coef list)
    # e.g. `poly[i]` or `poly[i:j]`
    def __getitem__(self,i):
        return self.coef[i]

    # overloads (==) operator
    # e.g. `poly1==poly2` or `poly1!=poly2`
    def __eq__(self,other):
        if not isinstance(other,self.__class__) or self.n!=other.n:
            return False
        eq_coef = [self[i]==other[i] for i in range(self.n)]
        return all(eq_coef)
    
    # overloads (+) operator
    # e.g. `poly1+poly2`
    # poly1 and poly must be same length
    def __add__(self,other):
        assert(isinstance(other,self.__class__))
        assert(self.n==other.n)

        #Implement addition for two polynomials of the same length
        add_coef = []
        for i in range(self.n):
            add_coef.append(self.coef[i]+other.coef[i])
        
        return self.__class__(add_coef)

    # overloads (-) operator
    # e.g. `poly1-poly2`
    # poly1 and poly2 must be same length
    def __sub__(self,other):
        assert(isinstance(other,self.__class__))
        assert(self.n==other.n)

        #Implement subtraction for two polynomials of the same length
        sub_coef = []
        for i in range(self.n):
            sub_coef.append(self.coef[i]-other.coef[i])
        
        return self.__class__(sub_coef)
 
    # overloads (*) operator
    # e.g. `poly1*poly2`
    # poly1 and poly2 must be same length, and length must be power of 2
    def __mul__(self,other):
        assert(isinstance(other,self.__class__))
        assert(self.n==other.n)
        
        if self.n==1:
            base_coef = self.coef[0]*other.coef[0]
            
            #implement base case
            return self.__class__([base_coef])

        assert(self.n%2==0)
        n=self.n
        half=self.n//2

        #assign the correct values to {a,b,c,d}_coef
        a_coef=self.coef[:half]
        b_coef=self.coef[half:]
        c_coef=other.coef[:half]
        d_coef=other.coef[half:]

        a=self.__class__(a_coef)
        b=self.__class__(b_coef)
        c=self.__class__(c_coef)
        d=self.__class__(d_coef)

        #implement Karatsuba's algorithm using a,b,c,d
        first_sub = a*c
        second_sub = b*d
        third_sub = (a+b)*(c+d)-first_sub-second_sub
        
        mul_coef_len= (2*self.n)-1

        mul_coef=[self.__class__.zero for i in range(mul_coef_len)]

        #combine results of Karatsuba's algorithm to compute mul_coef
        for i in range(first_sub.n):
            mul_coef[i] += first_sub[i]
            mul_coef[i + half] += third_sub[i]
            mul_coef[i + 2 * half] += second_sub[i]
        
        return self.__class__(mul_coef)

    # O(n^2) implementation of polynomial multiplication
    # use for testing
    def convolution(self,other):
        assert(isinstance(other,self.__class__))
        assert(self.n==other.n)

        n=self.n
        
        mul_coef=[self.__class__.zero for i in range(2*n-1)]
        for i in range(n):
            for j in range(i+1):
                mul_coef[i]+=self[j]*other[i-j]
        for i in range(n,2*n-1):
            for j in range(i-n+1,n):
                mul_coef[i]+=self[j]*other[i-j]
            
        return self.__class__(mul_coef)

    def test_mul(self,other):
        assert(isinstance(other,self.__class__))
        assert(self.n==other.n)

        conv=self.convolution(other)
        mul=self*other

        assert conv==mul, f"convolution and __mul__ are not equal on inputs:\n  p: {self}\n  q: {other}\n  conv:  {conv}\n  mul:   {mul}"

if __name__=="__main__":
    p=Polynomial([1,2,3,4])
    q=Polynomial([3,4,5,6])

    print(p*q)
    Polynomial.test_mul(p,q)
