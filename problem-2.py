# Qtec - Assignments
def searchString(strings,patterns):
    """Find pattern from string and return count"""
    slen,plen,count = len(strings),len(patterns),0     # string lenght, pattern lenght, number of matched patterns
    for i in range(slen+1):
        if strings[i:i+plen] == patterns:
            count += 1
    return count
################################
strings = "tadadattaetadadadafa"
patterns = "dada"
result = searchString(strings,patterns)
print(f"Total matched pattern count: {result}.")