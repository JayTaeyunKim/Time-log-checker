from datetime import datetime
import csv
import pandas as pd

today = datetime.today()
filedir = today.strftime("%Y.%m.%d")+'.csv'

start = []
stop = []
mins = []

flag = ' '
for i in range(9999):
    flag = input("press any key to start...")

    if flag == "exit":
        break

    #시작
    current_time = datetime.now()
    start.append(current_time.strftime("%H:%M:%S"))
    minutes = int(round(current_time.timestamp()))
    print("Current Time: ", start[i])

    #멈춤
    flag = input("press any key to stop...")
    current_time = datetime.now()
    stop.append(current_time.strftime("%H:%M:%S"))
    minutes = int(round(current_time.timestamp())) - minutes
    print("Current Time: ", stop[i])

    #총
    mins.append(minutes/60)
    print("Lasted time: ", round(minutes/60, 2))

#마지막 total 저장
sum = sum(mins)
start.append("")
stop.append("")
mins.append('{}h {}m'.format(int(sum/60), int(sum)))
timelog = pd.DataFrame(data={'start': start, 'stop': stop, 'total': mins})

print(timelog)
print('total: {}h {}m'.format(int(sum/60), int(sum)))

#파일로 저장
timelog.to_csv(filedir, mode='a', index=False, encoding='utf8')


