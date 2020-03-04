import os
from os import path
import subprocess

def check_problem(problem):
    print('Running the java code...')
    if path.exists(problem+'.java'):
        subprocess.run(['javac', problem+'.java'])
    if path.exists(problem+'.class'):
        subprocess.run(['java', problem])
    if path.exists(problem+'.class'):
        os.remove(problem+'.class')
    print('Checking the output...')
    with open('out') as our_output, open(problem+".out") as actual_output:
        index = 0
        error_count = 0
        for our_answer, actual_answer in zip(our_output, actual_output):
            our_answer = our_answer.strip()
            actual_answer = actual_answer.strip()
            if our_answer != actual_answer:
                print('Error for output no. {}'.format(index))
                error_count += 1
            index += 1
        if error_count == 0:
            print('All Good!')
        else:
            print('{} number of errors! See output above!'.format(error_count))
    


num = input('What problem do you want to work on? ')
try:
    num = int(num)
except ValueError:
    print('You must enter an integer!')
    exit()

with open("files.txt") as f:
    print("Opening our problem index...")
    problems = f.read().split('\n')

    print("Index...")
    for problem in problems:
        print('{:>30}'.format(problem))

    print('Looking for number {}'.format(num))
    for problem in problems:
        if int(problem[:problem.index(':')]) == num:
            print('Running problem: {}'.format(problem[problem.index(': ')+2:]))
            check_problem(problem[problem.index(': ')+2:    ])
            break
    else:
        print('The problem specified doesn\'t exist')
print('Done!')