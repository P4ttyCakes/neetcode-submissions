class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderList = {}

        for i in range(len(order)):
            orderList[order[i]] = i
        
        for i in range(len(words)- 1):
            word1 = words[i]
            word2 = words[i+1]

            for j in range(len(word1)):
                if j == len(word2): # word2 is a prefix of word1, so that's false
                    return False 
                
                #we are looking for differing characters

                if word1[j] != word2[j]:
                    if orderList[word1[j]] > orderList[word2[j]]:
                        return False
                
                    break
        return True

    



            


        
        