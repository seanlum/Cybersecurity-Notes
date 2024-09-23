import sys
def e(f):
  sys.stdout.write('  \'' + f + '\': {\n')

def d():
  sys.stdout.write(',\n')

def j():
  sys.stdout.write('\n  }')

def q():
  sys.stdout.write('{\n')

def r():
  sys.stdout.write('\n}\n')

def a(b, c):
  sys.stdout.write('    \'' + b + '\': [\n');
  for n in c:
    sys.stdout.write('      \'%s-%02d\'' % (b, n))
    if (n == c[len(c)-1]):
      sys.stdout.write('\n')
    else:
      sys.stdout.write(',\n')
  sys.stdout.write('    ]')

def g(h, i):
  e(h)
  n = 0
  for k in i.keys():
    n += 1
    a(h + '.' + k, i[k])
    if n < len(i):
      d()
  j()

def l(m):
  q()
  p = 0
  for n in m.keys():
    p += 1
    g(n, m[n])
    if p < len(m):
      d()
  r()

l({
  'GV': {
    'OC': range(1,6),
    'RM': range(1,8),
    'RR': range(1,5),
    'PO': range(1,3),
    'OV': range(1,4),
    'SC': range(1,11) 
  },
  'ID': {
    'AM': range(1,9),
    'RA': range(1,11),
    'IM': range(1,4)
  },
  'PR': {
    'AA': range(1,7),
    'AT': range(1,3),
    'DS': [1,2,10,11],
    'PS': range(1,7),
    'IR': range(1,5)
  },
  'DE': {
    'CM': [1,2,3,6,9],
    'AE': [2,3,4,6,7,8]
  },
  'RS': {
    'MA': range(1,6),
    'AN': [3,6,7,8],
    'CO': [2,3],
    'MI': [1,2]
  },
  'RC': {
    'RP': range(1,7),
    'CO': [3,4]
  }
})
