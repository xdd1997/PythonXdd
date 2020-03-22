#本程序可计算六维空间下载一个资源将要消耗的积分
#XiaZaiXiaoHao
import math
def JiFen(XiaZai):
	if math.log(XiaZai+1)/math.log(2) >33:
		bianliang1 = 33
	else:
		bianliang1 = math.log(XiaZai+1)/math.log(2)
	JiFenXiaZai = XiaZai/(34-bianliang1)
	#print(JiFenXiaZai)
	return JiFenXiaZai

#-----------在此输入已下载量 与将要下载量 单位为G--------------
YiDownload = 30.4  #单位为G
WillDownload = 10 #单位为G
#------------勿动下面-----------------------------


print('已下载',YiDownload,'G 已消耗积分数','{:.2f}'.format(JiFen(YiDownload * 1024)))
WillSpent = JiFen((YiDownload+WillDownload) * 1024) - JiFen(YiDownload * 1024)
print('再下载',WillDownload,'G 将消耗积分数', '{:.2f}'.format(WillSpent))


