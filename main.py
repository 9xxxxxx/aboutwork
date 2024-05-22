# coding: utf-8
import random
import time
import uiautomator2 as u2
from datetime import datetime

d = u2.connect()

d.settings['wait_timeout'] = 8


def readwechatid(filepath):
    lines = []
    with open(filepath, 'r', encoding='utf-8') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip()
            if line:
                lines.append(line.strip())
    lines = list(set(lines))
    return lines


def addfriends(wechatid, success, found):
    # 输入要添加的号码
    d.xpath('//*[@resource-id="com.tencent.mm:id/gfl"]').set_text(wechatid)
    # #输入完毕点击下方出现的搜索:xxxxxxxxxxxx
    d.xpath('//*[@resource-id="com.tencent.mm:id/mfg"]/android.widget.RelativeLayout[1]').click()
    # 判断用户状态
    # 等待虚拟页面加载完毕
    time.sleep(2)
    if d(text='发消息').exists:
        print(wechatid + ' is already your friend!')
        with open('log.txt', 'a+', encoding='utf-8') as file:
            file.write(wechatid + ' is already your friend!\n')
        d.xpath('//*[@resource-id="com.tencent.mm:id/hf"]').click()
        return
    if not d(text='添加到通讯录').exists:
        print(wechatid + f"  该用户不存在! not found:No.{found}")
        with open('log.txt', 'a+', encoding='utf-8') as file:
            file.write(wechatid + f"  该用户不存在! not found:No.{found}\n")
        return
    if d(text='操作过于频繁，请稍后再试').exists or d.xpath('//*[@resource-id="com.tencent.mm:id/cam"]').exists:
        print("添加频繁！！")
        d(resourceId="com.tencent.mm:id/b5i").click()
    # #点击接下来要进行的操作按钮 这里是点击添加到通讯录
    d(resourceId="com.tencent.mm:id/o3b").click()
    # 设置好友申请内容
    d(resourceId="com.tencent.mm:id/m9y").set_text(verifyContent)
    # 点击发送
    d.xpath('//*[@resource-id="com.tencent.mm:id/g68"]').click()
    # 点击返回到添加好友页面
    time.sleep(3)
    d.press("back")
    print(wechatid + f' is add successfully! addSuccessful:No.{success}')
    return 1


def main():
    phonelist = readwechatid(file_path)
    # 点击右上角+号
    d.xpath('//*[@resource-id="com.tencent.mm:id/ky9"]').click()
    #  点击添加好友
    d.xpath('//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.ImageView[1]').click()
    # 聚焦输入框
    d.xpath('//*[@resource-id="com.tencent.mm:id/mes"]').click()
    count = 0
    notfound = 1
    success = 1
    pfnumber = None
    try:
        for number in phonelist:
            # number = random.choice(phonelist)
            pfnumber = number
            print(f"当前正在添加的号码：{number}")
            with open('log.txt', 'a+', encoding='utf-8') as file:
                file.write(pfnumber + ' is used!\n')
            phonelist.remove(number)
            if addfriends(number, success, notfound):
                success += 1
            else:
                notfound += 1
            count += 1

    finally:
        print(f'{pfnumber}  最后添加的号码')
        print('此次加人工作结束---------------')
        # phonelist.append(pfnumber)
        with open(file_path, 'w', encoding='utf-8') as done_file:
            for i in phonelist:
                done_file.write(i + '\n')
            # 提示频繁或者出错 返回到微信主界面
            # 检测发送按钮是否存在于当前页面
            if d(resourceId="com.tencent.mm:id/g68").exists:
                d.press("back")
                d.press("back")
                d.press("back")
                d.press("back")
            else:
                d.press("back")
                d.press("back")
                d.press("back")
            print('file modify successfully!')
            print(f'this time add totally {count}')
            print(f'this time add successfully {success}')
            with open('log.txt', 'a+', encoding='utf-8') as file:
                file.write(f'this time add totally {count}\n')
                file.write(f'this time work done! {datetime.now().replace(microsecond=0)} '
                           f'分割线  --------------------------------------------\n')


if __name__ == '__main__':
    # 输出设备信息
    for k, value in d.info.items():
        print(f"{k}: {value}")
    # 设置申请内容
    file_path = 'goodluck.txt'
    verifyContent = '您好，精仿飞天茅台，品质对标正品,降低招待成本，提升饭桌规格，欢迎品鉴！'
    # 主程序
    # 工作文件目录 修改输入文件时切记修改输出文件！！！！
    main()
