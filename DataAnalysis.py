import pandas as pd
import matplotlib.pyplot as plt

def analysis():

    csv_file='task.csv'
    data=pd.read_csv(csv_file)
    
    titles=data["title"]
    hour=data["hours"]

    x=[]
    y=[]

    x=list(titles)
    y=list(hour)

    plt.pie(y,labels=x,autopct='%.2f%%',shadow=True,startangle=140)
    plt.show()

'''def graph():
    import pandas as pd
    import matplotlib.pyplot as plt

    df=pd.read_csv('task.csv')

    titles=df['title'].tolist()
    hour=df['hours'].tolist()

    plt.plot(titles,hour,linewidth=4,marker='p',markersize=2,label='Task')
    plt.xlabel('Title')
    plt.ylabel('Hours/Mins')
    plt.title('Your Tasks')
    plt.legend(shadow=True)
    plt.grid()
    plt.show()'''

def graph():
    import seaborn
    import pandas
    import matplotlib.pyplot as plt
    csv = pandas.read_csv("C:\\Users\\AKANSHA\\Desktop\\project\\task.csv")
    res = seaborn.barplot(x=csv['title'], y=csv['hours'])
    plt.show()

    

