#----Program finding non dominating set by KUNG ET Al.
import math


#------function to take input and sort according to F1------ 

def initialization():
 twodlist=[]                                                         #to store coordinates of the points
 list1=[]                                                            # to store sorted input according to F1
 n=0                                                                 #to store the size of population
 n=input("Enter the size of population:")
 for i in range(n):                                                  # taking the input
     new=[]
     print "Enter coordinate",i+1
     k1=input("Enter x:")
     k2= input("Enter y:")
     k3=input("Enter z:")
     new.append(k1)
     new.append(k2)
     new.append(k3)
     twodlist.append(new)

 print "The initial population will be:"
 for i in range(n):
    print twodlist[i]
 
 #----to take the values of objective functions----
    
 objx=raw_input("Enter the objective function for fx(max/min):")   # for f1
 objy=raw_input("Enter the objective function for fy(max/min):")   # for f2
 objz=raw_input("Enter the objective function for fz(max/min):")   # for f3
 
 #---sorting according to objective f1-----

 if objx=='max':
      list1=sorted([twodlist[i] for i in range(n)],reverse=True)   #sort in decreasing order
 else:
      list1=sorted(twodlist[i] for i in range(n))                  # sort in increasing order


 rlist=[]                                                          # return all the values to reflect in main
 rlist.append(objx)
 rlist.append(objy)
 rlist.append(objz)
 rlist.append(n)
 rlist.append(list1)
 return rlist


#-----------to divide the sorted list recursively----------
# d contains divided lists

def kung(d,n,rlist):
 result=[]                                                         #to store the final result 
 if n==1:                                                          # if size of population reduces to 1 return it
     return d
# -----dividing the list ------                   
 x=int(math.floor(n/2))                                            # size of top
 y=n-x                                                             # size of bottom
 T=d[0:x]                                                          # 1st half of the sorted list
 B=d[x:]                                                           # 2nd half of the sorted list
#--------calling non dominating function for merging-----
 result=nondominating(kung(T,x,rlist),kung(B,y,rlist),x,y,rlist[0],rlist[1],rlist[2])    
 return result


#----------merging of top and bottom----------

def nondominating(T,B,x,y,objx,objy,objz):
   
    m=[]                                                           # m contains merged list
    m=T                                                            # merge list always contains top
    x=len(T)          
    y=len(B)
   
    for i in range(y):                                             # for bottom
        temp=1                                                     # flag for checking nondominance of ith solution of bottom
        #------loop for top and checking ith solution of bottom against all the values in top----
        for j in range(x):
            if objy=='max' and objz=='max':                  
                if T[j][1]>=B[i][1] and T[j][2]>=B[i][2]:          #checking T dominates B,when objective f2,f3 are max
                    temp=0                                         # top dominates bottom
                    break
            elif objy=='max' and objz=='min':                 
                if T[j][1]>=B[i][1] and T[j][2]<=B[i][2]:          #checking T dominates B,when objective f2 is max,f3 is min
                    temp=0
                    break
            elif objy=='min' and objz=='min':                     
                if T[j][1]<=B[i][1] and T[j][2]<=B[i][2]:          #checking T dominates B,when objective f2 is min,f3 is min
                    temp=0
                    break
            else:                                                  #checking T dominates B,when objective f2 is min,f3 are max
                if T[j][1]<=B[i][1] and T[j][2]>=B[i][2]:
                    temp=0
                    break
        if temp==1:                                                # when top does not dominates bottom
           k=B[i]                                                  # add bottom in the merge list m
           m.append(k)
                   
    return m

                 
def main():
 n=0                                                              # size of population
 result=[]                                                        # contains non dominating set(final result)
 m=[]
 print ' Non-dominating solution'
 list2=initialization()                                           # calling initialization function
 
 n=list2[3]                                                        
 m=list2[4]                                                       # contain sorted list according to f1
 result=kung(m,n,list2)
 print "NON-DOMINATING SOLUTION is:"
 print result
 
if __name__ == '__main__':
 main()
