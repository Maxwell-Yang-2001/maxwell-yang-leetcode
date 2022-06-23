class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda l: l[1])
        pq = []
        time = 0
        for c in courses:
            if time + c[0] <= c[1]:
                # push negative value to reverse sorting order
                heapq.heappush(pq, -c[0])
                time += c[0]
            elif pq and -pq[0] > c[0]:
                time += c[0] + heapq.heappop(pq)
                heapq.heappush(pq, -c[0])
        return len(pq)