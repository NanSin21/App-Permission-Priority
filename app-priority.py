#Scenario-a program to check priority of applications
#based on their permissions' priorities.

#permission priority list:
p_list={'Camera':'High',
        'Location':'High',
        'Storage':'High',
        'Contact':'Low',
        'Microphone':'Low',
        'Phone':'Low',
        'Call Log':'Medium',
        'SMS':'Medium',
        'Physical':'Medium'}

#application permission list
app_list={'whatsapp':['Camera','Contact','Microphone'],
          'google chrome':['Storage','Location','Phone'],
          'instagram':['Phone','Contact'],
          'inshorts':['Physical','Phone','SMS'],
          'telegram':['SMS','Physical']}

def hasValue(list1, value):
    for i in list1:
        if value==i:
            return 0
        else:
            return 1
            
def checkPermission(app_list,p_list):
        
        for i in app_list.keys():#app_list
            list1=[]
            for p in app_list[i]:#app_list->list values
                
                for k in p_list.keys():#p_list
                    if p==k:
                        if(p_list[p]=='High'):
                            list1.append('High')
                        elif(p_list[p]=='Medium'):
                            list1.append('Medium')
                        else:
                            list1.append('Low')
            
            if hasValue(list1,'High')==0:
                print(i+" "+"High")
            elif hasValue(list1,'Medium')==0:
                print(i+" "+"Medium")
            elif hasValue(list1,'Low')==0:
                print(i+" "+"Low")
##            print(list1)
            
            
            
                        

                    

checkPermission(app_list,p_list)
