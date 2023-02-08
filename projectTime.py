from datetime import datetime


def realTime():
    now = datetime.now()
    dtString = now.strftime('%H:%M:%S')
    return dtString
def realDate():
    now = datetime.now()
    dtString = now.strftime('%d/%m/%y')
    return dtString