import time

def in_the_set(article_time):
        timeArray = time.strptime(article_time, "%Y-%m-%d %H:%M:%S")
        
        if (timeArray.tm_year == 2016 and timeArray.tm_mon >= 11) or (timeArray.tm_year == 2017 and timeArray.tm_mon <= 9):
            if timeArray.tm_wday != 2:
                return False
            if (timeArray.tm_hour < 10 or timeArray.tm_hour > 22):
                return False
            return True
        return False


print(in_the_set("2017-12-17 23:51:28"))