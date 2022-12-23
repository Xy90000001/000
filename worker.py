a = 0
l=[]
while a<=11:
  a+=1
  l.clear()
  l.append(a)
  file =  open('cach.txt','w')
  file.write(str(l))

  
  
