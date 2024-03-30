import re


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

def numberfilter(file):
    result = readwechatid(file)
    result = list(set(result))
    with open(file, 'w+', encoding='utf-8') as file:
        file.truncate()
        for i in result:
            file.write(i + '\n')


# new line 更改倒数第五位
# 第一轮 9变8 其余加1  数值为9的已经加过9和1
# 第二轮 9--> 0 其余加2
# 所有的4位一样数号码倒数第五位单独改变已经用完

# 现在开始倒数第六位 加1加2用过已经
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
    filtered_numbers = []
    pattern = r"\d{4}(\d)\1{3,4}$"  # 匹配末尾4位或5位数字相同的模式
    pattern3 = r"\d{4}(\d)\1{2}$"
    pattern1 = r'^.{6}9'
    newnumber = []
    for number in numbers:
        if re.search(pattern, number):
            filtered_numbers.append(number)
        else:
            newnumber.append(number)
    with open('3set.txt', 'w') as done:
        for i in newnumber:
            done.write(i + '\n')
    return filtered_numbers

res = filter_numbers(readwechatid('originid.txt'))
# 将res的内容写入到done.txt
# with open('3set.txt', 'w') as done:
#     for i in res:
#         done.write(i+'\n')



# number = []
# # 示例输入
# with open('originid.txt', 'r') as file:
#         while True:
#             wxid = file.readline()
#             if not wxid:
#                 break
#             wxid = wxid.strip('\n')
#             number.append(wxid)
#
# res = filter_numbers(number)
# with open('old4.txt', 'w', encoding='utf-8') as file:
#     for i in res:
#         file.write(i + '\n')

def unarymodify(index):
    for i in range(1, 10):
        modify_phone_number('originid.txt', 'goodluck.txt', index, i)


def dualisticmodify(inputfile, midfile, outputfile, first, second):
    for i in range(1, 10):
        with open(midfile, 'w', encoding='utf-8') as file:
            file.truncate()
        modify_phone_number(inputfile, midfile, first, i)
        for x in range(1, 10):
            modify_phone_number(midfile, outputfile, second, x)



