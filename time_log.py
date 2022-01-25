from datetime import datetime
import pandas as pd
import os.path

#파일명 생성
today = datetime.today()
filedir = today.strftime("%Y.%m.%d")+'.csv'

#파일존재 확인
if os.path.exists(filedir) == True:
    timelog = pd.read_csv(filedir)
    timelog = timelog.iloc[:-1, :] #마지막열에 sum을 기록하기 때문에 삭제
    start = []
    stop = []
    mins = []
else:
    start = []
    stop = []
    mins = []
    timelog = pd.DataFrame(data={'start': start, 'stop': stop, 'total': mins})

flag = ' '
for i in range(99999):
    #exit입력시 종료
    if flag == "exit":
        break
    else:
        flag = input("Press enter to start...")
        if flag == "exit":
            break

    #시작
    current_time = datetime.now()
    start.append(current_time.strftime("%H:%M:%S"))
    minutes = int(round(current_time.timestamp()))
    print("Current Time: ", start[i])

    #멈춤
    flag = input("Press enter to stop...")
    current_time = datetime.now()
    stop.append(current_time.strftime("%H:%M:%S"))
    minutes = int(round(current_time.timestamp())) - minutes
    print("Current Time: ", stop[i])

    #총
    mins.append(round(minutes/60, 2))
    print("Lasted time: ", round(minutes/60, 2))

    print()

#마지막 total 저장
sum = sum(timelog['total'].astype(str).astype(float))+sum(mins) #기존 데이터 타입이 object이기 때문에
                                                                # float로 변환하여 새로운 기록과 합함
start.append("")
stop.append("")
mins.append('{}h {}m'.format(int(sum/60), int(sum%60)))

timelog = pd.concat([timelog,
                     pd.DataFrame(data={'start': start, 'stop': stop, 'total': mins})],
                    axis=0, ignore_index=True)

print(timelog)
print('total: {}h {}m'.format(int(sum/60), int(sum%60)))

int_date = today.year*10000 + today.month*100 + today.day
if os.path.exists('기록.csv') == True: #기록 파일이 있다면
    history = pd.read_csv('기록.csv')

    if history.iloc[-1, 0] == int_date: #기록 파일에 이미 오늘 기록이 있다면
        history = history.iloc[:-1, :]

    df = pd.DataFrame(data={'date': int_date, 'total concentration time': sum}, index=[0])
    pd.concat([history, df], axis=0, ignore_index=True)

else:
    history = pd.DataFrame(data={'date': int_date, 'total concentration time': sum}, index=[0])

history.plot(x='date', y='total concentration time', kind = 'line')
history.to_csv('기록.csv', mode='w', index=False, encoding='utf8')

#파일로 저장
timelog.to_csv(filedir, mode='w', index=False, encoding='utf8')

input() #화면 꺼짐 방지용


