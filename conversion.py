print("Let's play at Caesar cipher!")

tmp = list(input()) #変換対象文字列
print("How many seeds?")
seed = int(input())
#for i in range(seed):
ans = ""
for word in list(tmp):
  asc = ord(word)
  #文字種類を判別
  if asc < 12354:
    foo = asc - 97
    foo = (foo + seed) % 26
    asc = foo + 97
  else:
    foo = asc - 12354
    foo = (foo + seed * 2) % 81
    asc = foo + 12354
    print(asc)
  ans += chr(asc)
print(ans)
