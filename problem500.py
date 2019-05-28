import mylib, math

m = 500500507
t = 500500
pp = sorted(mylib.primes_from_file(10 ** 7))[:t]
p_max = max(pp)
p_max_r = math.ceil(p_max ** 0.5)
print(len(pp), p_max, p_max_r, p_max_r ** 2)
rr = pp[:t]
qq = [q for q in pp if q <= p_max_r]
print(qq)

for q in qq:
    x = q ** 2
    while x < p_max:
        print(q, x)
        rr.append(x)
        x = x ** 2

rr = sorted(rr)[:t]
print(max(rr))
s = 1
for i in range(len(rr)):
    r = rr[i]
    if not i % 10:
        print(i, r)
    s = (s * r) % m
print(s)
