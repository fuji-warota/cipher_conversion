print("Let's play at Caesar cipher!")

tmp = list(input()) #変換対象文字列
print ("How many seeds?")
seed = int(input())
#for i in range(seed):
ans = ""
for word in list(tmp):
  asc = ord(word)
  foo = asc - 97
  foo = (foo + seed) % 26
  asc = foo + 97
  ans += chr(asc)
print(ans)
