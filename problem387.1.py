import mylib

primes = mylib.make_primes_sieve_atkin(10 ** 4)  # a ** b means a in power of b, in this case 10000

harshads_by_power_of_ten = list()
harshads_by_power_of_ten.append([])  # append ~ push a new element in the list
harshads_by_power_of_ten.append([1, 2, 3, 4, 5, 6, 7, 8, 9])


def make_right_harshads(power_of_ten):
    if len(harshads_by_power_of_ten) < power_of_ten:
        make_right_harshads(power_of_ten - 1)
    previous_harshads = harshads_by_power_of_ten[power_of_ten - 1]
    harshads_new = []
    for harshad_number in previous_harshads:
        harshads_new += gen_next_right_harshads(power_of_ten, harshad_number)
    harshads_by_power_of_ten.append(harshads_new)
    print('-' * 79)


def gen_next_right_harshads(power_of_ten, previous_harshad_number):
    out = list()
    new_base = 10 * previous_harshad_number
    remainder = new_base % power_of_ten
    if not remainder:
        out.append(new_base)  # add 20, 240, 3240 etc
    for x in range(power_of_ten - remainder, 10, power_of_ten):  # ~ for (i=p-r; i<10; i+=p)
        out.append(new_base + x)
        # for example, for 220, cycle goes through 3-1 = 2, 5, 8 and we store 222, 225, 228
    print(power_of_ten, previous_harshad_number, out)
    return out


def filter_strong_harshads():
    out = list()
    for i in range(1, len(harshads_by_power_of_ten)):
        for x in harshads_by_power_of_ten[i]:
            if (x // i) in primes:
                out.append(x)
            else:
                print(x, '/', i, '=', x // i, 'is NOT prime')
    print('-' * 79)
    print('STRONG HARSHADS:')
    print(out)
    print('-' * 79)
    return out


def make_harshad_primes(strong_right_harshads):
    out = []
    tails = (1, 3, 7, 9)
    for x in strong_right_harshads:
        for y in tails:
            z = 10 * x + y
            if z in primes:
                out.append(z)
                print(z, 'is prime')
            else:
                print(z, 'is NOT prime')

    return out


if __name__ == '__main__':
    print('PRIMES:', primes)
    print('-' * 79)
    make_right_harshads(3)
    print('-' * 79)
    print('Harshads by power of ten:')
    for hh in harshads_by_power_of_ten:
        print(hh)
    print('-' * 79)
    harshad_primes = make_harshad_primes(filter_strong_harshads())
    print('-' * 79)
    print('RESULT:')
    print(sum(harshad_primes), harshad_primes)

"""
OUTPUT:
PRIMES: {2: True, 3: True, 5: True, 7: True, 7297: True, 11: True, 13: True, 2063: True, 17: True, 19: True, 2069: True, 23: True, 8219: True, 29: True, 6343: True, 31: True, 2081: True, 8389: True, 2083: True, 8647: True, 37: True, 2087: True, 8429: True, 41: True, 43: True, 8237: True, 47: True, 2099: True, 53: True, 6199: True, 4639: True, 4153: True, 59: True, 61: True, 4159: True, 8731: True, 2113: True, 67: True, 8663: True, 71: True, 73: True, 8887: True, 6221: True, 8893: True, 79: True, 2129: True, 8527: True, 83: True, 6229: True, 1721: True, 89: True, 4111: True, 2141: True, 2143: True, 97: True, 7867: True, 8293: True, 101: True, 9907: True, 103: True, 7573: True, 2153: True, 107: True, 9619: True, 109: True, 701: True, 113: True, 9551: True, 4211: True, 1163: True, 5323: True, 6263: True, 4217: True, 7369: True, 4219: True, 6269: True, 127: True, 7927: True, 131: True, 4229: True, 4231: True, 137: True, 9739: True, 139: True, 8629: True, 6287: True, 4241: True, 4243: True, 8461: True, 149: True, 151: True, 2203: True, 751: True, 4253: True, 7643: True, 2207: True, 8353: True, 163: True, 2213: True, 167: True, 7507: True, 7879: True, 2221: True, 4271: True, 4273: True, 179: True, 181: True, 6329: True, 683: True, 4127: True, 2237: True, 2393: True, 191: True, 6553: True, 193: True, 2243: True, 197: True, 9281: True, 199: True, 4297: True, 2251: True, 6353: True, 211: True, 7039: True, 6359: True, 6361: True, 2267: True, 2053: True, 2269: True, 4133: True, 4099: True, 2273: True, 227: True, 9623: True, 229: True, 4327: True, 233: True, 6379: True, 8123: True, 2287: True, 241: True, 4339: True, 6971: True, 2293: True, 9419: True, 2089: True, 2297: True, 7207: True, 251: True, 4349: True, 7237: True, 7919: True, 257: True, 9283: True, 4139: True, 8039: True, 2309: True, 263: True, 4363: True, 269: True, 271: True, 8867: True, 5507: True, 4373: True, 8179: True, 5849: True, 8329: True, 281: True, 283: True, 2333: True, 389: True, 2339: True, 293: True, 4391: True, 9643: True, 2347: True, 419: True, 2351: True, 6449: True, 9421: True, 307: True, 7307: True, 2357: True, 311: True, 3079: True, 313: True, 1759: True, 317: True, 6197: True, 7853: True, 2371: True, 6421: True, 4421: True, 9343: True, 4423: True, 2377: True, 331: True, 2381: True, 2383: True, 7529: True, 337: True, 6883: True, 8431: True, 2389: True, 6217: True, 6899: True, 4441: True, 8263: True, 347: True, 6317: True, 349: True, 2399: True, 9941: True, 353: True, 7349: True, 4451: True, 9377: True, 359: True, 9491: True, 4457: True, 2411: True, 367: True, 7309: True, 2417: True, 6547: True, 373: True, 2423: True, 6521: True, 6491: True, 379: True, 8573: True, 8537: True, 383: True, 4481: True, 4483: True, 2437: True, 3559: True, 2441: True, 9203: True, 8599: True, 397: True, 2447: True, 401: True, 6211: True, 7583: True, 8597: True, 6551: True, 6151: True, 409: True, 7013: True, 2459: True, 5881: True, 5189: True, 4513: True, 5333: True, 4507: True, 4517: True, 4519: True, 2473: True, 4523: True, 6389: True, 2477: True, 431: True, 3083: True, 433: True, 4447: True, 2803: True, 6581: True, 439: True, 1583: True, 8539: True, 443: True, 9221: True, 7789: True, 449: True, 4547: True, 4549: True, 2503: True, 457: True, 5879: True, 461: True, 7027: True, 463: True, 4561: True, 2467: True, 9631: True, 7517: True, 4567: True, 2521: True, 6619: True, 8669: True, 421: True, 2531: True, 4463: True, 8677: True, 4177: True, 8681: True, 491: True, 5437: True, 6563: True, 971: True, 4591: True, 8609: True, 2131: True, 7177: True, 4597: True, 2551: True, 6427: True, 4603: True, 509: True, 7253: True, 7723: True, 3499: True, 6661: True, 521: True, 2281: True, 523: True, 4621: True, 8269: True, 8719: True, 6673: True, 2579: True, 2137: True, 7451: True, 5309: True, 541: True, 9781: True, 2591: True, 2593: True, 547: True, 8741: True, 6577: True, 6823: True, 4649: True, 7247: True, 4651: True, 557: True, 8167: True, 6703: True, 2609: True, 8543: True, 563: True, 6709: True, 6373: True, 4663: True, 569: True, 9157: True, 571: True, 7043: True, 2621: True, 6719: True, 4673: True, 8971: True, 4679: True, 2633: True, 587: True, 8419: True, 6733: True, 7603: True, 7949: True, 5407: True, 593: True, 6089: True, 1123: True, 8951: True, 4657: True, 2543: True, 601: True, 5903: True, 607: True, 2657: True, 2659: True, 613: True, 2663: True, 617: True, 619: True, 7219: True, 2671: True, 157: True, 4721: True, 4723: True, 2677: True, 4201: True, 4729: True, 2683: True, 9091: True, 4733: True, 2687: True, 641: True, 643: True, 2693: True, 8273: True, 647: True, 6793: True, 7151: True, 2699: True, 1931: True, 653: True, 4751: True, 8849: True, 2707: True, 661: True, 4759: True, 6701: True, 2713: True, 6637: True, 8861: True, 2719: True, 673: True, 7933: True, 677: True, 2161: True, 2729: True, 2731: True, 6829: True, 8747: True, 4783: True, 9769: True, 6833: True, 4787: True, 8447: True, 4789: True, 3529: True, 4793: True, 8297: True, 2749: True, 4799: True, 4801: True, 9811: True, 709: True, 6857: True, 8311: True, 4813: True, 2767: True, 3229: True, 4817: True, 6947: True, 6869: True, 727: True, 7321: True, 2777: True, 6607: True, 733: True, 4831: True, 8929: True, 8761: True, 739: True, 2789: True, 743: True, 5927: True, 2797: True, 6367: True, 3571: True, 9293: True, 2801: True, 467: True, 757: True, 2857: True, 761: True, 2753: True, 6271: True, 4861: True, 3541: True, 6163: True, 769: True, 2819: True, 8209: True, 773: True, 8693: True, 4871: True, 7459: True, 7639: True, 4877: True, 8243: True, 4909: True, 2833: True, 787: True, 2837: True, 4889: True, 2843: True, 797: True, 9851: True, 6277: True, 7187: True, 2851: True, 9791: True, 6949: True, 4903: True, 809: True, 811: True, 2861: True, 9007: True, 6959: True, 6301: True, 6961: True, 6983: True, 9011: True, 821: True, 9029: True, 4919: True, 479: True, 829: True, 2879: True, 6977: True, 4931: True, 4933: True, 839: True, 6029: True, 4937: True, 823: True, 9439: True, 4943: True, 3847: True, 2897: True, 8689: True, 853: True, 3779: True, 2903: True, 857: True, 859: True, 4957: True, 863: True, 827: True, 2917: True, 4967: True, 4969: True, 6907: True, 4583: True, 877: True, 2927: True, 881: True, 883: True, 6917: True, 887: True, 8963: True, 4987: True, 5417: True, 6781: True, 3109: True, 4993: True, 2539: True, 4999: True, 8803: True, 2953: True, 907: True, 2957: True, 911: True, 6689: True, 5009: True, 2963: True, 8623: True, 5827: True, 919: True, 2969: True, 2971: True, 8059: True, 5021: True, 5023: True, 929: True, 6299: True, 7079: True, 937: True, 2887: True, 941: True, 5039: True, 8969: True, 499: True, 2999: True, 3001: True, 5051: True, 8147: True, 2549: True, 9511: True, 3011: True, 7109: True, 967: True, 9161: True, 8011: True, 503: True, 5897: True, 3023: True, 5147: True, 977: True, 4259: True, 7193: True, 5077: True, 983: True, 9239: True, 5081: True, 3919: True, 3037: True, 5087: True, 7057: True, 4261: True, 8699: True, 997: True, 8017: True, 7549: True, 3049: True, 5099: True, 5101: True, 2557: True, 8831: True, 1009: True, 5107: True, 3061: True, 7159: True, 5113: True, 2939: True, 3067: True, 1021: True, 5119: True, 8363: True, 7331: True, 8231: True, 1031: True, 1033: True, 4951: True, 8627: True, 1039: True, 3089: True, 7877: True, 6659: True, 9241: True, 7127: True, 7001: True, 1049: True, 1051: True, 7741: True, 8423: True, 5153: True, 6991: True, 1061: True, 1063: True, 9257: True, 8287: True, 5639: True, 6173: True, 1069: True, 3119: True, 3121: True, 5171: True, 5641: True, 6037: True, 9227: True, 5179: True, 7229: True, 1087: True, 3137: True, 1091: True, 1093: True, 1097: True, 9311: True, 7243: True, 5197: True, 1103: True, 173: True, 5531: True, 9059: True, 1109: True, 8377: True, 5209: True, 3163: True, 1117: True, 719: True, 3167: True, 3169: True, 4283: True, 4129: True, 9319: True, 7577: True, 1129: True, 5227: True, 8221: True, 3181: True, 5231: True, 5233: True, 1879: True, 3187: True, 5237: True, 3191: True, 8941: True, 9337: True, 2239: True, 9341: True, 1151: True, 6827: True, 1153: True, 3203: True, 9349: True, 4289: True, 3209: True, 3607: True, 5261: True, 4973: True, 3217: True, 1171: True, 9859: True, 3221: True, 9109: True, 5273: True, 9371: True, 1181: True, 9041: True, 5279: True, 5281: True, 1187: True, 7333: True, 1193: True, 3271: True, 4637: True, 8837: True, 1201: True, 3251: True, 6841: True, 3253: True, 5303: True, 3257: True, 3259: True, 6691: True, 1213: True, 7951: True, 1217: True, 3041: True, 9187: True, 9413: True, 7883: True, 1223: True, 6451: True, 4337: True, 1229: True, 1231: True, 8737: True, 4643: True, 9767: True, 1237: True, 6997: True, 9431: True, 9433: True, 9043: True, 6247: True, 9437: True, 7717: True, 6323: True, 1249: True, 3299: True, 3301: True, 9587: True, 5351: True, 5869: True, 1259: True, 8839: True, 3313: True, 9467: True, 7411: True, 9461: True, 8369: True, 3319: True, 7417: True, 3323: True, 1277: True, 1279: True, 3329: True, 1283: True, 5381: True, 9931: True, 9479: True, 1289: True, 1291: True, 3343: True, 1297: True, 3347: True, 7681: True, 1301: True, 1303: True, 9497: True, 1307: True, 6863: True, 3359: True, 3361: True, 6113: True, 5413: True, 1319: True, 1321: True, 3371: True, 6569: True, 3373: True, 1327: True, 9521: True, 8233: True, 5683: True, 7477: True, 5431: True, 7481: True, 223: True, 3389: True, 3391: True, 5441: True, 5003: True, 2909: True, 7393: True, 5449: True, 7499: True, 3407: True, 1361: True, 5347: True, 3413: True, 1367: True, 9661: True, 9103: True, 1373: True, 5471: True, 7523: True, 6047: True, 1381: True, 5479: True, 8093: True, 3433: True, 691: True, 5483: True, 1523: True, 5693: True, 8707: True, 7537: True, 5011: True, 7541: True, 5843: True, 1399: True, 3449: True, 7547: True, 5501: True, 9719: True, 5503: True, 5801: True, 1409: True, 3307: True, 3461: True, 7753: True, 577: True, 7561: True, 3467: True, 3469: True, 9049: True, 1423: True, 3457: True, 5521: True, 1427: True, 1429: True, 5527: True, 1433: True, 239: True, 9629: True, 1439: True, 7129: True, 3491: True, 7589: True, 1447: True, 1451: True, 1453: True, 7069: True, 9649: True, 8641: True, 1459: True, 5557: True, 3511: True, 8117: True, 5563: True, 7823: True, 3517: True, 1471: True, 5569: True, 6911: True, 8779: True, 487: True, 5573: True, 3527: True, 7687: True, 1481: True, 1483: True, 3533: True, 1487: True, 1489: True, 3539: True, 1493: True, 5591: True, 6311: True, 9689: True, 3547: True, 9721: True, 8101: True, 8807: True, 7649: True, 8443: True, 3557: True, 1511: True, 9127: True, 6397: True, 6529: True, 7211: True, 4691: True, 5779: True, 7669: True, 5623: True, 7673: True, 7727: True, 1531: True, 9871: True, 3581: True, 7757: True, 3583: True, 7607: True, 9803: True, 9733: True, 1543: True, 3593: True, 7621: True, 599: True, 1549: True, 6871: True, 4013: True, 1553: True, 3331: True, 6803: True, 5653: True, 1559: True, 9391: True, 5657: True, 5659: True, 3613: True, 1567: True, 3617: True, 1571: True, 8713: True, 5669: True, 6599: True, 3623: True, 5167: True, 6257: True, 1579: True, 7213: True, 3631: True, 8753: True, 947: True, 3637: True, 7433: True, 5689: True, 7759: True, 3643: True, 1597: True, 1973: True, 7691: True, 1601: True, 5387: True, 3463: True, 5701: True, 1607: True, 1609: True, 3659: True, 1613: True, 5711: True, 9601: True, 7487: True, 1619: True, 1621: True, 6737: True, 3671: True, 6571: True, 3673: True, 8783: True, 1627: True, 3677: True, 9829: True, 7103: True, 9397: True, 9833: True, 1979: True, 1637: True, 5851: True, 5393: True, 5737: True, 3691: True, 5741: True, 6653: True, 5743: True, 7829: True, 3697: True, 8467: True, 8317: True, 3701: True, 6761: True, 5647: True, 1657: True, 6079: True, 3709: True, 8999: True, 277: True, 9533: True, 9857: True, 1667: True, 1669: True, 3719: True, 7817: True, 2647: True, 5399: True, 3727: True, 5059: True, 3733: True, 5783: True, 3739: True, 6967: True, 1693: True, 5791: True, 1697: True, 9613: True, 1699: True, 9463: True, 7793: True, 8581: True, 1907: True, 1709: True, 5717: True, 5807: True, 3761: True, 9013: True, 8819: True, 5813: True, 3767: True, 8191: True, 3769: True, 5581: True, 1723: True, 5821: True, 5749: True, 8563: True, 7873: True, 3019: True, 7559: True, 1733: True, 8923: True, 7457: True, 9929: True, 631: True, 1741: True, 5839: True, 3793: True, 1747: True, 8161: True, 3797: True, 1753: True, 3803: True, 7901: True, 2341: True, 5857: True, 6779: True, 5861: True, 6469: True, 7121: True, 5867: True, 3821: True, 3823: True, 5651: True, 1777: True, 9199: True, 2003: True, 9973: True, 6763: True, 1783: True, 9743: True, 3833: True, 1787: True, 1789: True, 9173: True, 7937: True, 5419: True, 9323: True, 2689: True, 1801: True, 9539: True, 3851: True, 3853: True, 4397: True, 1811: True, 9403: True, 953: True, 3863: True, 4493: True, 7963: True, 2617: True, 1823: True, 2311: True, 9949: True, 5923: True, 4357: True, 3877: True, 7591: True, 1831: True, 3881: True, 6791: True, 8513: True, 9181: True, 7699: True, 3889: True, 5939: True, 1847: True, 8291: True, 7993: True, 9677: True, 991: True, 7351: True, 8501: True, 5953: True, 3907: True, 1861: True, 3911: True, 8009: True, 1867: True, 9473: True, 3917: True, 5477: True, 1871: True, 1873: True, 3923: True, 1877: True, 4409: True, 3929: True, 9967: True, 3931: True, 5981: True, 5297: True, 1889: True, 5987: True, 9883: True, 3943: True, 9133: True, 6337: True, 3947: True, 9787: True, 1901: True, 9137: True, 2791: True, 8821: True, 659: True, 5519: True, 8053: True, 9679: True, 6007: True, 1913: True, 6011: True, 3967: True, 8171: True, 8069: True, 7489: True, 6679: True, 1663: True, 2711: True, 8087: True, 1933: True, 9697: True, 9901: True, 8081: True, 5443: True, 3989: True, 7907: True, 8089: True, 6043: True, 1949: True, 8521: True, 1951: True, 4001: True, 9151: True, 4003: True, 2179: True, 6053: True, 9817: True, 4007: True, 7703: True, 2111: True, 9001: True, 9067: True, 9749: True, 4157: True, 8111: True, 6203: True, 4019: True, 4021: True, 6473: True, 9277: True, 6073: True, 4703: True, 4027: True, 8863: True, 6067: True, 9923: True, 1013: True, 1987: True, 7841: True, 8933: True, 1993: True, 6091: True, 1997: True, 1999: True, 4049: True, 4051: True, 7283: True, 6101: True, 9209: True, 2741: True, 4057: True, 2011: True, 9887: True, 1499: True, 2017: True, 1019: True, 8387: True, 6481: True, 4073: True, 2027: True, 9547: True, 2029: True, 4079: True, 6131: True, 7019: True, 6133: True, 9839: True, 2039: True, 6121: True, 4091: True, 4093: True, 6143: True}
-------------------------------------------------------------------------------
2 1 [10, 12, 14, 16, 18]
2 2 [20, 22, 24, 26, 28]
2 3 [30, 32, 34, 36, 38]
2 4 [40, 42, 44, 46, 48]
2 5 [50, 52, 54, 56, 58]
2 6 [60, 62, 64, 66, 68]
2 7 [70, 72, 74, 76, 78]
2 8 [80, 82, 84, 86, 88]
2 9 [90, 92, 94, 96, 98]
-------------------------------------------------------------------------------
3 10 [102, 105, 108]
3 12 [120, 123, 126, 129]
3 14 [141, 144, 147]
3 16 [162, 165, 168]
3 18 [180, 183, 186, 189]
3 20 [201, 204, 207]
3 22 [222, 225, 228]
3 24 [240, 243, 246, 249]
3 26 [261, 264, 267]
3 28 [282, 285, 288]
3 30 [300, 303, 306, 309]
3 32 [321, 324, 327]
3 34 [342, 345, 348]
3 36 [360, 363, 366, 369]
3 38 [381, 384, 387]
3 40 [402, 405, 408]
3 42 [420, 423, 426, 429]
3 44 [441, 444, 447]
3 46 [462, 465, 468]
3 48 [480, 483, 486, 489]
3 50 [501, 504, 507]
3 52 [522, 525, 528]
3 54 [540, 543, 546, 549]
3 56 [561, 564, 567]
3 58 [582, 585, 588]
3 60 [600, 603, 606, 609]
3 62 [621, 624, 627]
3 64 [642, 645, 648]
3 66 [660, 663, 666, 669]
3 68 [681, 684, 687]
3 70 [702, 705, 708]
3 72 [720, 723, 726, 729]
3 74 [741, 744, 747]
3 76 [762, 765, 768]
3 78 [780, 783, 786, 789]
3 80 [801, 804, 807]
3 82 [822, 825, 828]
3 84 [840, 843, 846, 849]
3 86 [861, 864, 867]
3 88 [882, 885, 888]
3 90 [900, 903, 906, 909]
3 92 [921, 924, 927]
3 94 [942, 945, 948]
3 96 [960, 963, 966, 969]
3 98 [981, 984, 987]
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
Harshads by power of ten:
[]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
[102, 105, 108, 120, 123, 126, 129, 141, 144, 147, 162, 165, 168, 180, 183, 186, 189, 201, 204, 207, 222, 225, 228, 240, 243, 246, 249, 261, 264, 267, 282, 285, 288, 300, 303, 306, 309, 321, 324, 327, 342, 345, 348, 360, 363, 366, 369, 381, 384, 387, 402, 405, 408, 420, 423, 426, 429, 441, 444, 447, 462, 465, 468, 480, 483, 486, 489, 501, 504, 507, 522, 525, 528, 540, 543, 546, 549, 561, 564, 567, 582, 585, 588, 600, 603, 606, 609, 621, 624, 627, 642, 645, 648, 660, 663, 666, 669, 681, 684, 687, 702, 705, 708, 720, 723, 726, 729, 741, 744, 747, 762, 765, 768, 780, 783, 786, 789, 801, 804, 807, 822, 825, 828, 840, 843, 846, 849, 861, 864, 867, 882, 885, 888, 900, 903, 906, 909, 921, 924, 927, 942, 945, 948, 960, 963, 966, 969, 981, 984, 987]
-------------------------------------------------------------------------------
1 / 1 = 1 is NOT prime
4 / 1 = 4 is NOT prime
6 / 1 = 6 is NOT prime
8 / 1 = 8 is NOT prime
9 / 1 = 9 is NOT prime
12 / 2 = 6 is NOT prime
16 / 2 = 8 is NOT prime
18 / 2 = 9 is NOT prime
20 / 2 = 10 is NOT prime
24 / 2 = 12 is NOT prime
28 / 2 = 14 is NOT prime
30 / 2 = 15 is NOT prime
32 / 2 = 16 is NOT prime
36 / 2 = 18 is NOT prime
40 / 2 = 20 is NOT prime
42 / 2 = 21 is NOT prime
44 / 2 = 22 is NOT prime
48 / 2 = 24 is NOT prime
50 / 2 = 25 is NOT prime
52 / 2 = 26 is NOT prime
54 / 2 = 27 is NOT prime
56 / 2 = 28 is NOT prime
60 / 2 = 30 is NOT prime
64 / 2 = 32 is NOT prime
66 / 2 = 33 is NOT prime
68 / 2 = 34 is NOT prime
70 / 2 = 35 is NOT prime
72 / 2 = 36 is NOT prime
76 / 2 = 38 is NOT prime
78 / 2 = 39 is NOT prime
80 / 2 = 40 is NOT prime
84 / 2 = 42 is NOT prime
88 / 2 = 44 is NOT prime
90 / 2 = 45 is NOT prime
92 / 2 = 46 is NOT prime
96 / 2 = 48 is NOT prime
98 / 2 = 49 is NOT prime
102 / 3 = 34 is NOT prime
105 / 3 = 35 is NOT prime
108 / 3 = 36 is NOT prime
120 / 3 = 40 is NOT prime
126 / 3 = 42 is NOT prime
144 / 3 = 48 is NOT prime
147 / 3 = 49 is NOT prime
162 / 3 = 54 is NOT prime
165 / 3 = 55 is NOT prime
168 / 3 = 56 is NOT prime
180 / 3 = 60 is NOT prime
186 / 3 = 62 is NOT prime
189 / 3 = 63 is NOT prime
204 / 3 = 68 is NOT prime
207 / 3 = 69 is NOT prime
222 / 3 = 74 is NOT prime
225 / 3 = 75 is NOT prime
228 / 3 = 76 is NOT prime
240 / 3 = 80 is NOT prime
243 / 3 = 81 is NOT prime
246 / 3 = 82 is NOT prime
261 / 3 = 87 is NOT prime
264 / 3 = 88 is NOT prime
282 / 3 = 94 is NOT prime
285 / 3 = 95 is NOT prime
288 / 3 = 96 is NOT prime
300 / 3 = 100 is NOT prime
306 / 3 = 102 is NOT prime
324 / 3 = 108 is NOT prime
342 / 3 = 114 is NOT prime
345 / 3 = 115 is NOT prime
348 / 3 = 116 is NOT prime
360 / 3 = 120 is NOT prime
363 / 3 = 121 is NOT prime
366 / 3 = 122 is NOT prime
369 / 3 = 123 is NOT prime
384 / 3 = 128 is NOT prime
387 / 3 = 129 is NOT prime
402 / 3 = 134 is NOT prime
405 / 3 = 135 is NOT prime
408 / 3 = 136 is NOT prime
420 / 3 = 140 is NOT prime
423 / 3 = 141 is NOT prime
426 / 3 = 142 is NOT prime
429 / 3 = 143 is NOT prime
441 / 3 = 147 is NOT prime
444 / 3 = 148 is NOT prime
462 / 3 = 154 is NOT prime
465 / 3 = 155 is NOT prime
468 / 3 = 156 is NOT prime
480 / 3 = 160 is NOT prime
483 / 3 = 161 is NOT prime
486 / 3 = 162 is NOT prime
504 / 3 = 168 is NOT prime
507 / 3 = 169 is NOT prime
522 / 3 = 174 is NOT prime
525 / 3 = 175 is NOT prime
528 / 3 = 176 is NOT prime
540 / 3 = 180 is NOT prime
546 / 3 = 182 is NOT prime
549 / 3 = 183 is NOT prime
561 / 3 = 187 is NOT prime
564 / 3 = 188 is NOT prime
567 / 3 = 189 is NOT prime
582 / 3 = 194 is NOT prime
585 / 3 = 195 is NOT prime
588 / 3 = 196 is NOT prime
600 / 3 = 200 is NOT prime
603 / 3 = 201 is NOT prime
606 / 3 = 202 is NOT prime
609 / 3 = 203 is NOT prime
621 / 3 = 207 is NOT prime
624 / 3 = 208 is NOT prime
627 / 3 = 209 is NOT prime
642 / 3 = 214 is NOT prime
645 / 3 = 215 is NOT prime
648 / 3 = 216 is NOT prime
660 / 3 = 220 is NOT prime
663 / 3 = 221 is NOT prime
666 / 3 = 222 is NOT prime
684 / 3 = 228 is NOT prime
702 / 3 = 234 is NOT prime
705 / 3 = 235 is NOT prime
708 / 3 = 236 is NOT prime
720 / 3 = 240 is NOT prime
726 / 3 = 242 is NOT prime
729 / 3 = 243 is NOT prime
741 / 3 = 247 is NOT prime
744 / 3 = 248 is NOT prime
747 / 3 = 249 is NOT prime
762 / 3 = 254 is NOT prime
765 / 3 = 255 is NOT prime
768 / 3 = 256 is NOT prime
780 / 3 = 260 is NOT prime
783 / 3 = 261 is NOT prime
786 / 3 = 262 is NOT prime
801 / 3 = 267 is NOT prime
804 / 3 = 268 is NOT prime
822 / 3 = 274 is NOT prime
825 / 3 = 275 is NOT prime
828 / 3 = 276 is NOT prime
840 / 3 = 280 is NOT prime
846 / 3 = 282 is NOT prime
861 / 3 = 287 is NOT prime
864 / 3 = 288 is NOT prime
867 / 3 = 289 is NOT prime
882 / 3 = 294 is NOT prime
885 / 3 = 295 is NOT prime
888 / 3 = 296 is NOT prime
900 / 3 = 300 is NOT prime
903 / 3 = 301 is NOT prime
906 / 3 = 302 is NOT prime
909 / 3 = 303 is NOT prime
924 / 3 = 308 is NOT prime
927 / 3 = 309 is NOT prime
942 / 3 = 314 is NOT prime
945 / 3 = 315 is NOT prime
948 / 3 = 316 is NOT prime
960 / 3 = 320 is NOT prime
963 / 3 = 321 is NOT prime
966 / 3 = 322 is NOT prime
969 / 3 = 323 is NOT prime
981 / 3 = 327 is NOT prime
984 / 3 = 328 is NOT prime
987 / 3 = 329 is NOT prime
-------------------------------------------------------------------------------
STRONG HARSHADS:
[2, 3, 5, 7, 10, 14, 22, 26, 34, 38, 46, 58, 62, 74, 82, 86, 94, 123, 129, 141, 183, 201, 249, 267, 303, 309, 321, 327, 381, 447, 489, 501, 543, 669, 681, 687, 723, 789, 807, 843, 849, 921]
-------------------------------------------------------------------------------
21 is NOT prime
23 is prime
27 is NOT prime
29 is prime
31 is prime
33 is NOT prime
37 is prime
39 is NOT prime
51 is NOT prime
53 is prime
57 is NOT prime
59 is prime
71 is prime
73 is prime
77 is NOT prime
79 is prime
101 is prime
103 is prime
107 is prime
109 is prime
141 is NOT prime
143 is NOT prime
147 is NOT prime
149 is prime
221 is NOT prime
223 is prime
227 is prime
229 is prime
261 is NOT prime
263 is prime
267 is NOT prime
269 is prime
341 is NOT prime
343 is NOT prime
347 is prime
349 is prime
381 is NOT prime
383 is prime
387 is NOT prime
389 is prime
461 is prime
463 is prime
467 is prime
469 is NOT prime
581 is NOT prime
583 is NOT prime
587 is prime
589 is NOT prime
621 is NOT prime
623 is NOT prime
627 is NOT prime
629 is NOT prime
741 is NOT prime
743 is prime
747 is NOT prime
749 is NOT prime
821 is prime
823 is prime
827 is prime
829 is prime
861 is NOT prime
863 is prime
867 is NOT prime
869 is NOT prime
941 is prime
943 is NOT prime
947 is prime
949 is NOT prime
1231 is prime
1233 is NOT prime
1237 is prime
1239 is NOT prime
1291 is prime
1293 is NOT prime
1297 is prime
1299 is NOT prime
1411 is NOT prime
1413 is NOT prime
1417 is NOT prime
1419 is NOT prime
1831 is prime
1833 is NOT prime
1837 is NOT prime
1839 is NOT prime
2011 is prime
2013 is NOT prime
2017 is prime
2019 is NOT prime
2491 is NOT prime
2493 is NOT prime
2497 is NOT prime
2499 is NOT prime
2671 is prime
2673 is NOT prime
2677 is prime
2679 is NOT prime
3031 is NOT prime
3033 is NOT prime
3037 is prime
3039 is NOT prime
3091 is NOT prime
3093 is NOT prime
3097 is NOT prime
3099 is NOT prime
3211 is NOT prime
3213 is NOT prime
3217 is prime
3219 is NOT prime
3271 is prime
3273 is NOT prime
3277 is NOT prime
3279 is NOT prime
3811 is NOT prime
3813 is NOT prime
3817 is NOT prime
3819 is NOT prime
4471 is NOT prime
4473 is NOT prime
4477 is NOT prime
4479 is NOT prime
4891 is NOT prime
4893 is NOT prime
4897 is NOT prime
4899 is NOT prime
5011 is prime
5013 is NOT prime
5017 is NOT prime
5019 is NOT prime
5431 is prime
5433 is NOT prime
5437 is prime
5439 is NOT prime
6691 is prime
6693 is NOT prime
6697 is NOT prime
6699 is NOT prime
6811 is NOT prime
6813 is NOT prime
6817 is NOT prime
6819 is NOT prime
6871 is prime
6873 is NOT prime
6877 is NOT prime
6879 is NOT prime
7231 is NOT prime
7233 is NOT prime
7237 is prime
7239 is NOT prime
7891 is NOT prime
7893 is NOT prime
7897 is NOT prime
7899 is NOT prime
8071 is NOT prime
8073 is NOT prime
8077 is NOT prime
8079 is NOT prime
8431 is prime
8433 is NOT prime
8437 is NOT prime
8439 is NOT prime
8491 is NOT prime
8493 is NOT prime
8497 is NOT prime
8499 is NOT prime
9211 is NOT prime
9213 is NOT prime
9217 is NOT prime
9219 is NOT prime
-------------------------------------------------------------------------------
RESULT:
83372 [23, 29, 31, 37, 53, 59, 71, 73, 79, 101, 103, 107, 109, 149, 223, 227, 229, 263, 269, 347, 349, 383, 389, 461, 463, 467, 587, 743, 821, 823, 827, 829, 863, 941, 947, 1231, 1237, 1291, 1297, 1831, 2011, 2017, 2671, 2677, 3037, 3217, 3271, 5011, 5431, 5437, 6691, 6871, 7237, 8431]

"""
