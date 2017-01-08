process_queue = []
waiting_time_queue=[]
Queue1=[]
Queue2=[]
total_wtime = 0
count=0
total_burst_time=0
cpu_time_queue1=-1

print 'index am using only 2 queues in it'
print 'u will Enter Cpu Time For Queue1'
print 'the cpu time for Queue1 will be grearer the Queue1'

total_number_of_process = int(raw_input('Enter the total no of processes: '))
cpu_time_queue1 = int(raw_input('Enter the Cpu Time For Queue1: '))

for index in xrange(total_number_of_process):

    process_queue.append([])#append a list object to the list

    process_queue[index].append(raw_input('Enter p_name: '))

    process_queue[index].append(int(raw_input('Enter p_arrival Time: ')))

    total_wtime += process_queue[index][1]

    process_queue[index].append(int(raw_input('Enter p_bust Time: ')))

    print ''



process_queue.sort(key = lambda process_queue:process_queue[1])
total_burst_time=total_burst_time+process_queue[0][1]

for index in xrange(total_number_of_process):
   if process_queue[index][2]>=3:
      Queue2.append(process_queue[index])
   else :
      Queue1.append(process_queue[index])

for index in xrange(total_number_of_process):
    for a in xrange(index):
        total_burst_time=total_burst_time+process_queue[a][2] 
    if count is 0: 

        process_queue[index].append(0)
        count=count+1
        total_burst_time=process_queue[0][1]
    else:
        process_queue[index].append(total_burst_time-process_queue[index][1])
        count=count+1
        total_burst_time=process_queue[0][1]

count=0
total_burst_time=0
total_burst_time=total_burst_time+process_queue[0][1]
for index in xrange(total_number_of_process):
    total_burst_time=total_burst_time+process_queue[index][2] 
    if count is 0: 
        process_queue[index].append(process_queue[0][2]) 
        count=count+1
    else:
        process_queue[index].append(total_burst_time-process_queue[index][1])
        count=count+1

print 'Queue1 FcFs'

for index in xrange(len(Queue1)):
   print Queue1[index]

print 'Queue2 FCFS'

for index in xrange(len(Queue2)):
   print Queue2[index]




print 'ProcessName\tArrivalTime\tBurstTime\tWaitingTime\tTurnaroundTime'

for index in xrange(total_number_of_process):

    print process_queue[index][0],'\t\t',process_queue[index][1],'\t\t',process_queue[index][2],'\t\t',process_queue[index][3],'\t\t',process_queue[index][4]

