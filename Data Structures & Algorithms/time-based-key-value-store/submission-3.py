class TimeMap:

    def __init__(self):
        self.time_map = {}
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []

        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        keys = self.time_map.get(key,[])
        
        start = 0
        end = len(keys)-1
        result = ""
        while start <= end:
            mid = (start+end)//2
            if keys[mid][1]<=timestamp:
                result = keys[mid][0]
                start = mid+1
            
            else:
                end = mid-1
        return result
        
