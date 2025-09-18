stringLock, symvols10, stringUnlock = input('in: '), '0123456789', ''

for i in stringLock: 
    if i.isupper(): 
        stringLock = stringLock[stringLock.find(i):]
        break
step = [int(i) for i in range(len(stringLock) - 1) \
        if stringLock[i] in symvols10 and stringLock[i + 1] not in symvols10][0]
simvolsUnlock = [str(stringLock[i]) for i in range(0, len(stringLock), step + 1)]
for i in simvolsUnlock: stringUnlock += i

print(stringUnlock)

