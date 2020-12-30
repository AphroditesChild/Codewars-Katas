def solution(s):
    return [s[i:i+2] if len(s)%2==0 else (s+'_')[i:i+2] for i in range(0,len(s),2)]
# OR SIMPLY :
    #return [(s+'_')[i:i+2] for i in range(0,len(s),2)]
    # because i won't iterate through '_' if len(s) is odd

print(solution("To be or not to be"))
input()
