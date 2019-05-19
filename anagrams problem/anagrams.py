class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        master ={}
        words = []
        done =[]
        for i in range(len(A)):
            words.append(A[i])
        for i in range(len(words)):
            w1 = list(words[i])
            w1.sort()
            str1=""
            words[i]=str1.join(w1)
            if words[i] not in master:
                master[words[i]] = [i+1]
            else:
                master[words[i]].append(i+1)
        
        return list(master.values())
