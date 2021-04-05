import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType


TOKEN = 'e81d81e22420c9656942a929fae5a96cac61d464183120c63b78af72214f2b7131eba8366e3b8d2e513a5'
vk = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk)


def send_message(chat_id, text):
    random_id = random.randint(0, 100000000)
    vk.method('messages.send', {'chat_id': chat_id, 'message': text, 'random_id': random_id})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:
                msg = event.text
                chat_id = event.chat_id
                if '@1пдгр' in msg:
                    send_message(chat_id, '@katezarubina')
                elif '@2пдгр' in msg:
                    send_message(chat_id, 'this msg for the second group')

                #tag_add = event.tagAdd
