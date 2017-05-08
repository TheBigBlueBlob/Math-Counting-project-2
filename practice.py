from random import shuffle, randint

cards = ['J','J','J','J','Q','Q','Q','Q','K','K','K','K']

failures = 0
#heads = 0
trials = 10

for i in range(trials):
    
    shuffle(cards)
    print(cards)
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
    print(people)
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
    for j in range(8):
        if siblings[j] + siblings[j+1] == 'AA':
            failures3+=1
            break
    for j in range(8):
        if siblings[j] + siblings[j+1] == 'BB':
            failures3+=1
            break
    for j in range(8):
        if siblings[j] + siblings[j+1] == 'CC':
            failures3+=1
            break
    for j in range(8):
        if siblings[j] + siblings[j+1] == 'DD':
            failures3+=1
            break
    for j in range(8):
        if siblings[j] + siblings[j+1] == 'EE':
            failures3+=1
            break





print(failures3/trials3)


