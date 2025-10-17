def pract1():
    s = input()
    a = s.split()
    k = 0
    for x in a:
        c = x.strip('.,!?;:').lower()
        if c.startswith('е'):
            k = k + 1
    print(k)

def pract2():
    s = input()
    k = s.count(':')
    n = s.replace(':', '%')
    print(n)
    print(k)

def pract3():
    s = input()
    k = s.count('.')
    n = s.replace('.', '')
    print(n)
    print(k)

def pract4():
    s = input()
    k = s.count('а')
    n = s.replace('а', 'о')
    d = len(s)
    print(n)
    print(k)
    print(d)

def pract5():
    s = input()
    n = s.lower()
    print(n)

def pract6():
    s = input()
    k = s.count('а')
    n = s.replace('а', '')
    print(n)
    print(k)

def pract7():
    s = input()
    n = len(s)
    h = n // 2
    f = s[:h]
    t = s[h:]
    m = f.replace('п', '*')
    r = m + t
    print(r)

def pract8():
    s = input()
    if s.endswith('.'):
        s = s[:-1]
    a = s.split()
    k = len(a)
    print(k)

def pract9():
    s = input()
    w = input()
    a = s.lower().split()
    c = w.lower().strip('.,!?;:')
    k = 0
    for x in a:
        b = x.strip('.,!?;:').lower()
        if b == c:
            k = k + 1
    print(k)

def pract10():
    s = input()
    a = s.split()
    r = []
    for x in a:
        if x:
            n = x[0].upper() + x[1:].lower()
            r.append(n)
    t = ' '.join(r)
    print(t)

def pract11():
    s = input()
    m = 0
    n = 0
    for x in s:
        if x == 'н':
            n = n + 1
            if n > m:
                m = n
        else:
            n = 0
    print(m)
    t = s.replace('!', '.')
    print(t)

def pract12():
    s = input()
    a = s.split()
    r = []
    for x in a:
        c = x.strip('.,!?;:')
        if c.endswith('я'):
            r.append(c)
    for y in r:
        print(y)

def pract13():
    s = input()
    i = s.find('(')
    j = s.find(')')
    if i != -1 and j != -1 and i < j:
        t = s[i+1:j]
        print(t)
    else:
        print("")

def pract14():
    s = input()
    a = s.split()
    r = []
    p = []
    for x in a:
        c = x.strip('.,!?;:').lower()
        if c.startswith('а'):
            r.append(x.strip('.,!?;:'))
        if c.endswith('я'):
            p.append(x.strip('.,!?;:'))
    for y in r:
        print(y)
    for z in p:
        print(z)

def pract15():
    s = input()
    k = s.lower().count('т')
    print(k)

pract2()
