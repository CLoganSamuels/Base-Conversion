#!/bin/python
import random
import sys

#codes to represent question and answer formats
bin_format = 0
dec_format = 1
hex_format = 2


def bin_question(random_octect):
    bin_str = str(bin(random_octect))[2:]
    print('Binary: ' + bin_str)


def dec_question(random_octect):
    dec_str = str(random_octect)
    print("Decimal: " + dec_str)


def hex_question(random_octect):
    hex_str = str(hex(random_octect)[2:])
    print("Hexadecimal: " + hex_str)


def bin_user_answer(solution_value):
    solution = str(bin(solution_value)[2:])
    answer = input("Binary: ")
    check_answer(answer, solution)


def dec_user_answer(solution_value):
    solution = str(solution_value)
    answer = input("Decimal: ")
    check_answer(answer, solution)


def hex_user_answer(solution_value):
    solution = str(hex(solution_value)[2:])
    answer = input("Hexadecimal: ")
    check_answer(answer, solution)


def check_answer(answer, solution):
    if answer == solution:
        print("Correct!")
    else:
        print("Incorrect! The correct answer is " + solution)


def parse_args():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-s": return "S"
        elif sys.argv[1] == "-w": return "W"
    return "D"

class RandomByte:

    def __init__(self, mode="D"):
        self.mode = parse_args()
        self.subnet_answers = (128, 192, 224, 240, 248, 252, 254, 255)
        self.wildcard_answers = (1, 3, 7, 15, 31, 63, 127, 255)
        self.wild = False

    def __call__(self, *args, **kwargs):
        if self.mode == "D":
            return random.randint(0, 255)
        else:
            if self.wild:
                self.wild = False
                return random.choice(self.subnet_answers)
            else: 
                self.wild = True
                return random.choice(self.wildcard_answers)


def main():
    parse_args()
    rand_byte = RandomByte("S")
    while True:
        formats = [bin_format, dec_format, hex_format]
        question_format = formats.pop(random.randint(0, 2))
        answer_format = random.choice(formats)

        answer_key = rand_byte()
        question_functions[question_format](answer_key)
        answer_functions[answer_format](answer_key)
        print("")



question_functions = {
    bin_format: bin_question,
    dec_format: dec_question,
    hex_format: hex_question
}

answer_functions = {
    bin_format: bin_user_answer,
    dec_format: dec_user_answer,
    hex_format: hex_user_answer
}

if __name__=="__main__":
    main()
    
