for i in range(1 ,10, 3):   # (start, stop, [step]), if step omitted, defaults to 1
    print(i)                # print 1, then print 1+step = 4
    if (i ==4):
        break               # stop when 4 is reached.
      
for i in range(1 ,20, 3):   # (start, stop, [step]), if step omitted, defaults to 1
    print(i)                # print 1, then print 1+step = 4, then 1+(2*step)=9, then 1+(3*step)=10,
                            # then 1+(4*step)=13, then 1+(5*step)=16, then 1+(6*step)=19        
    if (i ==30):
        break               # stop when 4 is reached.
