from flask import Flask,render_template,session,send_file
from flask import request as req
import os
import pandas as pd
import re
import urllib
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from googlesearch import search
app=Flask(__name__)
app.secret_key = 'You Will Never Guess'
@app.route("/", methods=['GET', 'POST'])
def upload_file():
    return render_template("file.html")

@app.route("/data", methods=['GET','POST'])
def data():
    if req.method == 'POST':
        file=req.form['upload_file']
        data=pd.read_csv(file)
        data.to_csv("input.csv")
        your_list=[]
        your_list=data.columns.tolist()

        #session['df'] = data.to_dict('list')
        return render_template('projct.html', your_list=your_list)
@app.route("/hs", methods=['GET','POST'])
def dat():
    if req.method == 'POST':
        col1=str(req.form['name1'])
        col2=str(req.form['name2'])
        col3=str(req.form['name3'])
        col4=str(req.form['name5'])
        col5=str(req.form['name6'])
        col6=str(req.form['name7'])
        col7=str(req.form['name8'])
        col8=str(req.form['name9'])
        col9=str(req.form['name10'])
        phone=str(req.form['name4'])
        number1=int(req.form['num1'])
        number2=int(req.form['num2'])
        #dict_ob = session.get('df', None)
        #df = pd.DataFrame(dict_ob)
        df=pd.read_csv('input.csv')
        df[col1].fillna(' ',inplace=True)
        df[col2].fillna(' ',inplace=True)
        df[col3].fillna(' ',inplace=True)
        if(col4 == " "):
            df[col4]=" "
        else:
            df[col4].fillna(' ',inplace=True)
        if(col5 == " "):
            df[col5]=" "
        else:
            df[col5].fillna(' ',inplace=True)
        if(col6 == " "):
            df[col6]=" "
        else:
            df[col6].fillna(' ',inplace=True)
        if(col7 == " "):
            df[col7]=" "
        else:
            df[col7].fillna(' ',inplace=True)
        if(col8 == " "):
            df[col8]=" "
        else:
            df[col8].fillna(' ',inplace=True)
        if(col9 == " "):
            df[col9]=" "
        else:
            df[col9].fillna(' ',inplace=True)
        df[phone]=df[phone].astype('str')
        df['new']=df[col1]+" "+ df[col2]+" "+df[col3]+" "+df[col4]+" "+df[col5]+" "+df[col6]+" "+df[col7]+" "+df[col8]+" "+df[col9]+" "+df[phone]
        df['newcol']=df[col1]+" "+ df[col2]+" "+df[col3]+df[col4]+" "+df[col5]+" "+df[col6]+" "+df[col7]+" "+df[col8]+" "+df[col9]+" PHONE NUMBER "
        def custom_preprocessor(text):
            text = text.lower()
            text = re.sub('\[.*?\]', '', text)
            text = re.sub("\\W"," ",text) # remove special chars
            text = re.sub('https?://\S+|www\.\S+', '', text)
            text = re.sub('<.*?>+', '', text)
            text = re.sub('\n', '', text)
            text = re.sub('[a-z]+', '', text)
            return text
        def get_urls(tag, n, language):
            for url in search(tag, stop=n, lang=language):
                return url
        present=[]
        source=[]
        tele=[]
        finallist=[]
        list=[]
        sourcee=[]
        x=0
        for i in df['new']:
            print("index is ",end=" ")
            print(x)
            final=[]
            i=str(i)
            r = requests.get('https://google.com/search?q='+ i) 
        
            s=r.content
        
            soup = BeautifulSoup(r.content, "html.parser")
            set = soup.find_all("div","BNeawe s3v9rd AP7Wnd")
            length_of_set = len(set)
            
            #print(length_of_set_)
            print("phone number is "+df[phone][x])
            ans=False
            listis=[]
            for links in soup.findAll('div', {'class': 'kCrYT'}):
                for https in links.findAll('a'):
                    listis.append(https.get('href'))
            for y in range(length_of_set):
        
                
                s=(set[y].text)
                #print(set[y].text)
                a=custom_preprocessor(s)
                a=a.replace(" ","")
                el=a.find(df[phone][x])
            
                
            
                if(el!=-1) and y<len(listis)*2:
                    
                    
                    ans=True
                    li=y/2
                    li=int(li)
                    mylink=listis[li]
                    source.append(mylink[7:])
                    break
                    
            
            x=x+1
            if(ans==True):
                answer=False
                print('true')
                present.append("true")
                aurl=""
                aurl=get_urls(i, 1, 'en')
                zi=df[phone][x-1]
                try:
                    f = requests.get(aurl, timeout=8)
                    print(aurl)
                    z = f.text
                    zi = str(zi)
                    print(zi)
                    a = custom_preprocessor(z)
                    a = a.replace(" ", "")
                    el = a.find(zi)

                    if el == -1:
                    #present.append('False')
                        tele.append(' ')
                        sourcee.append(" ")
                        print('*******%%Number Not Found%%%*************')



                    else:
                        sourcee.append(aurl)
                        print('########################&&&&&&Number Matched&&&&&&&&&#############')
                        link=aurl
                        tele.append(' ')
                        answer=True



                except (requests.exceptions.Timeout, requests.exceptions.SSLError, requests.exceptions.ConnectionError): 
                #present.append('False')
                    sourcee.append(" ")
                    finallist.append(' ')
                    print('*******Number Not Found*************')
                    tele.append(' ')
                    continue
                
            else:
                print('false')
                present.append("false")
                source.append(" ")
                sourcee.append(" ")
                ind=0
                df['newcol'][x-1]=str(df['newcol'][x-1])
                url=str('https://google.com/search?q='+str(df['newcol'][x-1]))
                resy = requests.get(url)
                print(df['newcol'][x-1])
                small=df['newcol'][x-1]
                small=small.lower()
                soup = BeautifulSoup(resy.content, "html.parser")
            
                set = soup.find_all('div', {'class': 'kCrYT'})
                length_of_set = len(set)
                print(length_of_set)
                list= soup.find_all("div", {"class":"BNeawe vvjwJb AP7Wnd"})
                length_of_set_=len(list)
                stng=[]
                for y in range(length_of_set):
                    description = set[y].text
                    site = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]',description)
        
                    if len(site)>0:
                        for index in range(len(site)):
                
                            z=custom_preprocessor(site[index])
                            z=z.replace(" ","")
                            
                            if len(z)>9 and len(z)<11: 
                                if len(z)==10 and z[0]!='1':
                                    #zint=z.astype('int')
                                    stng.append(z)
                            print(len(stng))
                            print(len(final))
                            if length_of_set == length_of_set_*2+2 and y==1 and stng.count(z)==1:
                                print(" *******The Numer is present in******* ",end=" ")
                                small=small.replace(","," ")
                                final.append(small)
                                print(small)
                            elif length_of_set == length_of_set_*2+2 and stng.count(z)==1 :
                    
                                print(" *******The Numer is present in**** ",end=" ")
                                smallx=list[int(y/2)-1].text
                                smallx=smallx.replace(","," ")
                        
                                final.append(smallx)
                                print(smallx)
                            
                            elif length_of_set == length_of_set_*2 and stng.count(z)==1:
                                print(" *******The Numer is present in******* ",end=" ")
                                smallx=list[int(y/2)].text
                                smallx=smallx.replace(","," ")
                                final.append(smallx)
                                print(smallx)
                            elif stng.count(z)==1 and len(final)<len(stng):
                                print(" *******The Numer is present in******* ",end=" ")
                                final.append('No')
                                print("No")
                #print(stng)
                    
                freq = {} 
                for item in stng: 
                    if (item in freq): 
                        #item=item.replace(" ","")
                        freq[item] += 1
                    else: 
                        #item=item.replace(" ","")
                        freq[item] = 1
        
                #freq = dict(sorted(freq.items(), key=lambda item: item[1] ,reverse=True))
                
                listex = [] 
                empty=[]
                for key in freq.keys(): 
                
                    s=str(freq[key])
                    listex.append(key+" : "+s)
                print("length of list is ",end=" ")
                print(len(listex))
                print(listex)
                tele.append(listex)
            finallist.append(final)

        df.drop('new',axis='columns',inplace=True)
        df.drop('newcol',axis='columns',inplace=True)

        #df=df[number1:number2]

        df['present']=present
        df['source']=source
        df['phonenumber']=tele
        df['checked']=sourcee
        df['headings']=finallist

        df.to_csv('FILTERED.csv')
        df=pd.read_csv('FILTERED.csv')
        df=df[~df['present']]
        df.to_csv('false.csv')
        df = pd.read_csv('false.csv')
        s = df['phonenumber'].str.split(',').apply(pd.Series, 1).stack()
        s.index = s.index.droplevel(-1)
        s.name = 'phonenumber'

        del df['phonenumber']

        #df['phonenumber']=df['phonenumber'].replace("'", "")
        df = df.join(s)
        #df['phonenumber']=df['phonenumber'].str.strip('[]')
        df.to_csv('false1.csv')
        df = pd.read_csv('false.csv')
        df.drop(['phonenumber'], axis=1)
        df['headings']=df['headings'].str.strip('[]')
        s = df['headings'].str.split(',').apply(pd.Series, 1).stack()
        s.index = s.index.droplevel(-1)
        s.name = 'headings'
        del df['headings']
        df = df.join(s)
        df.to_csv('checkhead.csv')
        #df=df.drop(['phonenumber','FIRST','MIDDLE','LAST','SUFFIX','CRED','ADDRESS1','ADDRESS2','CITY','STATE','ZIP','PHONE1','present','source'], axis=1)
        #df=df.drop(['MASTER_KEY','OriginatedBy','AgeoutFlag','COMMENTS','phonenumber','present','PHONE1','PHONE2','PHONE3','PHONE4','FIRST','MIDDLE','LAST','ADDRESS1','ADDRESS2','CITY','STATE','ZIP','source'],axis=1)
        #a = pd.read_csv('cell.csv')

       # a.drop('Unnamed: 0.1',axis=1,inplace=True)
        #a.drop('Unnamed: 0.1.1',axis=1,inplace=True)
        #a.drop('Unnamed: 0',axis=1,inplace=True)
       # a.to_csv('filehead.csv')
        dffalse=pd.read_csv('false1.csv')
        #dffalse['headings']=a['headings']
        #dffalse['headings']=dffalse['headings'].astype(str)
        dffalse.to_csv('trials.csv')

        df=pd.read_csv('FILTERED.csv')
        df=df[df['present']]
        #df['phonenumber']=""
        #df['headings']=""
        df.to_csv('true.csv')
        #df.to_csv('cell.csv')
        a = pd.read_csv('trials.csv')
        b = pd.read_csv('true.csv')

        #values1=a[[  'S. No.','FIRST','MIDDLE','LAST','SUFFIX','CRED','ADDRESS1','ADDRESS2','CITY','STATE','ZIP','PHONE1','present','source','phonenumber','headings']]
        #values2=b[[ 'S. No.','FIRST','MIDDLE','LAST','SUFFIX','CRED','ADDRESS1','ADDRESS2','CITY','STATE','ZIP','PHONE1','present','source','phonenumber','headings']]
        values1=a[['S.No.','MASTER_KEY','OriginatedBy','AgeoutFlag','COMMENTS','PHONE1','PHONE2','PHONE3','PHONE4','FIRST','MIDDLE','LAST','ADDRESS1','ADDRESS2','CITY','STATE','ZIP','phonenumber','present','headings','source','checked']]
        values2=b[['S.No.','MASTER_KEY','OriginatedBy','AgeoutFlag','COMMENTS','PHONE1','PHONE2','PHONE3','PHONE4','FIRST','MIDDLE','LAST','ADDRESS1','ADDRESS2','CITY','STATE','ZIP','phonenumber','present','headings','source','checked']]

        dataframes=[values2,values1]
        join=pd.concat(dataframes)
        join.to_csv('joker.csv')
        df = pd.read_csv('joker.csv')
        str1 = "'"
        str2 = ''
        df['phonenumber'] = df['phonenumber'].str.replace(str1,str2)
        df['headings'] = df['headings'].str.replace(str1,str2)
        df['phonenumber'] = df['phonenumber'].str.strip('[]')
        df['headings']=df['headings'].str.strip('[]')
        df.drop('S.No.',axis=1,inplace=True)
        df.drop('Unnamed: 0',axis=1,inplace=True)
        #df.drop('Unnamed: 0.1',axis=1,inplace=True)
        #df.drop('Unnamed: 0.1.1',axis=1,inplace=True)
        #df.drop('Unnamed: 0',axis=1,inplace=True)
        df.to_csv('outputByFlask_24jan.csv')
        return render_template("download_file.html")

@app.route('/download', methods=['GET'])
def download_file():
    now = datetime.now()
    csv_file = now.strftime("Output_%d-%m-%Y %Hh %Mm %Ss.csv")
    os.rename(r'outputByFlask_24jan.csv',csv_file)
    path = csv_file
    return send_file(os.path.join(path), as_attachment=True, cache_timeout=0)

if __name__ == "__main__":
    app.run(debug=True)
            
