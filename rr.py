process_queue = []
time_queue=[]
remaining_time_queue=[]
turn_time=[]
waiting_time=[]
stat_time=[]
burst_time_queue=[]

total_wtime = 0
count=0
total_burst_time=0
time_count=0
source_count=0
check1=0



quantum_time = int(raw_input('Enter Quantum Time: '))

total_number_of_process = int(raw_input('Enter the total no of processes: '))


for index in xrange(total_number_of_process):

    process_queue.append([])#append a list object to the list

    process_queue[index].append(raw_input('Enter p_name: '))

    process_queue[index].append(int(raw_input('Enter p_arrival Time: ')))

    total_wtime += process_queue[index][1]

    process_queue[index].append(int(raw_input('Enter p_bust Time: ')))
    total_burst_time=total_burst_time+process_queue[index][2]
    burst_time_queue.append(process_queue[index][2])
    waiting_time.append(-1)
    turn_time.append(-1)
    print ''



process_queue.sort(key = lambda process_queue:process_queue[1])

print 'ProcessName\tArrivalTime\tBurstTime'
for index in xrange(total_number_of_process):

    print process_queue[index][0],'\t\t',process_queue[index][1],'\t\t',process_queue[index][2]


for count in xrange(total_burst_time):
   for index in xrange(total_number_of_process):
      if process_queue[index][2] is 0:
         check1=check1+1
      if process_queue[index][2]>0 and  process_queue[index][2] <=quantum_time:
         if source_count is 0:
            remaining_time_queue.append(process_queue[index][1])
            time_count=time_count+process_queue[index][1]
            source_count=source_count+1
         if source_count>0:
            if waiting_time[index] is -1:
               waiting_time[index]=time_count

            remaining_time_queue.append(process_queue[index][0])
            time_count=time_count+process_queue[index][2]
            remaining_time_queue.append(time_count)
            remaining_time_queue.append('f')
            total_burst_time=total_burst_time-time_count
            process_queue[index][2]=0
            turn_time[index]=time_count

      if process_queue[index][2]>0 and  process_queue[index][2] >quantum_time:
         if source_count is 0:
            remaining_time_queue.append(process_queue[index][1])
            time_count=time_count+process_queue[index][1]
            source_count=source_count+1
         if source_count>0:
            if waiting_time[index] is -1:
               waiting_time[index]=time_count

            remaining_time_queue.append(process_queue[index][0])
            time_count=time_count+quantum_time
            remaining_time_queue.append(time_count)
            remaining_time_queue.append('nf')
            total_burst_time=total_burst_time-time_count
            process_queue[index][2]=process_queue[index][2]-quantum_time




check=0
for x in xrange(total_number_of_process):
   for index in range(len(remaining_time_queue)):
      if remaining_time_queue[index] is process_queue[x][0] and check is 0:
          stat_time.append(remaining_time_queue[index-1])
          check=check+1
      if remaining_time_queue[index] is process_queue[x][0] and check >0:
          stat_time.append(remaining_time_queue[index-2])
          check=check+1



print 'Gant chart---------------------------------------> '
for index in range(len(remaining_time_queue)):
    print remaining_time_queue[index],'-->'

print '-------------------------------------------------> '

print '---------------Start Time--------------------> '
for index in range(len(waiting_time)):
   print 'Start time of->',process_queue[index][0],':',waiting_time[index]


print '------------Finish  Time----------------------> '
for index in range(len(turn_time)):
   print 'Finish time of->',process_queue[index][0],':',turn_time[index]

print '------------Turn Around Time-------------------> '
for index in range(len(waiting_time)):
   print 'Turn Around Time for->',process_queue[index][0],':',turn_time[index]-waiting_time[index]


print '-------------------------------------------------> '
print '------------Waititng  Time-------------------> '
for index in range(len(waiting_time)):
   result=turn_time[index]-waiting_time[index]
   print  'waiting time of process',process_queue[index][0],':',result-burst_time_queue[index]


print '-------------------------------------------------> '
