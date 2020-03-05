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

def print_range(start, end, list, msg):
    print(msg)
    for val in list[start:end]:
        print('{:>30}'.format(val))

def get_input(problems):
    msg = 'What problem do you want to work on?\n(#/n for next/p for previous): ' 

    dx = 5
    start = 0
    end = dx
    print_range(start, end, problems, "Index....")
    val = input(msg)
    while True:
        try:
            val = int(val)
            return val
        except ValueError:
            if val == 'n':
                start += dx
            elif val == 'p':
                start -= dx
            else:
                print('Input Error. Try again.')
        if start >= len(problems):
            start = 0
        if start < 0:
            start = len(problems) - 5
        end = start + dx
        print_range(start, end, problems, "Index....")
        val = input(msg)

with open("files.txt") as f:
    print("Opening our problem index...")
    problems = f.read().split('\n')

    num = get_input(problems) 

    print('Looking for number {}'.format(num))
    for problem in problems:
        if int(problem[:problem.index(':')]) == num:
            print('Running problem: {}'.format(problem[problem.index(': ')+2:]))
            check_problem(problem[problem.index(': ')+2:    ])
            break
    else:
        print('The problem specified doesn\'t exist')
print('Done!')