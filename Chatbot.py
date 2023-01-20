from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

chatBot = ChatBot("My_ChatBot")

trainer = ChatterBotCorpusTrainer(chatBot)

trainer.train("chatterbot.corpus")


while True:
    query = input(">>>")
    print(chatBot.get_response(Statement(text=query, search_text=query)))
