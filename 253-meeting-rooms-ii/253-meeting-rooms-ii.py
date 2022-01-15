class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        max_meetings = 0
        curr_start = -1
        curr_meetings = set()
        save = set()
        
        # used to differentiate between intervals in set
        uid = 0
        
        for meeting in intervals:
            # if have the same start, just add it to the collection
            if meeting[0] == curr_start:
                uid += 1
                curr_meetings.add((meeting[0], meeting[1], uid))
            # else, reconsider meetings that could have passed to remove
            else:
                curr_start = meeting[0]
                max_meetings = max(max_meetings, len(curr_meetings))
                save.clear()
                for curr_meeting in curr_meetings:
                    if curr_meeting[1] > curr_start:
                        save.add(curr_meeting)
                curr_meetings, save = save, curr_meetings
                uid += 1
                curr_meetings.add((meeting[0], meeting[1], uid))
        
        max_meetings = max(max_meetings, len(curr_meetings))
        return max_meetings
                    
                    
                    
                
        