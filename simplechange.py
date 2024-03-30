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



def unarymodify(input, output):
    count = 0
    for index in range(3, 7):
        for i in range(1, 10):
            modify_phone_number(input, output, index, i)
            count += 1
    return count


def dualisticmodify(inputfile, midfile, outputfile, first, second):
    count = 0
    for i in range(1, 10):
        with open(midfile, 'w', encoding='utf-8') as file:
            file.truncate()
        modify_phone_number(inputfile, midfile, first, i)
        for x in range(1, 10):
            modify_phone_number(midfile, outputfile, second, x)
            count += 1
    return count


if __name__ == '__main__':
    Count = None
    plan = input("请输入你的修改计划：\n1.单元修改\n2.双元修改\n")
    input_path = '4set.txt'
    mid_path = 'mid.txt'
    output_path = 'goodluck.txt'
    if plan == '1':
        Count = unarymodify(input_path, output_path)
        with open('修改日志.txt', 'a+', encoding='utf-8') as f:
            f.write(f"{datetime.now().replace(microsecond=0)}  文件单元修改已完毕，共生成{Count}个号码\n")
        print(f'修改成功,共生成{Count}个新号码！！！👍👍👍')
    elif plan == '2':
        first = int(input('第一个修改位置😅😅😅：'))
        second = int(input('第二个修改位置😅😅😅：'))
        Count = dualisticmodify(input_path, mid_path, output_path, first, second)
        with open('修改日志.txt', 'a+', encoding='utf-8') as f:
            f.write(f"{datetime.now().replace(microsecond=0)}  文件双元修改已完毕，修改位置为{first}位和{second}位,共生成{Count}个号码\n")
        print(f'修改成功,共生成{Count}个新号码！！！👍👍👍')

