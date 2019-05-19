# coding=UTF-8

import data_opration
#
# TEXT = 'Text'
# # 位置
# MAP = 'Map'
# # 名片
# CARD = 'Card'
# # 提示
# NOTE = 'Note'
# # 分享
# SHARING = 'Sharing'
# # 图片
# PICTURE = 'Picture'
# # 语音
# RECORDING = 'Recording'
# # 文件
# ATTACHMENT = 'Attachment'
# # 视频
# VIDEO = 'Video'
# # 好友请求
# FRIENDS = 'Friends'
d1 = {}

d2 = {
    "TEXT": 0,
    "SHARING": 0,
    "PICTURE": 0,
    "RECORDING": 0,
    "ATTACHMENT": 0,
    "MAP": 0,
    "CARD": 0,
    "NOTE": 0,
    "VIDEO": 0
}
#群发言计数
def countNum(msg):

    #   countShareNum(msg,msg.type)
    msg_type = msg.type
    type = msg_type.lower()
    name = msg.member.name

    groupName = msg.chat.name
   # value = data_opration.selectByUserName(name)
    value = data_opration.selectGroupUserCount(name,groupName,None)
    nickName = msg.member.nick_name

    if len(value) == 0:

        data_opration.addDefult(groupName,None,name , nickName);

        #判断类型，更新操作
        data_opration.updateByType(groupName, type,name,1);

    elif len(value) == 1 :
        val = value[0].get(type)
        num = str(int(val) + 1)

        data_opration.updateByType(groupName, type,name,num);
        return
    else:
        return
        #def saveCountNum():





# def countShareNum(msg,type):
#     name = msg.sender.user_name
#
#
#     if (name in d1.keys()):
#          d1[name][type] += 1
#     else:
#         d2[type] = 1;
#         d1.setdefault(name,d2)
#
#     return d2;