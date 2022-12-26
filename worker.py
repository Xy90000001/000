import time
file =  open('cach.txt','w')
file.write('file')
a = 0
l=[]
while a<=11:
  a+=1
  l.clear()
  l.append(a)
  file1 =  open('cach.txt','w')
  file1.write(str(l))
  time.sleep(2)

  
  
