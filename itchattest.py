# 直接将联系人发来的信息返回， 复读机
import itchat
from itchat.content import *

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return msg['Text']
# 命令行内显示二维码
# itchat.auto_login(hotReload=True,enableCmdQR=True)
# 退出后暂存登陆状态
itchat.auto_login(hotReload=True)
itchat.run()

#获取一个联系人， 发送消息
import itchat
itchat.auto_login(hotReload=True)
author = itchat.search_friends(name='霍阿敏')[0]
# author.send('你到哪儿了？')
author.send('厉害了')

# 登陆，推出回调方法
import time
import itchat

def lc():
    print('finish login')

def ec():
    print('exit')

itchat.auto_login(loginCallback=lc, exitCallback=ec ,hotReload=True)

itchat.logout


# 群聊@自动回复
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))


itchat.auto_login(hotReload=True)
itchat.run()


# 自动添加好友，并打招呼
import itchat
from itchat.content import *

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')
itchat.auto_login(hotReload=True)
itchat.run()




# 控制台直接打印收发到的消息
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])

itchat.auto_login(hotReload=True)
itchat.run()

# 返回收到信息的微信号
import itchat
from itchat.content import TEXT

@itchat.msg_register(TEXT)
def print_msg_users(msg):
    print(msg.fromUserName)

itchat.auto_login(hotReload=True)
itchat.run()




