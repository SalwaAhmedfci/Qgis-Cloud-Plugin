from typing import List
import json


class DataBase:
    def __init__(self, Dbname, UserName, Password, Port,
                 Host, Dbtype, UserId):
        self.Dbname = Dbname
        self.UserName = UserName
        self.Password = Password
        self.Port = Port
        self.Host = Host
        self.Dbtype = Dbtype
        self.UserId = UserId

    def set_Dbname(self, Dbname):
        self.Dbname = Dbname
    def set_UserName(self, UserName):
        self.UserName = UserName
    def set_Password(self, Password):
        self.Password = Password
    def set_Port(self, Port):
        self.Port = Port
    def set_Host(self, Host):
        self.Host = Host

    # Set Getters

    def get_Dbname(self):
        return self.Dbname
    def get_UserName(self):
        return self.UserName
    def get_Password(self):
        return self.Password
    def get_Port(self):
        return self.Port
    def set_Host(self):
        return self.Host



class CurrentUser:
    def __init__(self, UserName, Email, displayName, Token,
                 FirstName, LastName, PictureUrl, UserType, Role, Id, DataBases: List[DataBase]):
        self.UserName = UserName
        self.Email = Email
        self.Token = Token
        self.displayName = displayName
        self.FirstName = FirstName
        self.LastName = LastName
        self.PictureUrl = PictureUrl
        self.UserType = UserType
        self.Role = Role
        self.Id = Id
        self.DataBases = DataBases

    # set setters
    def set_UserName(self, UserName):
        self.UserName = UserName

    def set_Email(self, Email):
        self.Email = Email

    def set_Token(self, Token):
        self.Token = Token

    def set_displayName(self, displayName):
        self.displayName = displayName

    def set_FirstName(self, FirstName):
        self.FirstName = FirstName

    def set_LastName(self, LastName):
        self.LastName = LastName

    def set_PictureUrl(self, PictureUrl):
        self.PictureUrl = PictureUrl

    def set_UserType(self, UserType):
        self.UserType = UserType

    def set_Role(self, Role):
        self.Role = Role

    def set_UserGeoDatabases(self, UserGeoDatabases):
        self.UserGeoDatabases = UserGeoDatabases

    # Set Getters
    def get_LastName(self):
        return self.LastName
    def get_Token(self):
        return self.Token
    def get_PictureUrl(self):
        return self.PictureUrl

    def get_UserType(self):
        return self.UserType

    def get_Role(self):
        return self.Role

    def get_Id(self):
        return self.Id

    def get_UserGeoDatabases(self):
        return self.UserGeoDatabases


# def serlization:
#     # Serialization
#     json_data = json.dumps(team, default=lambda o: o.__dict__, indent=4)
#     return json_data
# def Deserlization:
#     # Deserialization
#     decoded_team = Team(**json.loads(json_data))
#     return decoded_team
