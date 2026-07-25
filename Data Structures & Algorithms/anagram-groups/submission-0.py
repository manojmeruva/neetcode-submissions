class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        istaken = [0]*len(strs)
        for i in range(len(strs)):
            io=[strs[i]]
            if istaken[i] != 1:
                for j in range(i+1,len(strs)):
                    if self.valid(strs[i],strs[j]):
                        io.append(strs[j])
                        istaken[j]=1
                istaken[i] = 1
                output.append(io)
            
        return output


        
    def valid(self,str1,str2):
        if len(str1)!=len(str2):
            return False
        hashmap ={}
        for i in range(len(str1)):
            hashmap[str1[i]]=hashmap.get(str1[i],0)+1
            hashmap[str2[i]]=hashmap.get(str2[i],0)-1
        for i in hashmap:
            if hashmap[i] != 0:
                return False
        return True



        