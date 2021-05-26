
f1 = open('krishna.txt','r')
f2 = open('krishna1.txt','w')
f3 = open('IITGN.png','rb')
f4 = open('IIT.png','wb')
for i in f1:
    f2.write(i)

f2 = open('krishna1.txt','ab')

for i in f3:
    f4.write(i)
