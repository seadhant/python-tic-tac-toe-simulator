#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string


# In[2]:


alphabet = ascii_letters()


# In[3]:


alphabet = string.ascii_letters()


# In[5]:


print(alphabet)


# In[6]:


sentence = "Jim quickly realized that the beautiful gowns are expensive"


# In[7]:


letters=list(alphabet)


# In[8]:


print(letters)


# In[9]:


dict(dictionary)


# In[10]:


dictOfWords = { i : 0 for i in letters }


# In[11]:


print(dictOfWords)


# In[12]:


for i in sentence:
    for j in dictOfWords:
        if (i == j):
            dictOfWords[j]+=1


# In[16]:


print(dictOfWords)


# In[14]:


a = """Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."""


# In[15]:


b=list(a)


# In[17]:


dictOfWords = { i : 0 for i in letters }


# In[18]:


print(dictOfWords)


# In[19]:


for i in a:
    for j in dictOfWords:
        if (i == j):
            dictOfWords[j]+=1


# In[20]:


print(dictOfWords)


# In[21]:


import math


# In[22]:


math.pi


# In[23]:


print(math.pi/4)


# In[25]:


import random

random.seed(1) # Fixes the seed of the random number generator.

def rand():
   print(random.uniform(-1,1))
   

rand()


# In[26]:


def distance(x,y):
    a=x[0]-y[0]
    b=x[1]-y[1]
    p=math.sqrt((a*a)+(b*b))
    print(p)
    if 
    
x=(0,0)
y=(1,1)

distance(x,y)


# In[27]:


random.seed(1)
inside = ( random.uniform(-1,1) for i in range(10000) )
def in_circle(x,y=(0,0)):
    a=x[0]-y[0]
    b=x[1]-y[1]
    p=math.sqrt((a*a)+(b*b))
    #print(p)
    if (p<1):
        y=True
        t+=1
    else
        y=False
        f+=1
    return(t,f)

for i in inside:
    in_circle(i)


# In[40]:


random.seed(1)
inside = ( (random.uniform(-1,1),random.uniform(-1,1)) for i in range(10000) )
def in_circle(x):
    a=x[0]-0.0
    b=x[1]-0.0
    p=math.sqrt((a*a)+(b*b))
    
    if (p<1):
        y=True
        
    else:
        y=False
    print(p,y)    
    return(y)

t=0
f=0
for i in inside:
    z=in_circle(i)
    if (z==True):
        t+=1
    else:
        f+=1
print(t,f)


# In[41]:


7790/10000


# In[42]:


0.785398-0.779


# In[47]:


def moving_window_average(x, n_neighbors=2):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    mean_values = []
    for i in range(n):
        temp = x[i: i+width]
        sum_= 0
        for elm in temp:
            sum_+= elm
        mean_values.append(sum_ / width)

    return mean_values

x = [0,10,5,3,1,5]
print(moving_window_average(x, 2))


# In[45]:


numbers = [0,10,5,3,1,5]
window_size = 3

i = 0
moving_averages = []
while i < len(numbers) - window_size + 1:
    this_window = numbers[i : i + window_size]

    window_average = sum(this_window) / window_size
    moving_averages.append(window_average)
    i += 1

print(moving_averages)


# In[50]:


import random

random.seed(1) #Initialize the basic random number generator.

def moving_window_average(x, n_neighbors=2):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    return [sum(x[i:(i+width)]) / width for i in range(n)]
    
    
x=[0,10,5,3,1,5]
print(moving_window_average(x, 2))


# In[49]:


random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.
    
# write your code here!
    
R = 1000
x = [random.uniform(0, 1) for i in range(0, 1000)] #Return a random floating point number N such that
   #a <= N <= b for a <= b 
   #and b <= N <= a for b < a.
Y = [x] + [moving_window_average(x, n_neighbors) for n_neighbors in range(1, 10)]
print(len(Y))


# In[51]:


random.seed(1) #Initialize the basic random number generator.

def moving_window_average(x, n_neighbors=5):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    return [sum(x[i:(i+width)]) / width for i in range(n)]

x = [random.uniform(0, 1) for i in range(0, 1000)]
print(moving_window_average(x, 5))


# In[52]:


def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    return [sum(x[i:(i+width)]) / width for i in range(n)]

random.seed(1)

R = 1000
x = [random.random() for i in range(R)]
Y = [x] + [moving_window_average(x, i) for i in range(1, 10)]

print(Y[5][9])


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
x = np.logspace(0,1,10)
y= x**2
plt.loglog(x,y,"bo-")
plt.show()


# In[3]:


import numpy as np
import matplotlib.pyplot as plt
np.


# In[4]:


import random
random.choice(list([1,2,3,4]))


# In[5]:


import random
sum(random.sample(range(10),10))


# In[6]:


import random
sum(random.choice(range(10),10))


# In[7]:


import random
sum(random.sample(range(10),10))


# In[8]:


import random
sum(random.sample(range(10),10))


# In[9]:


import random
sum(random.choice(range(10))for i in range(10))


# In[10]:


import random
sum(random.choice(range(10))for i in range(10))


# In[11]:


import random
sum(random.choice(range(10))for i in range(10))


# In[1]:


x=numpy.random.normal(1,2,3)
x


# In[2]:


import numpy
import random
x=numpy.random.normal(1,2,3)
x


# In[3]:


import numpy
import random
x=numpy.random.randint(1,5,(2,3))
x


# In[5]:


import numpy as np

def create_board():
    return np.zeros((3,3))

board = create_board()
board


# In[6]:


import numpy as np

def create_board():
    return np.zeros((3,3))

board = create_board()
board

def place(board, player, position):
    if(board[position[0]][position[1]]==0):
        board[position[0]][position[1]]==player
        


# In[26]:


import numpy as np

def create_board():
    return np.zeros((3,3))

def place(board, player, position=(1,1)):
    print(board[position])
    if board[position]==0:
        board[position]=player
        print(board[position])
                
def possibilities(board):
    not_occupied = np.where(board == 0)
    return list(zip(not_occupied[0], not_occupied[1]))
            
board = create_board()
place(board,1,(0,0))
print(possibilities(board))


# In[30]:


import numpy as np
import random

def create_board():
    return np.zeros((3,3))

def place(board, player, position):
    if board[position]==0:
        board[position]=player
                
def possibilities(board):
    not_occupied = np.where(board == 0)
    return list(zip(not_occupied[0], not_occupied[1]))


def random_place(board, player):
    selection = possibilities(board)
    pos = random.choice(selection)
    place(board,player,pos)
    
            
board = create_board()
place(board,1,(0,0))
print(possibilities(board))
random_place(board,2)
print(board)
print(possibilities(board))


# In[64]:



import numpy as np
import random

def create_board():
    return np.zeros((3,3))

def place(board, player, position):
    if board[position]==0:
        board[position]=player
                
def possibilities(board):
    not_occupied = np.where(board == 0)
    return list(zip(not_occupied[0], not_occupied[1]))


def random_place(board, player):
    selection = possibilities(board)
    pos = random.choice(selection)
    place(board,player,pos)
    
    
def check_row(row, player):
    for marker in row:
        if marker != player:
            return False
    return True

def row_win(board, player):
    for row in board:
        if check_row(row, player):
            return True
    return False  

def col_win(board, player):
    for row in board.T:
        if check_row(row, player):
            return True
    return False

def diag_win(board,player):
    main_diag = board.diagonal()
    anti_diag = np.flipud(board).diagonal()[::-1]
    return check_row(main_diag, player) or check_row(anti_diag, player)

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # add your code here!
        a=row_win(board,player)
        b=col_win(board,player)
        c=diag_win(board,player)
        if (a==True or b==True or c==True ):
            return player
        pass
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner
        
#board = create_board()

#print(possibilities(board))

#random_place(board,1)
#random_place(board,2)
#random_place(board,1)
#random_place(board,2)
#random_place(board,1)
#random_place(board,2)

#print(board)
#print(possibilities(board))
#print(evaluate(board))

def play_game():
    board = create_board()
    while True:
        for player in [1, 2]:
            random_place(board, player)
            result = evaluate(board)
            print(board)
            if result != 0:
                return result             
             
#Call play_game once.

#play_game()

def play_strategic_game():
    board = create_board()
    while True:
        for player in [1, 2]:
            x=np.any(board)
            if x == False:
                board[1][1]=1
                pass
            random_place(board, player)
            result = evaluate(board)
            #print(board)
            if result != 0:
                print(result)
                return result 
                
            
q=0
w=0
e=0

for i in range(1000):
    p=play_strategic_game()
    if p==1:
        q+=1
    elif p==2:
        w+=1
    else:
        e+=1
print(q,w,e)


# In[ ]:





# In[ ]:




