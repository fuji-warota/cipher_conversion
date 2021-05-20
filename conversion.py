print("Let's play at Caesar cipher!")

tmp = list(input()) #変換対象文字列
seed = int(input()) 
rel = [0] * len(tmp)
for i in range(len(tmp)):
   rel[i] = chr(ord(tmp[i])+seed)

print(*rel)
