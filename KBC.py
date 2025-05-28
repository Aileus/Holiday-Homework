import random
def welcome():
    print("Welcome to Kaun Banega Crorepati (KBC)!")
    print("You will be presented with multiple choice questions.")
    print("Type 1-4 to answer each question.")
    print("You get +10 points for a correct answer and -5 for a wrong answer.")
    print("Good luck!\n")

welcome()

def KBC(no_of_ques):
    with open(r'E:\Coding\Coding\Python\Holiday Homework\ques.txt', 'r') as f:
        data = f.read()
        list_data = eval(data)
        print(type(list_data))
        exit()
        ques_data = random.sample(list_data,20)
        
        ##### Printing ques and options #####
        for i in range(no_of_ques):
            ques = eval(ques_data[i])
            print(f'Question {i+1}:',ques[0])
            # n += 1
            for i in range(4):
                print(f'{i+1})', ques[1][i])
        #####################################
        ##### Taking the answers ############
            a = int(input('\nEnter your option number: '))
            print('\n')
            if a == 1 or a == 2 or a == 3 or a == 4:
                ans.append(int(a))
            else:
                print('Please enter a valid option!')
                a = int(input('Enter your option number: '))
                print('\n')
                if a == 1 or a == 2 or a == 3 or a == 4:
                    ans.append(int(a))
                else:
                    print('Follow the rules!!')
                    exit()
        #####################################
    return ans   

def check_ans(answ,no_of_ques):
    with open(r'E:\Coding\Coding\Python\Holiday Homework\ques.txt', 'r') as f:
        data = f.readlines()
        correct_ans = []
        for i in range(len(answ)):
            x = eval(data[i])
            options = x[1]
            ans = x[2]
            b = options.index(ans)
            b += 1
            correct_ans.append(b)
        
        nth = ['st','nd','rd','th']
        score = 0
        
        for i in range(no_of_ques):
            x = eval(data[i])
            options = x[1]
            ans = x[2]
            if i < 4:
                if correct_ans[i] == answ[i]:
                    print(f'Your {i+1}{nth[i]} answer was correct\n +10\n')
                    score += 10
                else:
                    print(f'Your {i+1}{nth[i]} answer was incorrect\n -5')
                    print(f'The correct answer was: "{ans}"\n')
                    score -= 5
                    
            elif i >= 4:
                if correct_ans[i] == answ[i]:
                    print(f'Your {i+1}{nth[3]} answer was correct\n +10\n')
                    score += 10
                else:
                    print(f'Your {i+1}{nth[3]} answer was incorrect\n -5')
                    print(f'The correct answer was: "{ans}"\n')
                    score -= 5
    print(f'You scored {score} out of {no_of_ques*10}')
                
                    
 
n = 2
answers = KBC(n)
check_ans(answers,n)