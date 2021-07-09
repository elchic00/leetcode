import heapq
from collections import defaultdict
def findCheapestPrice(n, flights, src, dst, K):
    
        adj_list = defaultdict(list)
        for unvisited, visited, weight in flights:
            adj_list[unvisited].append((visited,weight))
        
        best_visited = defaultdict(lambda: float('inf')) # Initialized to maximum. This lambda will make it so every element you put in the dictionary will have a default key of INF.
        
        prior_queue = [ (0, -1, src) ] #weight, steps, node

        while prior_queue:
            cost, steps, node = heapq.heappop(prior_queue)
            
            if best_visited[node] <= steps:  #Have seen the node already, and the steps are more than last time
                continue

            if steps>K:  # More than k stops, invalid
                continue

            if node==dst: 
                return cost
            
            best_visited[node] = steps #Update steps

            for neighb, weight in adj_list[node]:
                if steps + 1 < best_visited[neighb]: #Push neighbor into the heap, only if steps+1 is better than the last time it was visited
                    heapq.heappush(prior_queue, (cost+weight, steps + 1, neighb))

        return -1     
    
print(findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))
    
#Time: O(Edges log V)(Vertex == # of nodes), Space: O(V)
