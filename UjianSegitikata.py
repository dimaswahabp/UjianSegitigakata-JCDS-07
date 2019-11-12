kata = ('kode python').replace (' ', '')
katList = list(kata)


rules = []
for a in range(len(katList)):
    X = int((a*(a+1))/2)
    rules.append (X)
print (rules)

n=0
if len(katList) not in rules:
    print ('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.')
else:
    n= rules.index(len(katList))
def kiki(n):   
    num = 0
    for i in range(0, n): 
        for j in range(0, i+1): 
            print(katList[num], end=" ")  
            num = num + 1
        print("\r") 
def kuku(n):   
    num = 0
    for i in range(n, 0, -1): 
        for j in range(1, i+1): 
            print(katList[num], end=" ")  
            num = num + 1
        print("\r") 
       
kiki(n)
kuku(n)
