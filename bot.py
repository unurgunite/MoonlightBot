# Импорт файлов
import json
import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll,VkBotEventType
import random
import requests
import vk_api
# Server
class Server:
    def __init__(self,api_token,group_id,server_name: str="Empty"):
        self.server_name=server_name
        self.vk=vk_api.VkApi(token=api_token)
        self.long_poll=VkBotLongPoll(self.vk,group_id)
        self.vk_api=self.vk.get_api()
    def send(self,peer_id,message=None,attachment=None): self.vk_api.messages.send(peer_id=peer_id,message=message,attachment=attachment,random_id=random.randint(-2135425,2135425))
    def kick(self,chat_id,member_id): self.vk_api.messages.removeChatUser(chat_id=chat_id,member_id=member_id)
    def photos(self, user_id):
        a = vk.method("photos.getMessagesUploadServer")
   #    b = requests.post(a[])
        c 
        d 
    def start(self):
        # Что должен отвечать, если бот запустился
        print("OK!")
        while True:
            for event in self.long_poll.listen():
                try:
                    # Импорт файла JSON
                    with open('roli.json') as f: roli=json.load(f)
                    if event.object.action!=None and (event.object.action['type']=='chat_kick_user'):
                        self.kick(chat_id=event.object.peer_id-2000000000,member_id=event.object.from_id)
                    elif event.object.text.lower().startswith("/") or event.object.text.lower().startswith("!"):
                        msg,user_id,peer_id=event.object.text[1:],event.object.from_id,event.object.peer_id
                        msg1=msg.split()
                        msg2=' '.join(msg1[1:])
                        # Сообщение на сообщение
                        if msg.lower() in ['тест']:
                            self.send(peer_id=peer_id,message="OK!")
                        # Говорит ID беседы
                        elif msg.lower() in ['узнать id беседы']:
                            self.send(peer_id=peer_id,message=str(peer_id))
                        # Все роли (временно не работает, выдает только 1 роль, думаю проблема в id) (нет, прикол не в id которые находятся в json.)
                        elif msg.lower() in ['узнать роли']:
                            ans="Admin lv2:\nAdmin lv1:\n"
                            for i in roli["Admin lv2"]: ans+=f"*{i} (vk.users.get(id=i));"
                            ans="\nAdmin lv1:\n"
                            for i in roli["Admin lv1"]: ans+=f"@id{i} (vk.users.get(id=i));"
                            self.send(peer_id=peer_id,message=ans)
                        # Команда Кик
                        elif msg1[0].lower() in ['кик'] and user_id in "admins" == [233676147]:
                            time.sleep(1)
                            for i in msg2.split(): self.kick(chat_id=peer_id-2000000000,member_id=i)
                        if msg1[0].lower() in ["картинка"]:
                            att=['photo-173756456_456239024']
                            self.send(peer_id=peer_id,message=att)
                except Exception as E: print(E)
# Api 5.50(callback) и 5.101(longpool)
moonlight=Server("ВАШ_ТОКЕН", АЙДИ_ВАШЕЙ_ГРУППЫ, "moonlight")
moonlight.start()