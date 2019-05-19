# coding=UTF-8

from wxpy import *

import datetime
import schedule
import threading

import data_opration
import time
time.time()
strftime = time.strftime('%Y-%m-%d', time.localtime(time.time()))






# @bot.register()
# def recv_send_msg(msg):
#     print('收到的消息：', msg.text)
#     # msg.reply_file()
#     if msg.sender == gf:
#         msg.forward(bot.file_helper, prefix='女同学留言：')
#         ms = '【测试】好好学习，天天向上！'+dic
#         return ms
#
bot = Bot(cache_path=True)



def job1():
    gf = bot.friends().search('excellent')[0]
    groups = bot.groups()

    for group in groups:
        # if group.name == "生活超市":
        #     continue
        # if group.name == "Home":
        #     continue
        # if group.name != "Test":
        #     continue
        by_group = data_opration.selectByGroup(group.name)
        if len(by_group) > 0:

            str = "{0}消息统计：\n".format(strftime)
            for g in by_group:

                str2 ="{0}在群中贡献，语音{1}条，文字{2}条，图片{3}条，视频{4}条，分享{5}条，位置信息{6}条，文件{7}次\n".format(g.get("userName"),g.get("recording"),g.get("text"),g.get("card"),g.get("video"),g.get("sharing"),g.get("map"),g.get("attachment"))

                str += str2

                #str = '「{0}」在群「{1}」中艾特了你：'.format(g.username, g.name))'


            countInfo = str
            group.send(countInfo)
            gf.send("统计聊天信息定时任务\n"+"群名:"+group.name+"\n"+countInfo)


# def job2():
#     print("I'm working for job2")
#     time.sleep(2)
#     print("job2:", datetime.datetime.now())


def job1_task():
    threading.Thread(target=job1).start()


# def job2_task():
#     threading.Thread(target=job2).start()


def run():
    #schedule.every().day.every(10).seconds.do(job1_task)
    #   schedule.every(1).minute.do(job1_task)
    #schedule.every(5).seconds.do(job1_task)
#    schedule.every().day.at("21:00").do(job1_task)
    schedule.every().day.at("22:30").do(job1_task)
    # schedule.every(10).seconds.do(job2_task)

    while True:
        schedule.run_pending()
        time.sleep(1)


if   __name__ == '__main__' :
    #job1()
    run()