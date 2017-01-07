process_queue = []
waiting_time_queue=[]

total_wtime = 0
count=0
total_burst_time=0
start=1
burst_time=0
temp=[]
no_of_process = int(raw_input('Enter the total no of processes: '))

for counter in xrange(no_of_process):

    process_queue.append([])#append a list object to the list

    process_queue[counter].append(raw_input('Enter p_name: '))

    process_queue[counter].append(int(raw_input('Enter p_arrival Time: ')))

    total_wtime += process_queue[counter][1]

    process_queue[counter].append(int(raw_input('Enter p_bust Time: ')))
   
    process_queue[counter].append(int(raw_input('Enter Priority of Process: ')))

    print ''



process_queue.sort(key = lambda process_queue:process_queue[1])


value=process_queue[0][1]
check2=1
check1=0
count1=0
for counter in xrange(no_of_process):
   if process_queue[counter][1] is value:
      check1=1
   else:
      check2=0

if check1 is 1 and check2 is 1:
   process_queue.sort(key = lambda process_queue:process_queue[3])
else:
   for j in range(0,no_of_process-1):
      burst_time=burst_time+process_queue[j][2]
      min=process_queue[start][3]
      index=start
      for l in range(index,no_of_process):
        if process_queue[l][3]<min:
           
           temp.append(process_queue[start])
           process_queue[start]=process_queue[l]
           process_queue[l]=temp[count1]
           count1=count1+1
      start=start+1

total_burst_time=total_burst_time+process_queue[0][1]
for counter in xrange(no_of_process):
    for a in xrange(counter):
        total_burst_time=total_burst_time+process_queue[a][2] 
    if count is 0: 

        process_queue[counter].append(0)
        count=count+1
        total_burst_time=process_queue[0][1]
    else:
        process_queue[counter].append(total_burst_time-process_queue[counter][1])
        count=count+1
        total_burst_time=process_queue[0][1]

count=0
total_burst_time=0
total_burst_time=total_burst_time+process_queue[0][1]
for counter in xrange(no_of_process):
    total_burst_time=total_burst_time+process_queue[counter][2] 
    if count is 0: 
        process_queue[counter].append(process_queue[0][2]) 
        count=count+1
    else:
        process_queue[counter].append(total_burst_time-process_queue[counter][1])
        count=count+1

print 'ProcessName\tArrivalTime\tBurstTime\tPriority \tWaitingTime\tTurnaroundTime'

for counter in xrange(no_of_process):

    print process_queue[counter][0],'\t\t',process_queue[counter][1],'\t\t',process_queue[counter][2],'\t\t',process_queue[counter][3],'\t\t',process_queue[counter][4],'\t\t',process_queue[counter][5]

    

