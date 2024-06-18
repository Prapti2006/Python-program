"""  A Sober Walk
 Our hoary culture had several great persons since time immemorial and king
 Vikramaditya's nava ratnas (nine gems) belongs to this ilk. They are named in the
 following shloka:
 Among these, Varahamihira was an astrologer of eminence and his book Brihat
 Jataak is recokened as the ultimate authority in astrology. He was once talking
 with Amarasimha, another gem among the nava ratnas and the author of the
 Sanskrit thesaurus, Amarakosha. Amarasimha wanted to know the final position
 of a person, who starts from the origin 0 0 and travels per the following scheme.
 • He first turns and travels 10 units of distance
 • His second turn is upward for 20 units
 • The third turn is to the left for 30 units
 • The fourth turn is downward for 40 units
 • The fifth turn is to the right(again) for 50 units
 …Andthus he travels, every time increasing the travel distance by 10 units.
 Constraints:
 2<=n<=1000
 Input:
 3     """


n =int(input())
c = 'R'
x,y=0,0
for i in range(n):
  if c=='R':
    x = abs(x) + 10
    y = abs(y)
    c ='U'
  elif c=='U':
    y = y + 20
    c = 'L'
  elif c=='L':
    x = -(x + 10)
    c = 'D'
  elif c=='D':
    y = -(y)
    c = 'R'
print(x,y)