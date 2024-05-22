import re
import random


def readwechatid(filepath):
    lines = []
    with open(filepath, 'r', encoding='utf-8') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(line)
    return lines


def modify_phone_number(input_file_path, output_file_path, index, amount):
    with open(input_file_path, 'r') as input_file:
        phone_numbers = input_file.readlines()
        phone_numbers = [number.strip() for number in phone_numbers]

    modified_numbers = []
    for number in phone_numbers:
        if len(number) == 11:
            digit = int(number[index])
            digit = (digit + amount) % 10
            modified_number = number[:index] + str(digit) + number[index + 1:]
            modified_numbers.append(modified_number)

    with open(output_file_path, 'a+') as output_file:
        for i in modified_numbers:
            output_file.write(i + '\n')

    # return modified_numbers


def filter_numbers(numbers):
    filtered_numbers = []  # 4set
    pattern = r"\d{4}(\d)\1{3,4}$"  # 匹配末尾4位或5位数字相同的模式
    pattern3 = r"\d{4}(\d)\1{2}$"
    pattern1 = r'^.{6}9'
    newnumber = []  # 3set
    for number in numbers:
        if re.search(pattern, number):
            filtered_numbers.append(number)
        else:
            newnumber.append(number)
    with open('3set.txt', 'w', encoding='utf-8') as done:
        for i in newnumber:
            done.write(i + '\n')
    with open('4set.txt', 'w', encoding='utf-8') as done:
        for i in filtered_numbers:
            done.write(i + '\n')


def numberallocate():
    numbers = []
    mid = []
    with open('hc.txt', 'r', encoding='utf-8') as origin:
        mid = origin.readlines()
        sex = len(mid)
        sex = int(sex)
        sex = sex // 2
        for i in range(sex):
            number = random.choice(mid)
            numbers.append(number)
            mid.remove(number)

    with open('WeChatId.txt', 'a+', encoding='utf-8') as file:
        for i in mid:
            file.write(i)

    with open('forhc.txt', 'a+', encoding='utf-8') as file:
        for i in numbers:
            file.write(i)


if __name__ == '__main__':
    numberallocate()
    # filter_numbers(readwechatid('originid.txt'))
