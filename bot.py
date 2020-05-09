try:
    # Import packages
    import config
    import json
    import sys
    import os
    import random
    import time

    import vk_api
    import vk_api.vk_api
    from vk_api.bot_longpoll import VkBotLongPoll


    # Server
    class Server:

        def __init__(self, api_token, group_id, server_name: str = "Empty"):
            self.server_name = server_name
            self.vk = vk_api.VkApi(token=api_token)
            self.long_poll = VkBotLongPoll(self.vk, group_id)
            self.vk_api = self.vk.get_api()

        def send(self, peer_id, message=None, attachment=None):
            self.vk_api.messages.send(peer_id=peer_id, message=message, attachment=attachment,
                                      random_id=random.randint(-2135425, 2135425))

        def kick(self, chat_id, member_id):
            self.vk_api.messages.removeChatUser(chat_id=chat_id, member_id=member_id)

        """
        def photos(self, user_id):
            a = vk.method("photos.getMessagesUploadServer")
            #    b = requests.post(a[])
            c
            d
        """

        def start(self):
            # Print if connection established
            print("OK!")
            while True:
                for event in self.long_poll.listen():
                    try:
                        # Import JSON file with roles
                        with open('roles.json') as f:
                            roles = json.load(f)
                        if event.object.action is not None and (event.object.action['type'] == 'chat_kick_user'):
                            self.kick(chat_id=event.object.peer_id - 2000000000, member_id=event.object.from_id)
                        elif event.object.text.lower().startswith("/") or event.object.text.lower().startswith("!"):
                            msg, user_id, peer_id = event.object.text[1:], event.object.from_id, event.object.peer_id
                            msg1 = msg.split()
                            msg2 = ' '.join(msg1[1:])

                            # Activity test
                            if msg.lower() in ['тест']:
                                self.send(peer_id=peer_id, message="OK!")

                            # Show chat ID
                            elif msg.lower() in ['узнать id беседы']:
                                self.send(peer_id=peer_id, message=str(peer_id))

                            # Roles does not work correctly
                            # TODO: fix roles
                            elif msg.lower() in ['узнать роли']:
                                ans = "Admin lv2:\nAdmin lv1:\n"
                                for i in roles["Admin lv2"]:
                                    ans += f"*{i} (vk.users.get(id=i));"
                                ans = "\nAdmin lv1:\n"
                                for i in roles["Admin lv1"]:
                                    ans += f"@id{i} (vk.users.get(id=i));"
                                self.send(peer_id=peer_id, message=ans)

                            # Kick chat user
                            elif msg1[0].lower() in ['кик'] and user_id in "admins" == [config.OWNER_ID]:
                                time.sleep(1)
                                for i in msg2.split():
                                    self.kick(chat_id=peer_id - 2000000000, member_id=i)
                            """
                            # TODO: create photo send command
                            if msg1[0].lower() in ["картинка"]:
                                att = [os.environ['ALBUM_ID']]
                                self.send(peer_id=peer_id, message=att)
                            """
                    except Exception as E:
                        print(E)


    # Api 5.50(callback) и 5.101(longpool)
    moonlight = Server(config.TOKEN, config.GROUP_ID, "moonlight")
    moonlight.start()

except:
    print("\n Переподключение к серверам ВК \n")
    time.sleep(3)
    os.execl(sys.executable, sys.executable, *sys.argv)
