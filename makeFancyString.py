def makeFancyString(s):
        if len(s) <= 1 :
            return s
        i, count = 0, 0
        j = i + 1
        ans = ""
        for _ in range(len(s)-1):
            
            if s[i] == s[j] and count >= 2:
                s = s[:i] + s[j:] 
                
            elif s[i] == s[j]:
                count = 2
                i += 1
                j+=1
                
            elif s[i] != s[j]:
                i += 1
                j += 1
                count = 0
                
        return s
