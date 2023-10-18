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


file_path = 'originid.txt'


def phonenumberchange():
    newline = readwechatid(file_path)
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
    # 第一轮 9变8 其余加1
    try:
        for i in newline:
            l = list(i)
            if l[-5] == '9':
                l[-5] = '8'
            elif l[-5] == '8':
                l[-5] = '9'
            elif l[-5] == '7':
                l[-5] = '8'
            elif l[-5] == '6':
                l[-5] = '7'
            elif l[-5] == '5':
                l[-5] = '6'
            elif l[-5] == '4':
                l[-5] = '5'
            elif l[-5] == '3':
                l[-5] = '4'
            elif l[-5] == '2':
                l[-5] = '3'
            elif l[-5] == '1':
                l[-5] = '2'
            elif l[-5] == '0':
                l[-5] = '1'
            i = ''.join(l)
            workdone.append(i)
            count += 1
    except IndexError:
        print(f'{count} is wrong!')
    finally:
        print(workdone)
        with open('WeChatid.txt', 'a', encoding='utf-8') as file:
            for i in workdone:
                file.write(i + '\n')


# 483

phonenumberchange()
