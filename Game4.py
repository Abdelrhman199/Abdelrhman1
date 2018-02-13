a =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
w=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
b =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
m=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
temp=0
temp1=0
d=[4,8,12]
c=[5,9,13] 
j=0
o=0
c=0
N=0
N1=0
N2=0
c1=0
c2=0
z=16
q="x"
print("WELCOME")
while(True):
 while (True):
            print("Choose Two Numbers To Form A Rectangle") 
            for i in range (0,4,1):
                 while(j<4):
                  print("  |",a[j][c] ,"|",a[j][c+1] ,"|",a[j][c+2] ,"|",a[j][c+3],"|")
                  j=j+1
            c=0
            j=0
            print(b)
            

            print("player one ")
            print("Choose Two numbers") 
            F=int(input())
            S=int(input())
            if(S in b and F in b) :
                if (((S in [5,9,13]) and (F in [4,8,12])) or ((S in[4,8,12]) and (F in [5,9,13]))):
                    while(True):
                        print("Choose Two Numbers Forming a Rectangle")
                        F=int(input())
                        S=int(input())
                        if(((S not in [5,9,13]) or (F not in [4,8,12])) and ((S not in [4,8,12] or F not in [5,9,13]))):
                           break
                    
                if((F-S==1) or (S-F==1)):
                      c1=c1+1
                      N=N+2
                      for k in range(0,4,1):
                        for p in range (0,4,1):
                            if(F==a[k][p]):
                                a[k][p]=q
                                b.remove(F)

                            elif(S==a[k][p]):
                               a[k][p]=q
                               b.remove(S)
                      z=z-2       
             
                elif((F-S==4) or (S-F==4)):
                        c1=c1+1
                        N=N+2 

                        for k in range(0,4,1):
                         for p in range (0,4,1):
                            if(F==a[k][p]):
                                a[k][p]=q
                                b.remove(F)

                            if(S==a[k][p]):
                               a[k][p]=q
                               b.remove(S)
                        z=z-2       
         
                elif((F-S!=1 or S-F!=1) and (F-S!=4 or S-F!=4) ):
                     while(True):

                      if(N<14):
                            print("player one")
                            print("choose another Two Numbers")
                            F=int(input())
                            S=int(input())
                            if(S and F in b) :
                                if (((S in [5,9,13]) and (F in [4,8,12])) or ((S in[4,8,12]) and (F in [5,9,13]))):
                                    while(True):
                                        print("Choose Two Numbers Forming a Rectangle")
                                        F=int(input())
                                        S=int(input())
                                        if(((S not in [5,9,13]) or (F not in [4,8,12])) and ((S not in [4,8,12] or F not in [5,9,13]))):
                                           break
                                if(F-S==1 or S-F==1):
                                 c1=c1+1
                                 N1=N
                                 N1=N1+2
                                 for k in range(0,4,1):
                                  for p in range (0,4,1):
                                   if(F==a[k][p]):
                                       
                                    a[k][p]=q
                                    b.remove(F)

                                   elif(S==a[k][p]):
                                    a[k][p]=q
                                    b.remove(S)
                                 z=z-2       
           
                                    
                                elif((F-S==4) or (S-F==4)):
                                  c1=c1+1
                                  N1=N
                                  N1=N1+2

                                  for k in range(0,4,1):
                                   for p in range (0,4,1):
                                    if(F==a[k][p]):
                                     a[k][p]=q
                                     b.remove(F)

                                    if(S==a[k][p]):
                                     a[k][p]=q
                                     b.remove(S)
                                  z=z-2       
           
                          
                       
                       
                      if(N1>N):
                            break

            elif(S and F not in b):
                while(True): 
                 print ("choose Two numbers from:", b)
                 F=int(input())
                 S=int(input())
                 if (((S in [5,9,13]) and (F in [4,8,12])) or ((S in[4,8,12]) and (F in [5,9,13]))):
                    while(True):
                        print("Choose Two Numbers Forming a Rectangle")
                        F=int(input())
                        S=int(input())
                        if(((S not in [5,9,13]) or (F not in [4,8,12])) and ((S not in [4,8,12] or F not in [5,9,13]))):
                           break
                 if(S and F in b):
                    break
                if((F-S==1) or (S-F==1)):
                      c1=c1+1
                      N=N+2
                      for k in range(0,4,1):
                        for p in range (0,4,1):
                            if(F==a[k][p]):
                                a[k][p]=q
                                b.remove(F)

                            elif(S==a[k][p]):
                               a[k][p]=q
                               b.remove(S)
                      z=z-2       
             
                elif((F-S==4) or (S-F==4)):
                        c1=c1+1
                        N=N+2 

                        for k in range(0,4,1):
                         for p in range (0,4,1):
                            if(F==a[k][p]):
                                a[k][p]=q
                                b.remove(F)

                            if(S==a[k][p]):
                               a[k][p]=q
                               b.remove(S)
                        z=z-2       
         
                elif((F-S!=1 or S-F!=1) and (F-S!=4 or S-F!=4)):
                     while(True):

                      if(N<14):
                            print("player one")
                            print("choose another Two Numbers")
                            F=int(input())
                            S=int(input())
                            if (((S in [5,9,13]) and (F in [4,8,12])) or ((S in[4,8,12]) and (F in [5,9,13]))):
                                while(True):
                                    print("Choose Two Numbers Forming a Rectangle")
                                    F=int(input())
                                    S=int(input())
                                    if(((S not in [5,9,13]) or (F not in [4,8,12])) and ((S not in [4,8,12] or F not in [5,9,13]))):
                                       break
                            if(S and F in b) :
                                if(F-S==1 or S-F==1):
                                 c1=c1+1
                                 N1=N
                                 N1=N1+2
                                 for k in range(0,4,1):
                                  for p in range (0,4,1):
                                   if(F==a[k][p]):
                                       
                                    a[k][p]=q
                                    b.remove(F)

                                   elif(S==a[k][p]):
                                    a[k][p]=q
                                    b.remove(S)
                                 z=z-2       
           
                                    
                                elif((F-S==4) or (S-F==4)):
                                  c1=c1+1
                                  N1=N
                                  N1=N1+2

                                  for k in range(0,4,1):
                                   for p in range (0,4,1):
                                    if(F==a[k][p]):
                                     a[k][p]=q
                                     b.remove(F)

                                    if(S==a[k][p]):
                                     a[k][p]=q
                                     b.remove(S)
                                  z=z-2       
           
                          
                       
                       
                      if(N1>N):
                            break
                
                
                


            if(z>1):
                print("Choose Two Numbers To Form a Rectangle") 
                for l in range (0,4,1):
                         while(o<4):
                           print("  |",a[o][c] ,"|",a[o][c+1] ,"|",a[o][c+2] ,"|",a[o][c+3],"|")
                           o=o+1
                c=0
                o=0
                print("player Two ")
                print("choose Two numbers")
                F1=int(input())
                S1=int(input())
                if(S1 and F1 in b) :
                    if (((S1 in [5,9,13]) and (F1 in [4,8,12])) or ((S1 in[4,8,12]) and (F1 in [5,9,13]))):
                            while(True):
                                print("Choose Two Numbers Forming a Rectangle")
                                F1=int(input())
                                S1=int(input())
                                if(((S1 not in [5,9,13]) or(F1 not in [4,8,12])) and ((S1 not in [4,8,12] or F1 not in [5,9,13]))):
                                   break
                    if((F1-S1==1) or (S1-F1==1)):
                          c2=c2+1
                          N=N+2
                          for h in range(0,4,1):
                            for u in range (0,4,1):
                                if(F1==a[h][u]):
                                    a[h][u]=q
                                    b.remove(F1) 
                                elif(S1==a[h][u]):
                                    a[h][u]=q
                                    b.remove(S1)

                    elif((F1-S1==4) or (S1-F1==4)):
                            c2=c2+1
                            N=N+2
                            for h in range(0,4,1):
                             for u in range (0,4,1):
                                if(F1==a[h][u]):
                                    a[h][u]=q
                                    b.remove(F1) 
                                elif(S1==a[h][u]):
                                   a[h][u]=q
                                   b.remove(S1)

                         
                    elif(((F1-S1!=1) or (S1-F1!=1)) and ((F1-S1!=4) or (S-F1!=4))):
                            while(True): 
                                    if(N<14):
                                     print("player Two ")
                                     print("choose another Two numbers")
                                     F1=int(input())
                                     S1=int(input())
                                     if (((S1 in [5,9,13]) and (F1 in [4,8,12])) or ((S1 in[4,8,12]) and (F1 in [5,9,13]))):
                                        while(True):
                                            print("Choose Two Numbers Forming a Rectangle")
                                            F1=int(input())
                                            S1=int(input())
                                            if(((S1 not in [5,9,13]) or (F1 not in [4,8,12])) and ((S1 not in [4,8,12] or F1 not in [5,9,13]))):
                                               break

                                     if((F1-S1==1) or (S1-F1==1)):
                                                c2=c2+1
                                                N2=N
                                                N2=N2+2
                                                for h in range(0,4,1):
                                                       for u in range (0,4,1):
                                                        if(F1==a[h][u]):
                                                            a[h][u]=q
                                                            b.remove(F1) 
                                                        elif(S1==a[h][u]):
                                                           a[h][u]=q
                                                           b.remove(S1)

                                     elif((F1-S1==4) or (S1-F1==4)):
                                             c2=c2+1
                                             N2=N
                                             N2=N2+2
                                             for h in range(0,4,1):
                                              for u in range (0,4,1):
                                                if(F1==a[h][u]):
                                                    a[h][u]=q
                                                    b.remove(F1) 
                                     elif(S1==a[h][u]):
                                                   a[h][u]=q
                                                   b.remove(S1)
                                    
                                       
                     
                                    if(N2>N):
                                             break
                elif(F1 not in b or S1 not in b):
                    while (True):
                     print("choose Two numbers from:", b)
                     F1=int(input())
                     S1=int(input())
                     if (((S1 in [5,9,13]) and (F1 in [4,8,12])) or ((S1 in[4,8,12]) and (F1 in [5,9,13]))):
                            while(True):
                                print("Choose Two Numbers Forming a Rectangle")
                                F1=int(input())
                                S1=int(input())
                                if(((S1 not in [5,9,13]) or (F1 not in [4,8,12])) and ((S1 not in [4,8,12] or F1 not in [5,9,13]))):
                                   break

                     if(F1 in b and S1 in b):
                         break 
                    if((F1-S1==1) or (S1-F1==1)):
                          c2=c2+1
                          N=N+2
                          for h in range(0,4,1):
                            for u in range (0,4,1):
                                if(F1==a[h][u]):
                                    a[h][u]=q
                                    b.remove(F1) 
                                elif(S1==a[h][u]):
                                    a[h][u]=q
                                    b.remove(S1)

                    elif((F1-S1==4) or (S1-F1==4)):
                            c2=c2+1
                            N=N+2
                            for h in range(0,4,1):
                             for u in range (0,4,1):
                                if(F1==a[h][u]):
                                    a[h][u]=q
                                    b.remove(F1) 
                                elif(S1==a[h][u]):
                                   a[h][u]=q
                                   b.remove(S1)

                         
                    elif(((F1-S1!=1) or (S1-F1!=1)) and ((F1-S1!=4) or (S1-F1!=4))):
                            while(True): 
                                    if(N<14):
                                     print("player Two ")
                                     print("choose another Two numbers")
                                     F1=int(input())
                                     S1=int(input())
                                     if (((S1 in [5,9,13]) and (F1 in [4,8,12])) or ((S1 in[4,8,12]) and (F1 in [5,9,13]))):
                                            while(True):
                                                print("Choose Two Numbers Forming a Rectangle")
                                                F1=int(input())
                                                S1=int(input())
                                                if(((S1 not in [5,9,13]) or (F1 not in [4,8,12])) and((S1 not in [4,8,12] or F1 not in [5,9,13]))):
                                                   break

                                  
                                     if((F1-S1==1) or (S1-F1==1)):
                                                c2=c2+1
                                                N2=N
                                                N2=N2+2
                                                for h in range(0,4,1):
                                                       for u in range (0,4,1):
                                                        if(F1==a[h][u]):
                                                            a[h][u]=q
                                                            b.remove(F1) 
                                                        elif(S1==a[h][u]):
                                                           a[h][u]=q
                                                           b.remove(S1)

                                     elif((F1-S1==4) or (S1-F1==4)):
                                            c2=c2+1
                                            N2=N
                                            N2=N2+2
                                            for h in range(0,4,1):
                                              for u in range (0,4,1):
                                                if(F1==a[h][u]):
                                                    a[h][u]=q
                                                    b.remove(F1) 
                                     elif(S1==a[h][u]):
                                                   a[h][u]=q
                                                   b.remove(S1)
                                       
                     
                                    if(N2>N):
                                             break
                 
                
            z=0 
            if (len(b)>0):
                 for s in range(0,len(b),1):
                        for g in range(0,len(b),1):
                         if((b[s]-b[g]==1) or (b[g]-b[s]== 1)):
                             z=z+1
                             break
                         if((b[s]-b[g]==4) or (b[g]-b[s]==4)):
                             z=z+1
                             break
                 print(z) 
                 if(z==0):
                   if (c1>c2):
                    print("player one win!")
                    break
                   elif(c2>c1):
                       
                    print("player Two win!")
                    break
                   elif(c1==c2):
                    print("Draw!")
                   break    
                  
            
      
            elif(len(b)==0): 
                if(c1==c2):
                        print("Draw!")
                break         
                
 print("Press Y To play Again Or press N")
 P=input()
 v="Y"
 L="N"
 temp=w
 a=temp
 temp2=m
 b=m 
 if(P==L):
    break 
