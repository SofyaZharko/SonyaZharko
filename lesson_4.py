s = ''.join((str(input()).lower()).split())
total = 0
ans = []
for j in range(len(s)):
    if s[j] == 'н':
        total += 1
    elif s[j] != 'н':
        ans.append(total)
        total = 0
ans.append(total)
print(max(ans))



text = (str(input()))
k = 0
while text[k] != '(':
    k += 1
k += 1
while text[k] != ')':
    print(text[k], end='')
    k += 1



s = (str(input()).lower())
for i in s.split():
    if (i.startswith("а") and i.endswith("я")):
        print(i)