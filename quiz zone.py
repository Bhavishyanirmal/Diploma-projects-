import Qmodule


def level():
    
    print("There are Four Levels To Play the Quiz!")
    print("1. Easy\n2. Medium\n3. Hard\n4. Logical")
    
    try:
        level_choice = int(input("Enter Your Level (1-4):\n"))
        
        if level_choice == 1:
            print("You Have Chosen Easy Level\n")
            print("You Will Get 1 Point For Each Correct Answer\n")
            print("You Will Get 0 Points For Each Wrong Answer\n")
            score=Qmodule.Easy()
            print("Your Total Score is:",score)
           
        
        elif level_choice == 2:
            print("You Have Chosen Medium Level\n")
            print("You Will Get 1 Points For Each Correct Answer\n")
            print("You Will Get 0 Points For Each Wrong Answer\n")
            score=Qmodule.Medium()
            print("Your Total Score is:",score)
        
        elif level_choice == 3:
            print("You Have Chosen Hard Level\n")
            print("You Will Get 1 Points For Each Correct Answer\n")
            print("You Will Get 0 Points For Each Wrong Answer\n")
            score=Qmodule.Hard()
            print("Your Total Score is:",score)
        
        elif level_choice == 4:
            print("You Have Chosen Logical Level\n")
            print("You Will Get 1 Points For Each Correct Answer\n")
            print("You Will Get 0 Points For Each Wrong Answer\n")
            score=Qmodule.Logical()
            print("Your Total Score is:",score)
        
        else:
            print("Wrong Option! Please choose a level between 1 and 4.")
            level()

    except ValueError:
        print("Invalid input! Please enter a number.")
        level()





# Main Quiz Code
start_quiz=1
while(start_quiz!=0):
    print("\t\t\tWelcome to the World of Quiz!\n")
    start_quiz= int(input("If you want to start the quiz, enter 1,else enter 0: "))

    if start_quiz == 1:
        print("")
        print("Quiz Started!\n")
        level()
    elif(start_quiz==0):
        print("thank you for watched my quiz")
        start_quiz=0
    else:
        print('re-renter the option:')






                (Qmodule)



def Easy():
    score = 0
    unique=0
    print("Welcome to the Quiz With Easy Mode\n")
    
    # Question 1
    answer = input("->1. What is the capital of France?\n(a) London\n(b) Berlin\n(c) Paris\n(d) Madrid\nYour answer: ")
    if answer.lower() == 'c':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (c) Paris.")

    # Question 2
    answer = input("->2. Which data structure uses LIFO (Last In, First Out) principle?\n(a) Stack\n(b) Queue\n(c) List\n(d) Tree\nYour answer: ")
    if answer.lower() == 'a' :
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a) Stack.")

    # Question 3
    answer = input("->3. Who developed the Python programming language?\n(a) James Gosling\n(b) Guido van Rossum\n(c) Dennis Ritchie\n(d) Bjarne Stroustrup\nYour answer: ")
    if answer.lower() == 'b':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (b) Guido van Rossum.")

    # Question 4
    answer = input("->4. What is the output of 5 + 3 * 2?\n(a) 16\n(b) 13\n(c) 11\n(d) 10\nYour answer: ")
    if answer.lower() == 'c':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (c) 11.")

    # Question 5
    answer = input("->5. Which of the following is a mutable data type in Python?\n(a) Tuple\n(b) String\n(c) List\n(d) Integer\nYour answer: ")
    if answer.lower() == 'c':
            score += 1
            print("Correct!","Score = ",score)
    
    else:
        print("Wrong. The correct answer is (c) List.")

    # Question 6
    answer = input("->6. What is the output of len([1, 2, 3, 4])?\n(a) 3\n(b) 4\n(c) 5\n(d) Error\nYour answer: ")
    if answer.lower() == 'b':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (b) 4.")

    # Question 7
    answer = input("->7. Which symbol is used for comments in Python?\n(a) //\n(b) /* */\n(c) #\n(d) <!-- -->\nYour answer: ")
    if answer.lower() == 'c':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (c) #.")

    # Question 8
    answer = input("->8. What is the correct file extension for Python files?\n(a) .py\n(b) .python\n(c) .pt\n(d) .pyc\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a) .py.")

    # Question 9
    answer = input("->9. How do you create a variable with the floating number 2.8 in Python?\n(a) x = 2.8\n(b) x = float(2.8)\n(c) x = '2.8'\n(d) x == 2.8\nYour answer: ")
    if answer.lower() == 'a' or answer.lower() == 'b':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a) x = 2.8. or (b) x = float(2.8)")

    # Question 10
    answer = input("->10. Which keyword is used to define a function in Python?\n(a) def\n(b) function\n(c) func\n(d) define\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a) def.")

    return score


def Medium():
    
    score = 0
    print("Welcome to the  Medium-Level Quiz!\n")
    
    # Question 1
    answer = input("->1. What is the time complexity of searching an element in a balanced binary search tree (BST)?\n(a) O(log n)\n(b) O(n)\n(c) O(n log n)\n(d) O(1)\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a) O(log n).")

    # Question 2
    answer = input("->2. What is the output of the following Python code?\n\nx = [1, 2, 3]\nx.append([4, 5])\nprint(len(x))\n(a) 4\n(b) 5\n(c) 6\n(d) 7\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a) 4. Appending a list adds it as a single element.")

    # Question 3
    answer = input("->3. Which algorithm is used to find the shortest path in a graph?\n(a) Prim's Algorithm\n(b) Dijkstra's Algorithm\n(c) Kruskal's Algorithm\n(d) Floyd-Warshall Algorithm\nYour answer: ")
    if answer.lower() == 'b':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (b) Dijkstra's Algorithm.")

    # Question 4
    answer = input("->4. In Python, what is the result of the expression 4**0.5?\n(a) 2\n(b) 4\n(c) 1\n(d) 16\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
    else:
        print("Wrong. The correct answer is (a) 2. 4**0.5 is the square root of 4.")

    # Question 5
    answer = input("5. In SQL, which of the following is used to remove duplicates from the result set?\n(a) DISTINCT\n(b) UNIQUE\n(c) REMOVE\n(d) NO DUPLICATE\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a) DISTINCT.")

    # Question 6
    answer = input("->6. What is the best case time complexity of QuickSort?\n(a) O(n^2)\n(b) O(n log n)\n(c) O(log n)\n(d) O(n)\nYour answer: ")
    if answer.lower() == 'b':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (b) O(n log n).")

    # Question 7
    answer = input("->7. What is the output of the following Python code?\n\nx = {1, 2, 3}\nx.add(2)\nprint(len(x))\n(a) 3\n(b) 4\n(c) 2\n(d) Error\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
       
    else:
        print("Wrong. The correct answer is (a) 3. Sets do not allow duplicates.")

    # Question 8
    answer = input("->8. Which of the following is an example of a self-referential data structure?\n(a) Linked List\n(b) Array\n(c) Stack\n(d) Queue\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a) Linked List.")

    # Question 9
    answer = input("->9. What is the difference between shallow copy and deep copy in Python?\n(a) Shallow copy creates a reference to the original object, while deep copy creates a new object.\n(b) Shallow copy creates a new object, while deep copy creates a reference to the original object.\n(c) Both are the same.\n(d) None of the above.\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a).")

    # Question 10
    answer = input("->10. What is the purpose of the 'yield' keyword in Python?\n(a) It is used to create a generator.\n(b) It stops the execution of the program.\n(c) It is used to exit a function.\n(d) It returns multiple values from a function.\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a) It is used to create a generator.")
    
    return score

def Hard():
    
    score = 0
    print("Welcome to the Advanced-Level Quiz!\n")
    
    # Question 1
    answer = input("->1. What is the time complexity of finding the median of an unsorted array?\n(a) O(n)\n(b) O(n log n)\n(c) O(log n)\n(d) O(n^2)\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a) O(n) using the Median of Medians algorithm.")

    # Question 2
    answer = input("->2. Given the following Python code, what is the final value of 'result'?\n\nx = [[1, 2], [3, 4]]\nresult = x[0][0] + x[1][1] + x[0][1:]\n(a) 7\n(b) 8\n(c) TypeError\n(d) [3, 4]\nYour answer: ")
    if answer.lower() == 'c':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (c) TypeError. Adding a list slice to an integer raises a TypeError.")

    # Question 3
    answer = input("->3. What is the amortized time complexity of inserting an element into a dynamic array (Python list)?\n(a) O(1)\n(b) O(n)\n(c) O(log n)\n(d) O(n^2)\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a) O(1) amortized time.")

    # Question 4
    answer = input("->4. In Python, what does the following code output?\n\nclass A:\n    def __init__(self):\n        self.a = 'A'\n\nclass B(A):\n    def __init__(self):\n        super().__init__()\n        self.b = 'B'\n\nobj = B()\nprint(obj.a, obj.b)\n(a) AttributeError\n(b) None B\n(c) A B\n(d) None\nYour answer: ")
    if answer.lower() == 'c':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (c) A B. The superclass constructor is called, so 'a' is initialized.")

    # Question 5
    answer = input("->5. Which of the following SQL statements is true when using a subquery with the 'EXISTS' operator?\n(a) The subquery returns a single value.\n(b) The subquery returns TRUE if at least one row exists.\n(c) The subquery returns the number of rows.\n(d) The subquery must return a scalar value.\nYour answer: ")
    if answer.lower() == 'b':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (b) The subquery returns TRUE if at least one row exists.")

    # Question 6
    answer = input("->6. In a red-black tree, what is the maximum number of black nodes between any node and its leaves?\n(a) log n\n(b) n/2\n(c) n/3\n(d) n\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a) log n, where n is the number of nodes.")

    # Question 7
    answer = input("->7. What is the output of the following Python code?\n\nimport threading\nx = 0\ndef increment():\n    global x\n    for _ in range(100000):\n        x += 1\nthreads = [threading.Thread(target=increment) for _ in range(10)]\nfor t in threads:\n    t.start()\nfor t in threads:\n    t.join()\nprint(x)\n(a) 1000000\n(b) Random value due to race condition\n(c) 0\n(d) 10\nYour answer: ")
    if answer.lower() == 'b':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (b) Random value due to race condition. Without locks, threads interfere with each other.")

    # Question 8
    answer = input("->8. In Python, what is the primary difference between a shallow copy and a deep copy?\n(a) Shallow copy copies objects only at the first level, while deep copy copies objects at all levels.\n(b) Shallow copy is faster than deep copy.\n(c) Deep copy allows for copying immutable objects, while shallow copy does not.\n(d) Shallow copy is used only for primitive data types.\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a).")

    # Question 9
    answer = input("->9. What is the time complexity of finding the strongly connected components of a graph using Kosaraju's Algorithm?\n(a) O(n log n)\n(b) O(n)\n(c) O(n + m)\n(d) O(m^2)\nYour answer: ")
    if answer.lower() == 'c':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (c) O(n + m), where n is the number of vertices and m is the number of edges.")

    # Question 10
    answer = input("->10. In Python, what will be the result of the following code?\n\nfrom functools import lru_cache\n@lru_cache(maxsize=None)\ndef fib(n):\n    if n < 2:\n        return n\n    return fib(n-1) + fib(n-2)\nprint(fib(100))\n(a) Takes a long time to compute\n(b) Outputs 100\n(c) Outputs a Fibonacci number in reasonable time\n(d) Outputs None\nYour answer: ")
    if answer.lower() == 'c':
        score += 1
        print("Correct!","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (c) Outputs a Fibonacci number in reasonable time due to memoization with @lru_cache.")

    return score

def Logical():
    
    score = 0
    print("Welcome to the Logical Thinking Quiz!\n")
    
    # Question 1
    answer = input("->1. You have 8 identical balls. One of them is heavier, but you don't know which one. You have a balance scale and can only use it twice. How do you determine which ball is heavier?\n(a) Weigh 3 balls on each side, leaving 2 aside.\n(b) Weigh 4 balls on each side.\n(c) Weigh 2 balls at a time.\n(d) Weigh 3 balls on one side and 1 on the other.\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        print("Correct! In the first weighing, if they balance, the heavier ball is in the two set aside. Weigh them to find the heavier one.","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a).")

    # Question 2
    answer = input("->2. A farmer needs to cross a river with a wolf, a goat, and a cabbage. The boat can carry the farmer and one of the three items at a time. If left alone, the wolf will eat the goat, and the goat will eat the cabbage. How can the farmer cross the river without any losses?\n(a) Take the goat first, then the wolf, then the cabbage.\n(b) Take the cabbage first, then the wolf, then the goat.\n(c) Take the goat first, then return with the wolf, leave the wolf and take the cabbage, then return with the goat.\n(d) Take the wolf first, then the goat, and finally the cabbage.\nYour answer: ")
    if answer.lower() == 'c':
        score += 1
        print("Correct!","Score = ",score)
        print("Correct! This logical sequence prevents the wolf from being left alone with the goat and the goat from being left alone with the cabbage.","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (c).")

    # Question 3
    answer = input("->3. You are blindfolded and have 10 coins in front of you. Five of the coins show heads, and five show tails. You cannot feel or see which coins are heads or tails. How can you divide the coins into two groups so that each group has the same number of heads?\n(a) Divide them randomly.\n(b) Divide them into two groups of five, then flip all coins in one group.\n(c) Put all coins in one pile.\n(d) Keep flipping coins until you are lucky.\nYour answer: ")
    if answer.lower() == 'b':
        score += 1
        print("Correct!","Score = ",score)
        print("Correct! By flipping all coins in one group, you balance the number of heads between the two groups.","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (b).")

    # Question 4
    answer = input("->4. A man looks at a portrait and says, 'Brothers and sisters, I have none. But that man's father is my father's son.' Who is in the portrait?\n(a) His father\n(b) His son\n(c) His brother\n(d) Himself\nYour answer: ")
    if answer.lower() == 'b':
        score += 1
        print("Correct!","Score = ",score)
        print("Correct! 'My father's son' is the man himself, so the man in the portrait is his son.","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (b).")

    # Question 5
    answer = input("->5. You are given two fuses. Each fuse burns for exactly 60 minutes, but not at a constant rate (i.e., one end might burn faster than the other). How can you measure 45 minutes using these two fuses?\n(a) Light one fuse from both ends and the other from one end at the same time.\n(b) Light both fuses from both ends at the same time.\n(c) Light one fuse from one end, wait 15 minutes, and light the other.\n(d) Burn one fuse halfway, then burn the other from both ends.\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        print("Correct! The first fuse will burn in 30 minutes when lit from both ends. When the first fuse finishes, light the other fuse from the other end, and it will burn for 15 more minutes.","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a).")

    # Question 6
    answer = input("->6. You have three light switches outside a room, each controlling one of three bulbs inside the room. You cannot see inside the room while outside. How can you determine which switch controls which bulb if you can only enter the room once?\n(a) Flip all switches on, enter the room.\n(b) Flip one switch on for a while, then turn it off and flip another on before entering.\n(c) Flip two switches on, enter the room, and check the bulbs.\n(d) Turn one switch on and enter the room immediately.\nYour answer: ")
    if answer.lower() == 'b':
        score += 1
        print("Correct!","Score = ",score)
        print("Correct! The bulb that is on corresponds to the switch currently on, the warm bulb corresponds to the switch that was on, and the off and cool bulb corresponds to the switch that was never flipped.","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (b).")
    
        # Question 7
    answer = input("->7. You are on a game show and given three doors: behind one is a car, and behind the others are goats. You pick a door, and the host, who knows what is behind each door, opens one of the other two doors, revealing a goat. You are now given the chance to switch your choice to the remaining door. Should you switch?\n(a) Yes, the probability of winning increases if you switch.\n(b) No, the probability of winning is the same.\n(c) It doesn’t matter whether you switch or not.\n(d) The probability of winning decreases if you switch.\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        print("Correct! This is the Monty Hall problem. Switching gives you a 2/3 chance of winning, while sticking with your original choice gives you only a 1/3 chance.","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a).")

    # Question 8
    answer = input("->8. You are in a room with two doors. One leads to freedom, and the other leads to certain death. There are two guards: one always tells the truth, and the other always lies. You can ask only one question to one of the guards to determine which door leads to freedom. What should you ask?\n(a) 'Which door would the other guard say leads to freedom?'\n(b) 'Is the left door the correct one?'\n(c) 'Do you always tell the truth?'\n(d) 'Which door do you guard?'\nYour answer: ")
    if answer.lower() == 'a':
        score += 1
        print("Correct!","Score = ",score)
        print("Correct! By asking what the other guard would say, you can invert the answer. Both guards will point to the door that leads to death, so you should take the opposite door.","Score = ",score)
        
    else:
        print("Wrong. The correct answer is (a).")

    # Question 9
    answer = input("->9. A train leaves New York at 60 miles per hour heading towards Los Angeles