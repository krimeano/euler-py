"""
2z - length of bottom lateral
let the triangle to be isosceles
let p<q and i<j


a+b+c+d = hz = s
a = gz
a+b = iz
a+c = jz

p+m = q+n = z
m = z-p
n= z-q
i/p = j/q = h/z
i/g = (z+m) / (z+k) = (2z-p) / (z+k)
j/g = (z+n) / (z-k) = (2z-q) / (z-k)

i = ph/z
j = qh/z
g = i(z+k)/(z+m) = j(z-k)/(z+n)
ph(z+k)/z(z+m) = qh(z-k)/z(z+n)
(pz+pk)(z+n) = (qz-qk)(z+m)
(pz+pk)(2z-q) = (qz-qk)(2z-p)
2pzz + 2pzk - pqz - pqk = 2qzz - 2qkz - pqz +pqk
2k(pz+qz-pq) = 2zz(q-p)

pzz + pzn + pkz + pkn = qzz + qzm - qkz - qkm
k(pz+pn + qz+qm) = qzz + qzm - pzz - pzn

qzz + qz(z-p) - pzz - pz(z-q) = 2qzz - pzq - 2pzz +  pzq = 2zz(q-p)
pz + p(z-q) + qz + q(z-p) = pz + pz - pq + qz + qz - pq = 2pz + 2qz - 2pq = 2(pz+qz-pq)
k = (q-p)zz/(pz+qz-pq)

z+k = (pzz + qzz - pqz + qzz - pzz)/(pz+qz-pq) = qz(2z-p)/(pz+qz-pq)
z+m = 2z-p
g = ph/z * qz(2z-p) / (pz+qz-pq) / (2z-p) = pqh / (pz+qz-pq)
g =
h = g (pz + qz - pq) / pq


a+b+c+d = s

a = pqs / (ps+qs-pq) = 1 / (1/p + 1/q - 1/s)
1/a = 1/p + 1/q - 1/s
a+b = ph = p
a+c = qh = q
55 = (22,8,11,14)
a+b+c+d = 55
a+b = 30
a+c = 33
a = 30 * 33 * 55 / (30 * 55 +33 * 55 - 33 * 30)

1/30 + 1/33 - 1/55

p * s -integer
q * s -integer
"""
t = 0
for s in range(1, 20):
    for q in range(1, s):
        for p in range(1, q + 1):
            x = p * q * s
            y = p * s + q * s - p * q
            if not x % y:
                a = x // y
                b = p - a
                c = q - a
                d = s - p - q + a
                t += s
                print(s, x, y, a, b, c, d)
print(t)
