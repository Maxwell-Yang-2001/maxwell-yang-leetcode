def getEt(list: List[int]) -> int:
    return list[0]

def addTaskToToDo(toDo: List[List[int]], task: List[int]) -> int:
    index = 0
    if len(toDo) != 0:
        # if larger than the largest, insert at the end
        if taskIsSmaller(toDo[len(toDo) - 1], task):
            index = len(toDo)
        # else insert at index using binary search
        else:
            index = bSearch(toDo, task, 0, len(toDo) - 1)
    toDo.insert(index, task)
    
def bSearch(list: List[List[int]], elem: List[int], start: int, end: int) -> int:
    if end == start:
        return start
    mid = (start + end) // 2
    if taskIsSmaller(elem, list[mid]):
        return bSearch(list, elem, 0, mid)
    else:
        return bSearch(list, elem, mid + 1, end)
    
def taskIsSmaller(task1: List[int], task2: List[int]) -> bool:
    return task1[1] < task2[1] or (task1[1] == task2[1] and task1[2] < task2[2])

class Solution:
    
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # change into [et, pt, index]
        for i, t in enumerate(tasks):
            t.append(i)
        
        # sort by enqueueTime
        tasks.sort(key = getEt)
        result = []
        toDo = []
        index = 0
        time = 0
        
        while index < len(tasks):
            if len(toDo) == 0 and time < tasks[index][0]:
                time = tasks[index][0]
            
            if tasks[index][0] <= time:
                while index < len(tasks) and tasks[index][0] <= time:
                    addTaskToToDo(toDo, tasks[index])
                    index += 1
            
            currTask = toDo.pop(0)
            result.append(currTask[2])
            time += currTask[1]
            
        # one pass the remaining tasks (they are already sorted)
        for task in toDo:
            result.append(task[2])
        return result