
#프로그래밍 3

# def solution(info, query):
#     qlist=[]
#     for q in query:
#         querystr = ''
#         q=q.replace(' and ',' ').split()
#         querystr+=q[0][0]
#         querystr += q[1][0]
#         querystr += q[2][0]
#         querystr += q[3][0]
#         querystr += q[4]
#         qlist.append(querystr)
#
#     ilist=[]
#     for i in info:
#         infostr=''
#         i=i.split()
#         infostr+=i[0][0]
#         infostr += i[1][0]
#         infostr += i[2][0]
#         infostr += i[3][0]
#         infostr += i[4]
#         ilist.append(infostr)
#
#     print(qlist,ilist)
#     result=[]
#     for q in qlist:
#         cnt=0
#         for i in ilist:
#             if (i[0]==q[0] or q[0]=='-') and (i[1]==q[1] or q[1]=='-') and (i[2] == q[2] or q[2] == '-')  and (i[3] == q[3] or q[3] == '-')  and (int(i[4:]) >= int(q[4:])):
#                 cnt+=1
#         result.append(cnt)
#     return result

def solution(info, query):
    cntlist=[]
    resultlist=[]
    for q in query:
        cnt=0
        q = q.replace(' and ', ' ')
        q = q.replace('-','')

        list=q.split()
        result = 0

        for i in info:
            cnt=0
            for n in range(len(list) - 1):
                if i.find(list[n])!=-1:
                    cnt+=1
            if cnt==len(list)-1 and int(list[-1])<=int(i[i.rfind(' '):]):
                result+=1
        resultlist.append(result)
    return resultlist

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))