c1="~"
c2="!"
def draw_1d(n,char):
    return n*char
star_num= draw_1d(c2,8)
print(star_num)

for i in range(6):
    print("*"*10)

def draw_2d(n,m,char):
    for i in range(n):
        print(char*m)
def special_draw_2d(n,m,border,fill):
    print(border*m)
    for x in range(n-2):
        print(border+(fill*(m-2))+border)
    print(border*m)
def fib(n):
    

        
    
    





