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
            
            if 'High' in list1:
                print(i+" "+"High")
            elif 'Medium'in list1:
                print(i+" "+"Medium")
            elif 'Low' in list1:
                print(i+" "+"Low")
                  

checkPermission(app_list,p_list)
