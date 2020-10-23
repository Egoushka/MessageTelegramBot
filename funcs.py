from gtts import gTTS
import os

def error_callback(update, context):
    print(str(context.error))


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def echo(update, context):
  myobj = gTTS(text=str(update.message.text), lang='ru', slow=False)
  myobj.save("welcome.mp3")
  audio = open(r'welcome.mp3', 'rb')
  context.bot.send_audio(update.effective_chat.id, audio)
def echo1(update, context):

  context.bot.send_audio(update.effective_chat.id, gTTS(text=str(update.message.text), lang='ru', slow=False).save())

def echo2(update, context):

    if( str(update.message).find("Ливио","ливио")):
        context.bot.send_message(chat_id=update.effective_chat.id, text = str(update.message.from_user.name) + " is fucking gay")
    if(str( update.message.from_user.id) == "305873506"):
        context.bot.send_message(chat_id=update.effective_chat.id, text = str(update.message.from_user.name) + " is fucking gay")
    else:
        context.bot.send_message(chat_id = update.effective_chat.id,text = str(update.message.from_user.name) + " wrote \"" + update.message.text + "\"")


