print(f"{sum((lambda r: (lambda q: all(1<=abs(d)<=3 for d in[q[i+1]-q[i]for i in range(len(q)-1)])and(all(d>0 for d in[q[i+1]-q[i]for i in range(len(q)-1)])or all(d<0 for d in[q[i+1]-q[i]for i in range(len(q)-1)])))(r)or any((lambda q: all(1<=abs(d)<=3 for d in[q[i+1]-q[i]for i in range(len(q)-1)])and(all(d>0 for d in[q[i+1]-q[i]for i in range(len(q)-1)])or all(d<0 for d in[q[i+1]-q[i]for i in range(len(q)-1)])))([*r[:i]]+[*r[i+1:]])for i in range(len(r))))([*map(int,l.split())])for l in open('dec2input.txt'))}")
# 644