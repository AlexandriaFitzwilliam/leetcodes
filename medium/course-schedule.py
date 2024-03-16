class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not prerequisites:
            return True

        #decide on a graph representation
        graph  = {}
        #graph is going to be { NODE_ID : { ougoingedges: [], incomingedges : [] } }
        #make the graph
        for course, prereq in prerequisites:
            #course <-- prereq
            # 0 1
            # {0: incoming : 1}
            # {1: outgoing : 0}
            if course not in graph:
                graph[course] = { 'ougoingedges': [], 'incomingedges' : 0 }

            graph[course]['incomingedges'] += 1


            if prereq not in graph:
                graph[prereq] = { 'ougoingedges': [], 'incomingedges' : 0 }
            graph[prereq]['ougoingedges'].append(course)


        q = []

        for course, edges in graph.items():
            # if len(edges['incomingedges']) == 0:
            if not edges['incomingedges']:
                q.append(course)

        print(f'q={q}')

        seen = set()
        while q:
            cur = q.pop()
            if cur in seen:
                continue
            print(f'cur={cur}')
            seen.add(cur)
            # for the outgoing_edges of cur:
            for course in graph[cur]['ougoingedges']:
                graph[course]['incomingedges'] -=1
            #     delete the current node from the outgoingedges nodes incomingedges list
            #     if the node has no incoming edges other than me
                if not graph[course]['incomingedges']:
            #         add to code
                    q.append(course)

        print(f'seen={seen}')


        return len(seen)==numCourses

