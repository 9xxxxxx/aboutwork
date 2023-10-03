# coding: utf-8
import time

import uiautomator2 as u2
import os
d = u2.connect()


# 读取wechatid
def getwechatid(number, filepath):
    if os.path.getsize(filepath):
        return
    idlist = readwechatid(r'newid.txt')
    worklist = []
    for i in range(number):
        idnumber = idlist.pop()
        worklist.append(idnumber)
    with open('newid.txt', 'w+', encoding='utf-8') as file:
        file.truncate(0)
        for i in idlist:
            file.write(i + '\n')
    with open('freshId.txt', 'w+', encoding='utf-8') as file:
        file.truncate(0)
        for i in worklist:
            file.write(i + '\n')


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


def checkuserstatus(wechatid):
    if d.xpath('//*[@resource-id="com.tencent.mm:id/j5_"]/android.widget.ImageView[1]').exists:
        print(wechatid, "该用户不存在")
        d(resourceId="com.tencent.mm:id/apy").click()
        return


def addfriends(wechatid, success, found):
    # doneidlist = readwechatid(done_path)
    # if wechatid in doneidlist:
    #     print(f'this id ({wechatid}) already added')
    #     return
    # 点击账号输入框激活输入，聚焦输入光标
    # d(resourceId="com.tencent.mm:id/eg6").click()
    # 输入要添加的号码
    d.xpath('//*[@resource-id="com.tencent.mm:id/gfl"]').set_text(wechatid)
    # #输入完毕点击下方出现的搜索:xxxxxxxxxxxx
    d.xpath('//*[@resource-id="com.tencent.mm:id/mfg"]/android.widget.RelativeLayout[1]').click()
    # 判断用户状态
    # 等待虚拟页面加载完毕
    time.sleep(2)
    if d(text='发消息').exists:
        print(wechatid + ' is already your friend!')
        d.xpath('//*[@resource-id="com.tencent.mm:id/hf"]').click()
        return
    if not d(text='添加到通讯录').exists:
        print(wechatid + f"  该用户不存在! found:No.{found}")
        return
    # #点击接下来要进行的操作按钮 这里是点击添加到通讯录
    d(resourceId="com.tencent.mm:id/o3b").click()
    # 设置好友申请内容
    d(resourceId="com.tencent.mm:id/m9y").set_text(verifyContent)
    time.sleep(1)
    # 点击发送
    d.xpath('//*[@resource-id="com.tencent.mm:id/g68"]').click()
    time.sleep(3)
    # 点击返回到添加好友页面
    d.press("back")
    print(wechatid + f' is add successfully! addSuccessful:No.{success}')
    return 1


def filterepeat():
    result = readwechatid(r"doneId.txt")
    result = list(set(result))
    with open(r'doneId.txt', 'w+', encoding='utf-8') as file:
        for i in result:
            file.write(i + '\n')


def main():
    phonelist = readwechatid(file_path)
    phonelist = list(set(phonelist))
    # 点击右上角+号
    d.xpath('//*[@resource-id="com.tencent.mm:id/ky9"]').click()
    time.sleep(1)
    #  点击添加好友
    d.xpath('//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.ImageView[1]').click()
    time.sleep(1)
    # 聚焦输入框
    d.xpath('//*[@resource-id="com.tencent.mm:id/mes"]').click()
    time.sleep(1)
    count = 0
    notfound = 1
    success = 1
    try:
        for wechatid in phonelist:
            if addfriends(wechatid, success, notfound):
                success += 1
            else:
                notfound += 1
            phonelist.pop(count)
            count += 1
    finally:
        with open('./freshId.txt', 'w', encoding='utf-8') as done_file:
            done_file.truncate(0)
            for i in phonelist:
                done_file.write(i + '\n')
            # 提示频繁或者出错 返回到微信主界面
            if d(resourceId="com.tencent.mm:id/g68").exists:
                d.press("back")
                d.press("back")
                d.press("back")
                d.press("back")
            else:
                d.press("back")
                d.press("back")
            print(f'this time add totally {count}')
            print(f'this time add successfully {success}')
            print('file modify successfully!')


if __name__ == '__main__':
    # 输出设备信息
    for k, value in d.info.items():
        print(f"{k}: {value}")
    # 设置申请内容
    verifyContent = '您好，低价飞天茅台质量99.9%,对标正品，降低招待成本，提升饭桌规格！'
    # 主程序
    file_path = './freshId.txt'
    getwechatid(360, file_path)
    main()
