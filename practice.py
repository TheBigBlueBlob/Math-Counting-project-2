from random import shuffle, randint

cards = ['J','J','J','J','Q','Q','Q','Q','K','K','K','K']

failures = 0
#heads = 0
trials = 1

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
trials2 = 10000



for i in range(trials2):
    
    shuffle(people)
    #print(people)
    for j in range(13):
        if people[j] + people[j+1] + people[j+2] == 'TST' or people[j] + people[j+1] == 'TT':
            failures2+=1
            break

        if  people[13] + people[14] == 'TS' or people[13] + people[14] == 'ST':
            failures2+=1
            break     
        
        if people[0] + people[1] == 'ST' or people[0] + people[1] == 'TS':
            failures2+=1
            break
print ((trials2-failures2)/trials2*100, '%')

siblings = ['AA','AB','BA','BB','CA','CB','DA','DB','EA','EB']

failures3 = 0
trials3 = 1



for i in range(trials3):
    
    shuffle(siblings)
    #print(siblings)
    for j in range(8):
        if siblings[j] + siblings[j+1] == 'AAAB' or siblings[j] + siblings[j+1] == 'ABAA':
            failures3+=1
            break
    for j in range(8):
        if siblings[j] + siblings[j+1] == 'BABB' or siblings[j] + siblings[j+1] == 'BBBA':
            failures3+=1
            break
    for j in range(8):
        if siblings[j] + siblings[j+1] == 'CACB' or siblings[j] + siblings[j+1] == 'CBCA':
            failures3+=1
            break
    for j in range(8):
        if siblings[j] + siblings[j+1] == 'DADB' or siblings[j] + siblings[j+1] == 'DBDA':
            failures3+=1
            break
    for j in range(8):
        if siblings[j] + siblings[j+1] == 'EAEB' or siblings[j] + siblings[j+1] == 'EBEA':
            failures3+=1
            break

print(failures3/trials3)

siblings2 = ['A','A','B','B','C','C','D','D','E','E']

failures4 = 0
trials4 = 1



for i in range(trials4):
    
    shuffle(siblings2)
    #print(siblings2)
    for j in range(8):
        if siblings2[j] + siblings2[j+1] == 'AA':
            failures4+=1
            break
    for j in range(8):
        if siblings2[j] + siblings2[j+1] == 'BB':
            failures4+=1
            break
    for j in range(8):
        if siblings2[j] + siblings2[j+1] == 'CC':
            failures4+=1
            break
    for j in range(8):
        if siblings2[j] + siblings2[j+1] == 'DD':
            failures4+=1
            break
    for j in range(8):
        if siblings2[j] + siblings2[j+1] == 'EE':
            failures4+=1
            break

print(failures4/trials4)

