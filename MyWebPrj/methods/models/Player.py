from methods.models.GameRoom import GameRoom
from methods.models.Characters import *

class Player(object):
    """玩家类"""
    __RoomID = ''
    __Character = None
    def __init__(self,ID,Username):
        self.__ID=ID
        self.__Username=Username

    def CreateRoom(self,PlayerNumber):
        Room=GameRoom(self,PlayerNumber)
        self.__RoomID=Room.RoomID
        return Room

    def JoinRoom(self,RoomID):
        try:
            Room=GameRoom.Rooms[RoomID]
        except Exception:
            return '无该房间号！'
        if len(Room.Players) == Room.PlayerNumber:
            return '房间已满，无法加入！'
        else:
            Room.Players[self.__ID]=self
            self.__RoomID=RoomID
            return '加入成功'

    def GetCharacter(self,character):
        self.__Character=character

    @property
    def ID(self):
        return self.__ID

    @property
    def RoomID(self):
        return self.__RoomID

    @property
    def Character(self):
        return self.__Character

    @property
    def Username(self):
        return self.__Username

    @Character.setter
    def Character(self,Character):
        self.__Character=Character

if __name__ == '__main__':
    player=Player(1,'a')
    room = player.CreateRoom(1)
    character=Witch()
    player.Character=character
    print(character.ReturnMedicineStatus())
    print(room.CheckMedicine())



