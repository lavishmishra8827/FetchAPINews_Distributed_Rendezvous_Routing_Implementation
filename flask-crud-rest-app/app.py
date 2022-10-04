from flask import Flask,render_template,request,redirect,url_for
import logging as logger
import requests
logger.basicConfig(level="DEBUG")
import sys
import os
import json
current_port=5000
if 'port' in os.environ:
    current_port=os.environ['port']
else:
    print("didn't got port in environment variables and thus setting it to default value ",current_port)
config_write={}
config_write['port']=current_port
with open("config_file.json","w") as config_write_file:
    json.dump(config_write,config_write_file)
    
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')
'''
@app.route('/subscribeUnsubscribe',methods=["GET","POST"])
def subscribeUnsubscribe():
    userId=request.form['userid']
    topic_given=request.form['topic']
    topic_splitted=topic_given.split('_')
    subscribe_or_unsubscribe=topic_splitted[0]
    topic="_".join(topic_splitted[1:])
'''    
@app.route('/fetchFeeds',methods=["GET", "POST"])
def fetchFeeds():
    userID=request.form['userid']
    topic=request.form['topic']
    #lst=[['lavishmi','Lavish Mishra'],['sakshimo','Sakshi Modi']]
    #r = requests.get("http://localhost:"+str(current_port)+"/FetchFromDatabase/")
    formdata={'userid':userID,'topic':topic,'portno':current_port}
    print("current_port is ",current_port)
    r = requests.post("http://localhost:"+str(current_port)+"/FetchFromDatabase/",data=formdata)
    print("r now is",r.json())
    print(r.status_code)
    
    if r.status_code!=200:
        logger.debug("Status code is {}".format(r.status_code))
        r_json=r.json()
        if r_json['lst']=='topic not present':
            max_port_avl=r_json['max_port_no']
            min_port_avl=r_json['min_port_no']
            print('max_port_avl=',max_port_avl,'min_port_avl',min_port_avl)
            next_port=int(current_port)+1
            while(next_port!=current_port):
                if next_port>=max_port_avl:
                    next_port=min_port_avl
                else:
                    next_port+=1
                print("checking now on port",5001)
                formdata['portno']=next_port
                r=requests.post("http://host.docker.internal:"+str(next_port)+"/FetchFromDatabase/",data=formdata)
                if r.status_code==200:
                    break
                    print("r from port ",next_port," is ",r)
            
            
    data_dict=r.json()
    
    return render_template('front.html',data_dict=data_dict,userID=userID)
@app.route('/signup')
def signup():
    return render_template('signup.html')
    
@app.route('/portal')
def portal():
    return render_template('portal.html')
    
@app.route('/logout')
def logout():
    return redirect(url_for('home'))


if __name__=="__main__":
    
    logger.debug("Starting the application")
    from api import *
    '''
    if len(sys.argv)>1:
        port=int(sys.argv[1])
    '''
    #print("value of port environment variable is ",os.environ['port'])
    app.run(port=current_port,debug=True,use_reloader=True,host="0.0.0.0")
    logger.debug("Application has been started")