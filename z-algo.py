# s = "aabxaabxcaabxaabxay"
# s = "abc$xabcabzabc"
text = "aabxaabxcaabxaabxay"
substring = input()
s = substring + "$" + text
z = '0'
left = 0
length = 1
val = 0
idx = []
for i in range(1, len(s)):
    while length <= i:
        if s[i: i + length] == s[left: left + length]:
            # print("s", s[i: i + length])
            # print("o", s[left: left + length])
            val += 1
            length += 1
            #print("length, i", length, i)
        else:
            # print("s", s[i: i + length])
            # print("o", s[left: left + length])
            # print("val", val)
            if val == len(substring):
                idx.append((i - len(substring) - 1))
            z += str(val)
            val = 0
            length = 1
            break
        if length > i:
            if val == len(substring):
                idx.append((i - len(substring) - 1))
            z += str(val)
            val = 0
            length = 1
            break
print("z:", z)
print("text:", text)
print(f'{substring} is at index {idx} in the text')
