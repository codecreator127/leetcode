class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)

        def DFS(keys):
            for key in keys:
                if visited[key]:
                    continue
                visited[key] = True
                DFS(rooms[key])

        
        DFS([0])

        for room in visited:
            if not room:
                return False

        return True
