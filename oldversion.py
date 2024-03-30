import time
import uiautomator2 as u2
import os
d = u2.connect()


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

def addfriends(wechatid, success, found):
    # doneidlist = readwechatid(done_path)

    # if wechatid in doneidlist:
    #     print(f'this id ({wechatid}) already added')
    #     return
    # 点击账号输入框激活输入，聚焦输入光标
    d(resourceId="com.tencent.mm:id/eg6").click()
    time.sleep(1)
    # 输入要添加的号码
    d.xpath('//*[@resource-id="com.tencent.mm:id/eg6"]').set_text(wechatid)
    # #输入完毕点击下方出现的搜索:xxxxxxxxxxxx
    d.xpath('//*[@resource-id="com.tencent.mm:id/j6x"]/android.widget.RelativeLayout[1]').click()
    # 判断用户状态
    # 等待虚拟页面加载完毕
    time.sleep(3)
    if d(text='发消息').exists:
        print(wechatid + ' is already your friend!')
        d.xpath('//*[@resource-id="com.tencent.mm:id/g1"]').click()
        return
    if not d(text='添加到通讯录').exists:
        print(wechatid + f"  该用户不存在! found:No.{found}")
        return
    # #点击接下来要进行的操作按钮 这里是点击添加到通讯录
    d(resourceId="com.tencent.mm:id/khj").click()
    # 设置好友申请内容
    d(resourceId="com.tencent.mm:id/j0w").set_text(verifyContent)
    time.sleep(2)
    # 点击发送
    d(resourceId="com.tencent.mm:id/e9q").click()
    time.sleep(3)
    # 点击返回到添加好友页面
    d.xpath('//*[@resource-id="com.tencent.mm:id/g1"]').click()
    time.sleep(1)
    print(wechatid + f' is add successfully! addSuccessful:No.{success}')
    return 1


def main():
    phonelist = readwechatid(file_path)
    phonelist = list(set(phonelist))
    # 点击右上角+号
    d(resourceId="com.tencent.mm:id/hy6").click()
    time.sleep(1)
    #  点击添加好友
    d.xpath('//android.widget.ListView/android.widget.LinearLayout[2]').click()
    time.sleep(1)
    # 聚焦输入框
    d(resourceId="com.tencent.mm:id/j69").click()
    time.sleep(1)
    count = 0
    notfound = 1
    success = 1
    pfnumber = None
    try:
        for wechatid in phonelist[:]:
            pfnumber = wechatid
            if addfriends(wechatid, success, notfound):
                success += 1
            else:
                notfound += 1
            phonelist.remove(wechatid)
            count += 1
    finally:
        print('此次加人工作结束----')
        phonelist.append(pfnumber)
        with open(file_path, 'w', encoding='utf-8') as done_file:
            for i in phonelist:
                done_file.write(i + '\n')
            d(resourceId="com.tencent.mm:id/apy").click()
            d(resourceId="com.tencent.mm:id/g1").click()
            print(f'this time add totally {count}')
            print(f'this time add successfully {success}')
            print('file modify successfully!')


if __name__ == '__main__':
    # 输出设备信息
    for k, value in d.info.items():
        print(f"{k}: {value}")
    # 设置申请内容
    verifyContent = '您好，精仿飞天茅台,品质对标正品，价格实惠，欢迎评鉴！'
    # 主程序
    file_path = 'WeChatId.txt'
    main()



