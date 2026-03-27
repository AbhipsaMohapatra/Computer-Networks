# VIGNER CIPHER

print("Vigner Cipher")

pt = input("Enter the plain text").strip()
key = input("Enter the key ").strip()
ct=[]
for i in range(len(pt)):
    ct.append(chr((ord(pt[i])-ord('A')+ord(key[i])-ord('A'))%26+ord('A')))
  
   
print("".join(ct))

ct = input("Enter the cipher text").strip()
key = input("Enter the key ").strip()
ans=[]
for i in range(len(ct)):
    ans.append(chr(((ord(ct[i])-ord('A')-ord(key[i])-ord('A'))+26)%26+ord('A')))
  
   
print("".join(ans))
