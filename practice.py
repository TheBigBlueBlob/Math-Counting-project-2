from random import shuffle, randint

trees = ['M','M','M','O','O','O','O','B','B','B','B','B']

failures = 0
trials = 10

for i in range(trials):
    
    shuffle(trees)
    print(trees)
    for j in range(9):
        if trees[j] + trees[j+1] + trees[j+2] + trees[j+3] == 'BBBB':
            failures+=1
            break
        
print ((trials-failures)/trials*100, '%')
