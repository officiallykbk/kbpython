l1=[0]
l2=[0]
output=[]
carry=0
if len(l1)!=len(l2):
    print('on')
    minList=min(l1,l2)
    maxlist=max(l1,l2)
    maxListcut=[maxlist[i] for i in range(len(minList))]
    remainder=maxlist[len(minList):]
    result =[list(x) for x in zip(minList,maxListcut)]
else:
    print('off')
    result =[list(x) for x in zip(l1,l2)]
print(result)
for i in result:
    tot=str(sum(i,carry))
    carry=0
    if len(tot)>1:
        output.append(int(tot[1]))
        carry=int(tot[0])
        
    else:
        output.append(int(tot))
if len(remainder)>1:
    for j in remainder:
        tot=str(j+carry)
        carry=0
        if len(tot)>1:
            output.append(int(tot[1]))
            carry=int(tot[0])
            
        else:
            output.append(int(tot))
if carry>0:
    output.append(carry)
print(output)

