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


def phonenumberchange(origin, changed):
    newline = readwechatid(origin)
    # int_str = [int(x) for x in newline]
    print(newline)
    workdone = []
    count = 1
    # 更改的是倒数第四位
    # 第一次9变成8 其余加1
    # 第二次是其余减1 9变成1
    # 第三次其余减2 9变成0
    # 第四其余减3 9变成2
    # 第五次其余减4 9--> 3
    # 第六次其余减5 9--> 4
    # 第七次其余减6 9 --> 5

    # new line 更改倒数第五位
    # 第一轮 9变8 其余加1 9 + 9
    # 第二轮 9--> 0 其余加2 9 +1
    try:
        for i in newline:
            l = list(i)
            if l[-5] == '9':
                l[-5] = '0'
            elif l[-5] == '8':
                l[-5] = '0'
            elif l[-5] == '7':
                l[-5] = '9'
            elif l[-5] == '6':
                l[-5] = '8'
            elif l[-5] == '5':
                l[-5] = '7'
            elif l[-5] == '4':
                l[-5] = '6'
            elif l[-5] == '3':
                l[-5] = '5'
            elif l[-5] == '2':
                l[-5] = '4'
            elif l[-5] == '1':
                l[-5] = '3'
            elif l[-5] == '0':
                l[-5] = '2'
            i = ''.join(l)
            workdone.append(i)
            count += 1
    except IndexError:
        print(f'{count} is wrong!')
    finally:
        print(workdone)
        with open(changed, 'w+', encoding='utf-8') as file:
            for i in workdone:
                file.write(i + '\n')


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


# newid的倒数第五位所有轮次都加过已经
# newid的倒数第六位已经加到4 还可以加五位 加满了
# res = modify_phone_number('newid.txt','WeChatId.txt', -6, 9)


def filter_numbers(numbers):
    filtered_numbers = []
    pattern = r"\d{4}(\d)\1{3,4}$"  # 匹配末尾4位或5位数字相同的模式
    pattern1 = r'^.{6}9'
    for number in numbers:
        if re.search(pattern1, number):
            filtered_numbers.append(number)
    return filtered_numbers

# res = filter_numbers(readwechatid('old4.txt'))
# # 将res的内容写入到done.txt
# with open('done.txt', 'w') as done:
#     for i in res:
#         done.write(i+'\n')
# 示例输入


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

