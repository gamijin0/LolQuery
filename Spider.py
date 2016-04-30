import requests

class LolSpider:

    #========attr=============
    ServerName = ""
    UserId=""

    User_info_url = "http://API.xunjob.cn/playerinfo.php?" #玩家信息
    Record_url="http://API.xunjob.cn/Record.php?" #战绩信息
    CommonHero_url="http://API.xunjob.cn/Record.php?" #常用英雄
    Heros_url="http://lolbox.duowan.com/new/api/index.php?_do=personal/championslist&" #英雄信息
    Duanwei_url="http://API.xunjob.cn/s5str.php?" #段位信息
    HideRank_url="http://API.xunjob.cn/rank.php?" #隐藏分
    #=======func=============

    def __init__(self,ServerName,UserId):
        #获取用户id和服务器名
        self.ServerName =ServerName
        self.UserId=UserId

    def GetData(self,mode='h'):
        if(mode=='h'):
            #英雄数据
            pass
        elif(mode=='r'):
            #战绩
            pass
        elif(mode=='c'):
            #常用英雄
            pass
        elif(mode=='u'):
            #玩家信息
            pass
        elif(mode=='d'):
            #段位信息
            pass
        elif(mode=='hr'):
            #隐藏分信息
            pass





