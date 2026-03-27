key = input("Enter Key text").upper().replace('J','I')

uniqueq=[]
for i in key:
    if i not in uniqueq:
        uniqueq.append(i)
plainText = input("Enter palin text ").strip()
alpha=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in uniqueq:
    if(i in alpha):
        alpha.remove(i)


t=0
k=0
mat=list()
for i in range(1,6):
    temp=list();
    for i in range(1,6):
        if(t<len(uniqueq)):
            
            temp.append(uniqueq[t])
            t+=1
        elif(k<len(alpha)):
            temp.append(alpha[k])
            k+=1
    mat.append(temp)        
            


print("The matrix is ",mat,end="\n")

shuffle=list()
i=0
l=len(plainText)-1
while(i<l):
    s=[]
    if(plainText[i]!=plainText[i+1]):
        s.append(plainText[i])
        s.append(plainText[i+1])
        i+=2
    elif(plainText[i]!='X'):
        s.append(plainText[i])
        s.append('X')
        i+=1
    else:
        s.append(plainText[i])
        s.append('Z')
        i+=1
    shuffle.append(s)    
        
        
if(i==l):
    s=[]
    val=plainText[len(plainText)-1]
    if(val=='Z'):
        s.append('X')
        s.append('Z')
    else:
        s.append(val)
        s.append('Z')
    
    shuffle.append(s)  
print("The pairs formed is ",shuffle,end="\n")



# encryption

def findPos(ch,mat):
    for i in range(0,5):
        for j in range(0,5):
            if(mat[i][j]==ch):
                return i,j

cipher=""
for pair in shuffle:
    a,b=pair[0],pair[1]
    r1,c1=findPos(a,mat)
    r2,c2=findPos(b,mat)

    if(r1==r2):
        cipher+=mat[r1][(c1+1)%5]
        cipher+=mat[r1][(c2+1)%5]
    elif(c1==c2):
        cipher+=mat[(r1+1)%5][c1]
        cipher+=mat[(r2+1)%5][c2]
    else:
        cipher += mat[r1][c2]
        cipher += mat[r2][c1]
print(cipher)        

# decryption

key = input("Enter Key text").upper().replace('J','I')

uniqueq=[]
for i in key:
    if i not in uniqueq:
        uniqueq.append(i)
cipherText = input("Enter cipher text ").strip()
alpha=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in uniqueq:
    if(i in alpha):
        alpha.remove(i)


t=0
k=0
mat=list()
for i in range(1,6):
    temp=list();
    for i in range(1,6):
        if(t<len(uniqueq)):
            
            temp.append(uniqueq[t])
            t+=1
        elif(k<len(alpha)):
            temp.append(alpha[k])
            k+=1
    mat.append(temp)        
            


print("The matrix is ",mat,end="\n")


shuffle=list()
i=0
l=len(cipherText)-1
while(i<l):
    s=[]
    if(cipherText[i]!=cipherText[i+1]):
        s.append(cipherText[i])
        s.append(cipherText[i+1])
        i+=2
    elif(plainText[i]!='X'):
        s.append(cipherText[i])
        s.append('X')
        i+=1
    else:
        s.append(cipherText[i])
        s.append('Z')
        i+=1
    shuffle.append(s)    
        
        
'''if(i==l):
    s=[]
    val=cipherText[len(cipherText)-1]
    if(val=='Z'):
        s.append('X')
        s.append('Z')
    else:
        s.append(val)
        s.append('Z')
    
    shuffle.append(s) ''' 
print("The pairs formed is ",shuffle,end="\n")

plain=""
for pair in shuffle:
    a,b=pair[0],pair[1]
    r1,c1=findPos(a,mat)
    r2,c2=findPos(b,mat)

    if(r1==r2):
        plain+=mat[r1][(c1-1)%5]
        plain+=mat[r1][(c2-1)%5]
    elif(c1==c2):
        plain+=mat[(r1-1)%5][c1]
        plain+=mat[(r2-1)%5][c2]
    else:
        plain+= mat[r1][c2]
        plain+= mat[r2][c1]
if(plain[-1]=='X' or plain[-1]=='Z'):
    print(plain[0:-1:1])




