class Solution(object):
    def hIndex(self, citations):
        
        listLength = len(citations)
        h = 0
        sortedCitations = sorted(citations)

        if(listLength == 1 and citations[0] > 0):
            return 1

        for i in range(listLength-1, -1, -1):
            if (sortedCitations[i] >= h+1):
                h += 1
            else:break

        return h