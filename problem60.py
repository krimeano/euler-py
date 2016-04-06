import mylib

e = 4
ppp = mylib.primes_from_file(10 ** (2 * e))
pp = sorted(p for p in ppp if p < 10 ** e)
ss = [{}]

max_len = 0
for p in pp:
    if p == 2:
        continue
    ss_add = []
    for s in ss:
        if not len(s):
            ss_add.append({p})
            continue
        all_primes = True
        for q in s:
            pq = [str(p), str(q)]
            if int(''.join(pq)) not in ppp or int(''.join(pq[::-1])) not in ppp:
                all_primes = False
                break
        if all_primes:
            s_new = s | {p}
            if len(s_new) >= max_len:
                max_len = len(s_new)
                print(s_new)
            ss_add.append(s_new)
    ss += ss_add
print([(s, sum(s)) for s in ss if len(s) >= max_len])
