class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        sList = list(s)
        
        index = len(sList) - 1
        groupCounter = 0
        
        while index >= 0:
            if sList[index] == "-":
                sList.pop(index)
            else:
                sList[index] = sList[index].upper()
                groupCounter = (groupCounter + 1) % k
                if groupCounter == 0:
                    sList.insert(index, "-")
            index -= 1
        
        if (len(sList) > 0 and sList[0] == "-"):
            sList.pop(0)
        return "".join(sList)