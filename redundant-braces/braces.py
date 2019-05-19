class Solution:
	# @param A : string
	# @return an integer
	def braces(self, A):
	    arr =[]
	    for i in range(len(A)): 
            if A[i] == ')':  
                k = arr[-1]
                arr.pop()
                count = 0
                while k != '(':  
                    count += 1
                    k = arr[-1]
                    arr.pop()
                    
                if count <= 1:  
                    return 1
      
            else: 
                arr.append(A[i])
                
        return 0
