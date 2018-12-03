import itchat
from itchat import *
import json
@itchat.msg_register(itchat.content.TEXT)
def huoam(msg):
    print(json.dumps(msg))
    print(msg)
    print(msg.MsgId)

    print(msg['Text'])
    print(msg['FromUserName'])
    print(msg['ToUserName'])
    print(msg['Content'])
    print(msg['Type'])
    print(msg['ImgStatus'])
    # print(msg['RecommendInfo'])
    # msg.user.send('nice to meet you')

itchat.auto_login(hotReload=True)
# ham = itchat.search_friends(name='甄琛')
# print(ham)
# print(ham[0]['Signature'])
# print(ham.NickName)
itchat.run()
