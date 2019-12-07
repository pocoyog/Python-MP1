import matplotlib.pyplot as plt 
A = list(range(0,100))
B = []
def f():
    for i in range(0,100): 
        C = (i**2)-7
        if i<9:
            B.append(C)
        elif i==9:
            C=0
            B.append(C)
        else:
            while i >=10:
                i = i-10
                if i == 9:
                    C=0 
                    B.append(C)
                elif i<10:
                    C = (i**2)-7
                    B.append(C)
                
    return i
f()

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(color='k', linestyle='-', linewidth=0.5)
plt.stem(A, B, '-', use_line_collection = True) 