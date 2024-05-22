from datetime import datetime


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


def unarymodify(inputpath, output):
    count = 0
    for index in range(3, 7):
        for i in range(1, 10):
            modify_phone_number(inputpath, output, index, i)


def unarymodifyfor3set(inputpath, output):
    count = 0
    for index in range(3, 8):
        for i in range(1, 10):
            modify_phone_number(inputpath, output, index, i)


def dualisticmodify(inputfile, midfile, outputfile, first, second):
    count = 0
    for i in range(1, 10):
        with open(midfile, 'w', encoding='utf-8') as file:
            file.truncate()
        modify_phone_number(inputfile, midfile, first, i)
        for x in range(1, 10):
            modify_phone_number(midfile, outputfile, second, x)


if __name__ == '__main__':
    input_pathfor4 = '4set.txt'
    input_pathfor3 = '3set.txt'
    mid_path = 'mid.txt'
    output_path = 'hc.txt'
    plan = input("请输入你的修改计划：\n0.单元修改for4set.\n1.单元修改for3set.\n2.双元修改.\n")

    if plan == '0':
        # modify for 4set
        print(f'输入源文件为{input_pathfor4},输出文件为{output_path}')
        with open(input_pathfor4, 'r') as f:
            lines = f.readlines()
            line_count = len(lines)
        unarymodify(input_pathfor4, output_path)
        with open('修改日志.txt', 'a+', encoding='utf-8') as f:
            f.write(f"{datetime.now().replace(microsecond=0)}  文件单元修改已完毕，共生成{line_count * 4 * 9}个号码\n")
        print(f'修改成功,共生成{line_count * 4 * 9}个新号码！！！👍👍👍')

    elif plan == '1':
        # modify for 3set
        print(f'输入源文件为{input_pathfor3},输出文件为{output_path}')
        with open(input_pathfor3, 'r') as f:
            lines = f.readlines()
            line_count = len(lines)
        unarymodifyfor3set(input_pathfor3, output_path)
        with open('修改日志.txt', 'a+', encoding='utf-8') as f:
            f.write(f"{datetime.now().replace(microsecond=0)}  文件单元修改已完毕，共生成{line_count * 5 * 9}个号码\n")
        print(f'修改成功,共生成{line_count * 5 * 9}个新号码！！！👍👍👍')

    elif plan == '2':
        # modify for multi index
        index1 = int(input('第一个修改位置😅😅😅：'))
        index2 = int(input('第二个修改位置😅😅😅：'))
        dualisticmodify(input_pathfor4, mid_path, output_path, index1, index2)
        with open('修改日志.txt', 'a+', encoding='utf-8') as f:
            f.write(
                f"{datetime.now().replace(microsecond=0)}  文件双元修改已完毕，修改位置为{index1}位和{index2}位,共生成?个号码\n")
        print(f'修改成功,共生成?个新号码！！！👍👍👍')
