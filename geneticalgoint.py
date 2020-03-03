# Program on genetic algorithm to find the maximum value of f(x)=x in integer.
# By : Group 11
#      Name : Ruchika Garg    Roll no. 37  
#      Name : Shipra Kanojia  Roll no. 39	
#      Name : Shruti Singhal  Roll no. 41	






from random import random,randint                          
import math



#................Initializing the population.............
def initializtion(twodlist,b,n):                      
  b=input(" Enter no of bits: ")                      # b is no. of bits of each member
  n=input(" Enter size of population: ")              # n is the size of the population
  new=[]
  rlist=[]
  for i in range(n):
    for j in range(b):
      r=randint(0,1)                                  # generating population randomly in binary form
      new.append(r)
    twodlist.append(new)                              # storing in variable list named twodlist
    new=[]

  print ' Initial population: '                       # printing initial population
  for k in range(n):
    print twodlist[k]
  rlist.append(twodlist)
  rlist.append(b)
  rlist.append(n)
  return rlist                                        # returning the values to reflect in the main


#...............Evaluating the value of the function f(x)....
def evaluate(twodlist,b,n):                                                 
  r=[]
  for i in range(n):                           #convert binary to integer
    s=0
    for j in range(b):
      s=s+(twodlist[i][j]*pow(2,b-j-1))
    r.append(s)
  return r


#............Selecting the population according to the fitness....
def select(twodlist,r,n,b):                           
  sum=0
  s=[]
  nl=[]
  q=[]
  for i in range(n):                                 # evaluating cummulative frequency & total frequency                             
    sum=sum+r[i]
    if i==0:
      s.append(r[i])
    else:
      s.append(s[i-1]+r[i])
  if sum==0:
   print ' errorrr !!! '                             # if all the members of the population are zero
   exit()
  else:
   for j in range(n):
        s[j]=(s[j]*100)/sum                          # bounding in the range 0-100
   for k in range(n):                                
     flag=0
     m=randint(0,100)                                # m is the randomly generated value to be compared with cummulative frequency
     for j in range(n):
       if m<s[j]:
         for c in range(b):
           q.append(twodlist[j][c])
         flag=1
         break
     if flag==0:                                     # if no member is selected,then first member is selected by default
       for c in range(b):
         q.append(twodlist[0][c])
   
        
     nl.append(q)                                    # nl is the new selected population
     q=[]
        
   for f in range(n):                               #print the selected population
     print nl[f]
 
   return nl    



 # ...............Evolution in the population......
def alter(twodlist,n,b):                            
  i=0
 
  while i<n:
	#CROSSOVER OPERATOR
	if (i+1)!=n:                                     #check for odd size population
		prob=round(random(),2)                       #for two digit precision
		if prob<0.95:
		 x=randint(1,b-1)                            #x is the position on which we apply crossover
		 print ' applying crossover between ' ,(i+1),' & ',(i+2),' member of population at bit postion:',x
		 for j in range(x,b):                        # this loop swap the position of bits
		   elem1=twodlist[i][j]
		   twodlist[i][j]=twodlist[i+1][j]
		   twodlist[i+1][j]=elem1
		    
	#MUTATION OPERATOR
	prob=round(random(),2)
	if prob<0.10:
	 x=randint(0,b-1)                             #x is the position that to be flipped
	 print ' applying mutation on ',(i+1),' member of population at bit position: ',x
	 twodlist[i][x]=twodlist[i][x]^1              # flip the bit

	if (i+1)!=n:                                  #check for even size population
		prob=round(random(),2)
		if prob<0.10:
		 x=randint(0,b-1)
		 print ' applying mutation on ',(i+2),' member of population at bit position: ',x
		 twodlist[i+1][x]=twodlist[i+1][x]^1
	i=i+2	
  print ' New population after changes will be: '
  for k in range(n):                        
     print twodlist[k]
  return twodlist

#.............Display the maximum value in function f(x)=x....
def display(twodlist,r,n,b):
  print ' final generation:'
  for i in range (n):                            #print the value in binary form
    print twodlist[i]                        
  max=r[0]
  s=twodlist[0]
  for j in range(1,n):                         #find the maximum value in f(x)=x
    if max<r[j]:
      max=r[j]
      s=twodlist[j]
  print ' maximum value of f(x)=x ', max
  print ' max in binary ' , s




def main():
  twodlist=[]                             #twolist contain population in binary form
  r=[]                                    #r contain population in real form
  n=0                                     #initialize size of population with 0
  b=0                                     #initialise number of bits with 0 value
  rlist=[]                                #it contain reflected values
  print ' Genetic Algo to maximize f(x)=x '  
  rlist=initializtion(twodlist,b,n)
  twodlist=rlist[0]
  b=rlist[1]
  n=rlist[2]
  r=evaluate(twodlist,b,n)
  i=1
  while i<=20:
    print ' Population selected for ', i,' generation according to fitness: '
    twodlist=select(twodlist,r,n,b)
    print ' changes in generation: ',i
    twodlist=alter(twodlist,n,b)
    r=evaluate(twodlist,b,n)
    i=i+1
  display(twodlist,r,n,b)                              
    

if __name__ == '__main__':
    main()
