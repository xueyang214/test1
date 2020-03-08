import datetime
import tushare
import tushare as ts

print(tushare.__version__)
 
pro = ts.pro_api('15ceb9f0738a78141878b3a3a22beed3e64c2b67ec2efd3d857f4ed0')


#####计算均线涨跌
def UpDownVal(arr):
    ma5=arr["ma5"][0]
    ma5Last=arr["ma5"][1]
    ma10=arr["ma10"][0]
    ma10Last=arr["ma10"][1]
    val = "WAIT"
    if(ma5>ma10 and  ma5>ma5Last and ma10>ma10Last) :
        val = "BUY"
    if(ma5<ma10 and  ma5<ma5Last and ma10<ma10Last) :
        val = "SELL"       
    return val
#####函数结束

######分析信息 codeStr 代码 buyPrice 买入价格 info 备注
def CodeInfo(codeStr,buyPrice,info):
    #获取数据
    dp月 = ts.get_hist_data(codeStr,ktype='M')   
    dp周 = ts.get_hist_data(codeStr,ktype='W')    
    dp日 = ts.get_hist_data(codeStr,ktype='D')  
    dp分60 = ts.get_hist_data(codeStr,ktype='60')  
    dp分30 = ts.get_hist_data(codeStr,ktype='30') 
    dp分15 = ts.get_hist_data(codeStr,ktype='15') 
    dp分5 = ts.get_hist_data(codeStr,ktype='5') 

    ##计算
    BS月 = UpDownVal(dp月)
    BS周 = UpDownVal(dp周)
    BS日 = UpDownVal(dp日)
    BS60 = UpDownVal(dp分60)
    BS30 = UpDownVal(dp分30)
    BS15 = UpDownVal(dp分15)
    BS5 = UpDownVal(dp分5)

    cost=""
    if(buyPrice !=0):
        cost = str(round(dp日["close"][0]-buyPrice,2))

    info = info + str(round(dp日["close"][0],2))
    ResultStr =info + " 月_" + BS月 +" 周_" + BS周 +" 日_" + BS日 + " 60分_" +BS60  
    ResultStr = ResultStr + " 30分_" +BS30  + " 15分_" +BS15  + " 5分_" +BS5 
    ResultStr = ResultStr + " 当前_" + cost

    print(ResultStr)
    return ResultStr
#########结束


 
 #大盘数据
CodeInfo('sh000001',0,'上证指数_')
CodeInfo('601567',8.45,'三星医疗_') #三星医疗
CodeInfo('601398',5.51,'工商银行_’') #工商银行
CodeInfo('600025',3.95,'华能水电_') #华能水电
#CodeInfo('110022',2.7680,'易基消费') #易基消费
#CodeInfo('515070',1.194,'AI智能') #AI智能

a=3
