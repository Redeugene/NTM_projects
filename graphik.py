import datetime
import pandas as pd
import random
import matplotlib.pyplot as plt
pd.options.display.max_rows = 50
pd.options.display.max_columns = 20
pd.options.display.max_colwidth = 100
pd.options.display.expand_frame_repr = False
def month_(year_,monthh,day_):
 start_=datetime.date(year_,monthh,day_)
 end_=start_.month
 # цикл поиска количества дней в месяце
 if any([end_==1,end_==3,end_==5,end_==7,end_==8,end_==10,end_==12]):
     end_=31
 elif any([end_==4,end_==6,end_==9,end_==11]):
     end_=30
 else:
     end_=28
 end_=datetime.date(year_,monthh,end_) #конец месяца
 month=pd.date_range(start=start_,end=end_) #месяц в цифрах
 a={1:"pn",2:"vt",3:"sr",4:"ch",5:"pt",6:"sb",7:"vs"}
 n=[]
 for c in month:
    n.append(c.isoweekday()) #перевод дней недели в цифры
 k=[]
 for b in n:
   for v,z in a.items():
    if b==v:   
      b=z
      k.append(b)    #перевод месяца из цифр.формата в текстовый
 data=pd.DataFrame(index=month)
 data["day"]=k
 return data
c=month_(2021,5,1)
#класс для записи смен в определенные дни недели
class Ucheba:
    def __init__(self,pn,vt,sr,ch,pt,sb,vs):
        self.pn=pn
        self.vt=vt
        self.sr=sr
        self.ch=ch
        self.pt=pt
        self.sb=sb
        self.vs=vs
    def create(self):
        for k, v in globals().items():
            if v is self:
                for x in c.index:
                    c.loc[c['day']=='pn',k]=self.pn
                    c.loc[c['day']=='vt',k]=self.vt
                    c.loc[c['day']=='sr',k]=self.sr
                    c.loc[c['day']=='ch',k]=self.ch
                    c.loc[c['day']=='pt',k]=self.pt
                    c.loc[c['day']=='sb',k]=self.sb
                    c.loc[c['day']=='vs',k]=self.vs
Natasha=Ucheba('15-23','-','15-23','-','16-23','6-16','6-16')
Gontar=Ucheba("-",'-','-','10-23','-','10-23','10-23')
Natasha.create()
Gontar.create()
#класс для записи смен в определенные дни месяца (0-форс-мажорные дни)
from datetime import datetime
class Dela:
    def __init__(self,*args):
        self.dela_days=[]
        for arg in args:
            arg_time=datetime.strptime(arg,'%d-%m-%Y')
            self.dela_days.append(arg_time)
    def solve(self):
        glob=globals().copy() 
        for k, v in glob.items():
            if v is self:
             for i in self.dela_days:
               for j in c.index:
                   if i==j:
                       c.loc[j,k]=0
Natasha=Dela('29-05-2021','20-05-2021')
Natasha.solve()
Gontar=Dela('22-05-2021')
Gontar.solve()
def lister():
    for i in c.index:
        busy_time=[]
        for j in c.columns[1:3]:
            busy_time.append(c.loc[i,j])
        a,b=tuple(busy_time)
        if (a==0 or a=='-') and (b==0 or b=='-'):
            if c.loc[i,'day']=='sb' or c.loc[i,'day']=='vs' or c.loc[i,'day']=='pt':
                c.loc[i,'busy_time']='6-16,10-23,13-23'
            else:
                c.loc[i,'busy_time']='6-15,10-23,15-23'
        elif str(a).endswith('3') and str(b).endswith('3'):
            c.loc[i,'busy_time']='6-1'+ max(a,b)[1]
        elif str(a).startswith('10') and (b==0 or b=='-'):
            if c.loc[i,'day']=='sb' or c.loc[i,'day']=='vs' or c.loc[i,'day']=='pt':
                c.loc[i,'busy_time']='6-16,13-23'
            else:
                c.loc[i,'busy_time']='6-15,15-23'
        elif (a==0 or a=='-') and str(b).startswith('10'):
            if c.loc[i,'day']=='sb' or c.loc[i,'day']=='vs' or c.loc[i,'day']=='pt':
                c.loc[i,'busy_time']='6-16,13-23'
            else:
                c.loc[i,'busy_time']='6-15,15-23'
        elif str(a).endswith('3') and (b==0 or b=='-'):        
            c.loc[i,'busy_time']='6-1'+str(a[1])+',10-23'
        elif (a==0 or a=='-') and str(b).endswith('3'):
            c.loc[i,'busy_time']='6-1'+str(b[1])+',10-23'
        elif str(a).startswith('6') and (b==0 or b=='-'):
            if c.loc[i,'day']=='sb' or c.loc[i,'day']=='vs' or c.loc[i,'day']=='pt':
                c.loc[i,'busy_time']='10-23,13-23'
            else:
                c.loc[i,'busy_time']='10-23,15-23'
        elif (a==0 or a=='-') and str(b).startswith('6'):
            if c.loc[i,'day']=='sb' or c.loc[i,'day']=='vs' or c.loc[i,'day']=='pt':
                c.loc[i,'busy_time']='10-23,13-23'
            else:
                c.loc[i,'busy_time']='10-23,15-23'
        elif str(a).startswith('6') and str(b).startswith('10'):
            if c.loc[i,'day']=='sb' or c.loc[i,'day']=='vs' or c.loc[i,'day']=='pt':
                c.loc[i,'busy_time']='13-23'
            else:
                c.loc[i,'busy_time']=str(a[-2:])+'23'
        elif str(a).startswith('10') and str(b).startswith('6'):
            if c.loc[i,'day']=='sb' or c.loc[i,'day']=='vs' or c.loc[i,'day']=='pt':
                c.loc[i,'busy_time']='13-23'
            else:
                c.loc[i,'busy_time']=str(b[-2:])+'23'
        elif str(a).startswith('6') and str(b).endswith('3'):
            c.loc[i,'busy_time']='10-23'
        elif str(a).endswith('3') and str(b).startswith('6'):
            c.loc[i,'busy_time']='10-23' 
        else:
            c.loc[i,'busy_time']='NaN'
lister()
def ginny():
 for i in c.index:
     if '6-1' in c.loc[i,'busy_time']:
         c.loc[i,'Ginny']=(c.loc[i,'busy_time'])[:4]
     else:
         c.loc[i,'Ginny']='-'
ginny()
def busy_time2():
    for i in c.index:
        if c.loc[i,'Ginny']==c.loc[i,'busy_time']:
            c.loc[i,'busy_time2']='-'
        elif len(c.loc[i,'Ginny'])>1 and c.loc[i,'Ginny'] in c.loc[i,'busy_time']:
            c.loc[i,'busy_time2']=(c.loc[i,'busy_time'])[5:]
        else:
            c.loc[i,'busy_time2']=c.loc[i,'busy_time']
busy_time2()
Koval=Dela('21-05-2021')
Koval.solve()           
Silen=Dela('05-05-2021')
Silen.solve() 
Boris=Ucheba('8-16','8-16','8-16','8-16','8-16','-','-') 
Boris.create()
def last():
    import datetime
    delta=datetime.timedelta(days=1)
    if c.loc[c.index[0],'busy_time2']=='-':
            c.loc[c.index[0],c.columns[6]]='-'
            c.loc[c.index[0],c.columns[7]]='-'
    else:
            if len(c.loc[c.index[0],'busy_time2'])>5 and (c.loc[c.index[0],c.columns[6]]==0 or c.loc[c.index[0],c.columns[7]]==0):
                c.loc[ic.index[0],c.columns[6]],c.loc[c.index[0],c.columns[7]]="ERROR",'ERROR'
            elif len(c.loc[c.index[0],'busy_time2'])>5:
                c.loc[c.index[0],c.columns[6]],c.loc[c.index[0],c.columns[7]]=(c.loc[i,'busy_time2']).split(',')
            elif c.loc[c.index[0],c.columns[6]]==0:
                c.loc[c.index[0],c.columns[7]]=c.loc[c.index[0],'busy_time2']
            elif c.loc[c.index[0],c.columns[7]]==0:
                c.loc[c.index[0],c.columns[6]]=c.loc[c.index[0],'busy_time2']
            else:
                 c.loc[c.index[0],c.columns[6]]=c.loc[c.index[0],'busy_time2']
                 c.loc[c.index[0],c.columns[7]]='-'
    for i in c.index[1:]:
        if c.loc[i,'busy_time2']=='-':
            c.loc[i,c.columns[6]]='-'
            c.loc[i,c.columns[7]]='-'
        else:
            if len(c.loc[i,'busy_time2'])>5 and (c.loc[i,c.columns[6]]==0 or c.loc[i,c.columns[7]]==0):
                c.loc[i,c.columns[6]],c.loc[i,c.columns[7]]="ERROR",'ERROR'
            elif len(c.loc[i,'busy_time2'])>5:
                c.loc[i,c.columns[6]],c.loc[i,c.columns[7]]=(c.loc[i,'busy_time2']).split(',')
            elif c.loc[i,c.columns[6]]==0:
                c.loc[i,c.columns[7]]=c.loc[i,'busy_time2']
            elif c.loc[i,c.columns[7]]==0:
                c.loc[i,c.columns[6]]=c.loc[i,'busy_time2']
            elif c.loc[i-delta,c.columns[6]]==0 or c.loc[i-delta,c.columns[6]]=='-':
                c.loc[i,c.columns[6]]=c.loc[i,'busy_time2']
                c.loc[i,c.columns[7]]='-'
            else:
                c.loc[i,c.columns[7]]=c.loc[i,'busy_time2'] 
                c.loc[i,c.columns[6]]='-'
last()
def chasy():
    itog={}
    for j in c.columns[[1,2,4,6,7]]:
        res=[]
        for i in c.index:
            if c.loc[i,j]==0 or c.loc[i,j]=='-':
                res.append(0)
            else:
             st,en=(c.loc[i,j]).split('-')
             res.append(int(en)-int(st))
        itog[j]=sum(res)
    itog=pd.Series(itog,name='itog')
    from datetime import datetime
    index_=[]
    for i in c.index:
       k=i.strftime('%d-%m')
       index_.append(k)
    c.index=index_
    m=c.append(itog)
    path='C:\\Users\\pc\\Desktop\\работа\\График сотрудников.xlsx'
    s=m.copy()
    del s['busy_time']
    del s['busy_time2']
    s.to_excel(path)
    return s
print(chasy())
   




        
            
                