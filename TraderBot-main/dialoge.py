"""
Класс пердназначен для диалога будет иметь три метода,
один который получает с сервера сообщение от пользователя,
другой который отправляет это сообщение пользователю,
в методе run мы соединяем все вместе.

message_for_user это лист который содержит в себе ответы,
на вопросы или команды от пользователя.
"""
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
class State():
    state = None

class Dialoge():
    def __init__(self, message_for_user: list):
        self.message_for_user = message_for_user
        self.scen = " "
        

    #message - сообщение от пользователя, lists - подготовленный диалог    
    def __get_message(self, message: str, lists:list):
        if self.scen is not None:
            for answer in lists:
                if any(token in message for token in answer["tokens"]):
                    if answer["answer"]:
                        return answer["answer"]       
                if answer["scenario"]:
                    self.scen = answer["scenario"]
                    metode = getattr(Dialoge, answer["scenario"])
                    return metode()
            else:
                err = "Bruh"
                return err
        else:
            # переделать
            methode = getattr(Dialoge, self.scen)
            methode(State.state)

    
    def get_trands(state = None):
        # переделать возможно удалить
        if state == "Выбор тренда":
            pass
        if state == "добавить в избранное":
            pass
        else:
            return "Выбор действия"

    def run(self,message_from_user:str):
        message = self.__get_message(message=message_from_user, lists = self.message_for_user)
        return message