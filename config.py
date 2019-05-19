# coding=UTF-8

"""项目配置"""

# 图灵机器人，99元一月付费版，尽情享用！
tuling_api_key = '88f17f853d974387af64955bed9466f4'

# 自动回复
is_friend_auto_reply = True  # 好友自动回复
is_group_reply = True  # 此项表示群中是否回复
is_group_at_reply = True  # 上一项开启后此项才生效
is_forward_revoke_msg = True  # 开启防撤回模式
is_forward_group_at_msg = False  # 转发群@我的消息

# 机器人主人
bot_master_name = 'chaojid@bo55'  # 使用备注名更安全，只允许一个，可远程控制机器人，如果不设置(空)则将文件助手设置为管理员，但不具备远程控制功能

# 监听某些好友群聊，如老板
is_listen_friend = True
listen_friend_names = 'lijing|jinliting|Giiho'  # 需要监听的人名称，使用备注名更安全，允许多个用|分隔，如：主管|项目经理|产品狗
listen_friend_groups = 'Home|test|群|1|2|3|4|5|6|7|8|超市|生活|交流|厨房'  # 在这些群里监听好友说的话，匹配模式：包含“唯一集团工作群”的群


# 转发信息至群
is_forward_mode = False  # 打开转发模式，主人发送给机器人的消息都将转发至forward_groups群
forward_groups = 'Python新手交流'  # 需要将消息转发的群，匹配模式同上

# 群分享监控
is_listen_sharing = True
listen_sharing_groups = 'Home|test|群|1|2|3|4|5|6|7|8|超市|生活|交流'  # 监控群分享，匹配模式同上


#连接mysql
mysql_url = "39.104.77.201"
mysql_userName = "root"
mysql_passWd = "976225li"
mysql_port = "3306"
mysql_dbName = "wxrobot"


