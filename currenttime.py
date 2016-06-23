import time

local_time=time.localtime(time.time())

def get_current_time():
    return time.strftime("%Y-%m-%d %X" , local_time) 
#     return "2016-16-16 12:21"
def get_current_month():
    return "%s" %(local_time[1])

def get_current_hour():
    return "%s" % (local_time[3])
def get_time():
    return time.time()
# if __name__ == '__main__':
#     print get_current_time()
#     print time.time()
#     print time.localtime(time.time())
#     print get_current_month()
#     print get_current_hour()