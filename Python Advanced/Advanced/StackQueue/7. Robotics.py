from collections import deque

def SecsToHrsMnsSec(seconds):
    seconds%=24*60*60
    hrs=seconds//3600
    mns=(seconds%3600)//60
    secs=(seconds%3600)%60
    return f"[{hrs:02d}:{mns:02d}:{secs:02d}]"
    #return "%02i:%02i:02i" % (hrs,mns,seconds)
    # #todo ATANAS variant

def convert_str_to_seconds(time):
    hrs,mns,secs=[int(x) for x in time.split(":")]
    return hrs*60*60+mns*60+secs

robots_data=input().split(";")
process_time_by_robot={}
busy_time_by_robot={}

for robot_data in robots_data:
    name,process_time=robot_data.split('-')
    process_time_by_robot[name]=int(process_time)
    busy_time_by_robot[name]=-1

time=convert_str_to_seconds(input())
items=deque()

item=input()
while item!= "End":
    items.append(item)
    item= input()

while items:
    time+=1
    item=items.popleft()

    for name,busy_until in busy_time_by_robot.items():
        if time >= busy_until:
            busy_time_by_robot[name]=time+process_time_by_robot[name]
            print(f"{name} - {item} {SecsToHrsMnsSec(time)}")
            break
    else:
        items.append(item)