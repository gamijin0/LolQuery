# coding: utf-8
import requests
import json

class LolSpider:

    #========attr=============
    ServerName = ""
    UserId=""
    data=list() #list_of_dict or list_of_str

    User_info_url = "http://API.xunjob.cn/playerinfo.php?" #玩家信息
    Record_url="http://API.xunjob.cn/Record.php?" #战绩信息
    CommonHero_url="http://API.xunjob.cn/Record.php?" #常用英雄
    Heros_url="http://lolbox.duowan.com/new/api/index.php?_do=personal/championslist&serverName={0}&playerName={1}" #英雄信息
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
            TheUrl = self.Heros_url.format(self.ServerName,self.UserId) #格式化url
            requestsRes = requests.post(url=TheUrl) #发起请求
            RowData = json.loads(requestsRes.text) #处理json
            content= RowData['content'] #content为字典组成的list
            self.data = content
            return content
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

    def SettleHerosData(self):
        #用于将list_of_dict整理为list_of_str
        #print(self.data)

        data_str_list =list()
        dict_keys = self.data[0].keys()

        for  i in self.data:
            #print(i)
            tempStr = "英雄名字:"+i['championNameCN']
            tempStr += "  MVP次数:"+str(i['totalMVP'])
            tempStr += "  场均[杀/死/助]:"+str(i['averageKDA'])
            tempStr += "  战损比:"+str(i['averageKDARating'])
            tempStr += "  胜率:"+str(i['winRate'])
            tempStr += "  使用场次:"+str(i['matchStat'])
            tempStr += "  场均输出"+str(i['averageDamage'])
            tempStr += "  场均分钟经济:"+str(i['averageEarn'])
            tempStr += "  场均补兵"+str(i['averageMinionsKilled'])
            data_str_list.append(tempStr)

        print(data_str_list)
        return data_str_list


    def SaveData(self):
        pass



if __name__=="__main__":
    one = LolSpider("祖安","爸爸在等你")
    one.GetData('h')
    one.SettleHerosData()