#Function

# Non Input
from datetime import datetime
from fridayspeaks import Say
import wikipedia

def Time():
    time = datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def NonInputExecution(query):
    query = str(query)
    if "time" in query:
        Time()
    elif "date" in query:
        Date()
#Input

def InputExecution(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("","")
        result = wikipedia.summary(name)
        print(result)
        Say(result)        
