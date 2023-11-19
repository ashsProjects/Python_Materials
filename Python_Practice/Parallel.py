global a
a = [3,4,2,8]
global b
b = [1,4,2,3]
global case
c = [0,0,0,0]

def foo1(A,B):
    C = [0]*len(A)
    for i in range(len(A)):
        C[i] = A[i]*B[i]
    return C
def foo2(A,B):
    C = 0
    for i in range(len(A)):
        C += A[i]*B[i]
    return C
def foo3(A,B):
    C = [0]*len(A)
    C[0] = A[0] * B[0]
    for i in range(1, len(A)):
        C[i] = C[i-1] + A[i]*B[i]
    return C

def bar1(s, e):
    if s==e:
        c[s] = a[s]*b[s]
        return
    mid = (e+s)//2
    bar1(s, mid)
    bar1(mid+1, e)
    for i in range(mid+1, e):
        c[i] = c[i] + c[0]
    return c
def bar2(s,e):
    if s==e:
       c[s] = a[s]*b[s]
       return
    mid = (e+s)//2
    bar2(s, mid)
    bar2(mid+1, e)
    return c
def bar3(s,e):
    if s==e:
        c[s] = c[s] + a[s]*b[s]
        return
    mid = (e+s)//2
    bar3(s, mid)
    bar3(mid+1, e)
    c[s] = c[s] + c[mid+1]
    return c


if __name__ == '__main__':
    A = [3,4,2,8]
    B = [1,4,2,3]
    
    print(f'foo1: {foo1(A,B)}')
    print(f'foo2: {foo2(A,B)}')
    print(f'foo3: {foo3(A,B)}')
    
    print(f'bar1: {bar1(0,3)}')
    print(f'bar2: {bar2(0,3)}')
    print(f'bar3: {bar3(0,3)}')
    