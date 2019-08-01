# Complete the function below.

# matchtype is left, right, or inner

def match(matchtype, left, right):
	output = []
    
	if matchtype=="left":
		for i,m in enumerate(left):
			pair = []
			matched = False
			for j,n in enumerate(right):
				if n==m:
					pair+=[i]
					pair+=[j]
					matched = True
				elif j==len(right)-1 and matched==False:
					pair+=[i]
					pair+=[-1]
                    
				if len(pair) > 0:
					output.append(pair)
            
            
	elif matchtype=="right":
		for i,m in enumerate(right):
			pair = []
			matched = False
			for j,n in enumerate(left):
				#pair=[]
				print m, i
				print n, j
				
				if n==m:
					pair+=[j]
					pair+=[i]
					matched = True
				elif (j==len(left)-1) and matched == False:
					pair+=[-1]
					pair+=[i]
					print "LAST"
                
				if (len(pair) > 0):
					print pair
					print '------'
					output.append(pair)
					
				pair = []
            
	elif matchtype=="inner":
		for i in range(len(left)):
			pair = []
			if left[i] in right:
				pair.append(i)
				pair.append(right.index(left[i]))
        
			if len(pair) > 0:
				output.append(pair)
        
	return output

'''	
right

apple		grape
grape		lemon
grape		apple
melon


1 0
2 0
-1 1
0 2
'''

print match("right", ['apple','grape','grape','melon'],['grape','lemon','apple'])
