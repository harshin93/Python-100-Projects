# A simple Alarm clock sound will play after X number of minutes/seconds or at a perticular time.

from time import localtime, strftime, time, sleep
import winsound


print(strftime("%a %d %b %Y %H:%M:%S",localtime())) #To get local time from your device
current_sec  = int(strftime("%S",localtime()))
current_min  = int(strftime("%M",localtime()))
print(current_min, current_sec)

def myalarm(minute_alarm, second_alarm): 
     additional_time = int(minute_alarm * 60 + second_alarm) #merge minute_alarm and second_alarm into 00:00 and add it to current_time
     print("Sleeping for seconds {}".format(additional_time))
     sleep(additional_time)
     frequency = 2500
     duration = 1000
     winsound.Beep(frequency,duration)

myalarm(0,5)


    
'''
if len(mytime)==3:
        sounds= mytime[0]*60*60+mytime[1]*60+mytime[2]
        time.sleep(sounds)
        frequency = 2500
        duration = 1000
        winsound.Beep(frequency,duration)
    else:
        print("Write the time in correct format")
        
    #except Exception as e:
        #print('this is the exception',e,'please enter correct details')
'''