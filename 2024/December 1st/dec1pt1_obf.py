print(f"{sum(abs(x-y)for x,y in zip(*[sorted(l)for l in zip(*[[*map(int,z.split())]for z in open('dec1input.txt')])]))}")
# 2264607