from random import shuffle, randint

cards = ['J','J','J','J','Q','Q','Q','Q','K','K','K','K']

failures = 0
#heads = 0
trials = 1000

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
    #print(cards)
    for j in range(13):
        if people[j] + people[j+1] + people[j+2] == 'TTT':
            failures2+=1
            break
        
print ((trials2-failures2)/trials2*100, '%')