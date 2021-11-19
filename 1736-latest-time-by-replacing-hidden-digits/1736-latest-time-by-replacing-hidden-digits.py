class Solution:
    def maximumTime(self, time: str) -> str:
        # we deal with hh and mm separately
        l = list(time)
        
        if l[0] == "?":
            if l[1] == "?":
                # hh = ??
                l[0] = "2"
                l[1] = "3"
            elif int(l[1]) > 3:
                # hh = ?[4-9]
                l[0] = "1"
            else:
                # hh - ?[0-3]
                l[0] = "2"
        elif l[1] == "?":
            # hh = x?
            if int(l[0]) == 2:
                # hh = 2?
                l[1] = "3"
            else:
                # hh = 9?
                l[1] = "9"
        
        if l[3] == "?":
            l[3] = "5"
        
        if l[4] == "?":
            l[4] = "9"
        
        return "".join(l)