# Qtec - Assignments
def searchString(strings,patterns):
    """Find pattern from string and return count"""
    # print(strings,patterns)
    slen = len(strings)
    plen =  len(patterns)
    count = 0
    for i in range(slen+1):
        print(i,strings[i:i+plen])
        if strings[i:i+plen] == patterns:
            count += 1
    return count

################################
strings = "tadadattaetadadadafa"
patterns = "dada"
result = searchString(strings,patterns)
print(f"Total Count: {result}.")

