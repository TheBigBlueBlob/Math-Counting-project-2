from random import shuffle, randint

cards = ['J','J','J','J','Q','Q','Q','Q','K','K','K','K']

failures = 0
#heads = 0
trials = 10

for i in range(trials):
    
    shuffle(cards)
    #print(cards)
    for j in range(9):
        if cards[j] + cards[j+1] + cards[j+2] + cards[j+3] == 'JJJJ' or cards[j] + cards[j+1] + cards[j+2] + cards[j+3] == 'QQQQ' or cards[j] + cards[j+1] + cards[j+2] + cards[j+3] == 'KKKK':
            failures+=1
            break

print ((trials-failures)/trials*100, '%')

"""

for i in range(trials):
    
    heads += randint(0,1)
    #print('Heads =', heads,' Tails=', trials-heads)

print('Heads =', heads,' Tails=', trials-heads)
"""


people = ['T','T','T','S','S','S','S','S','S','S','S','S','S','S','S']

failures2 = 0
trials2 = 10



for i in range(trials2):
    
    shuffle(people)
    #print(people)
    for j in range(13):
        if people[j] + people[j+1] + people[j+2] == 'TST' or people[j] + people[j+1] == 'TT':
            failures2+=1
            break

        if  people[13] + people[14] == 'TS':
            failures2+=1
            break     
        
        if people[0] + people[1] == 'ST':
            failures2+=1
            break
print ((trials2-failures2)/trials2*100, '%')

siblings = ['A','A','B','B','C','C','D','D','E','E']

failures3 = 0
trials3 = 10



for i in range(trials3):
    
    shuffle(siblings)
    print(siblings)
    for j in range(7):
        if siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'AABB' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'AACC' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'AADD' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'AAEE' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'BBAA' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'BBCC' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'BBDD' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'BBEE' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'CCAA' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'CCBB' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'CCDD' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'CCEE' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'DDAA' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'DDBB' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'DDCC' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'DDEE' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'EEAA' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'EEBB' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'EECC' or siblings[j] + siblings[j+1] + siblings[j+2] + siblings[j+3] == 'EEDD':
            failures3+=1
            break






print(failures3/trials3)


