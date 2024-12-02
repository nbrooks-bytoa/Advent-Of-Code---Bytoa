from collections import Counter as C
print(f"{sum((l*(d:=C(b:=[*zip(*[map(int,x.split())for x in open('dec1input.txt')])][1]))[l])for l in sorted([*zip(*[map(int,x.split())for x in open('dec1input.txt')])][0]))}")
# 22588371