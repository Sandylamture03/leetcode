class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        dict = defaultdict(int)
        res = []
        for i in cpdomains:
            click, domain = i.split(" ")
            dict[domain] += int(click)
            
            li = domain.split(".")
            
            subDomain = ''
            for j in range(1, len(li)):
                subDomain = '.'.join(li[j:])
                dict[subDomain] += int(click)
        
        for k, v in dict.items():
            res.append(str(v) + ' ' + k)
        
        return res
