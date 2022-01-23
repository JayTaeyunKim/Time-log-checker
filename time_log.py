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

#파일로 저장
timelog.to_csv(filedir, mode='w', index=False, encoding='utf8')

input() #화면 꺼짐 방지용


