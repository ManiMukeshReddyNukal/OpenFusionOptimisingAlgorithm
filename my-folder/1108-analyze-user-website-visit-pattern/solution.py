class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        webinfo=[]
        for i,j,k in zip(username,timestamp,website):
            webinfo.append((j,i,k))
        if not webinfo:
            return []
        webinfo.sort(key=lambda x:x[0])
        sitesvisitedbyuser=defaultdict(list)
        for _,user,site in webinfo:
            sitesvisitedbyuser[user].append(site)
        counter=defaultdict(int)
        for user in sitesvisitedbyuser:
            usertravelledroutes=set(combinations(sitesvisitedbyuser[user], 3))
            for route in usertravelledroutes:
                counter[route]+=1
        maxval,routes=max(counter.values()),[]
        for r,val in counter.items():
            if val==maxval:
                routes.append(r)
        routes.sort()
        return routes[0]
