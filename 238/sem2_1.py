k = 5
s = input()

res = ''

replacement = {
    chr(i): chr((i + k - ord('a')) % (ord('z') - ord('a') + 1) + ord('a'))
    for i in range(ord('a'), ord('z') + 1)
}

print(*(i for i in range(1)), 1)
print(*(replacement[c] for c in s), sep='')
res = ''.join(replacement[c] for c in s)

for c in s:
    res += replacement[c]
    # res += chr(ord(c) + k)
    # print(chr((ord(c) + k - ord('a')) % (ord('z') - ord('a') + 1) + ord('a')))

print(res)
