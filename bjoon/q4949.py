
#백준 알고리즘 4949 [균형잡힌 세상]

def fun(str):
    stack=[]
    for s in str:
        if s=='(' or s=='[':
            stack.append(s)
        elif s==')' or s==']':
            if len(stack)==0:
                return('no')
            elif s==')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    return('no')
            elif s==']':
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return('no')
    return 'yes'

list=[]
while True:
    str=input()
    if (str == '.'):
        break
    list.append(str)

for str in list:
    print(fun(str))
