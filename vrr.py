process_queue = []
time_queue=[]
remaining_time_queue=[]
auxiliary_queue=[]
turn_time=[]
waiting_time=[]
stat_time=[]
waiting_queue=[]
wake_up=[]

check_interrupt=0
total_wtime = 0
count=0
total_burst_time=0
time_count=0
source_check=0
do_nothing=0
running_time=[]
interrupt=1000
quantum_time=0

quantum_time = int(raw_input('Enter Quantum Time: '))

while interrupt>quantum_time:

   interrupt=int(raw_input('Enter Interrupt time Time slice: '))

wait=int(raw_input('Enter the index/o wait Time: '))



no_of_process = int(raw_input('Enter the total no of processes: '))


for index in xrange(no_of_process):
    waiting_queue.append([])
    process_queue.append([])#append a list object to the list

    process_queue[index].append(raw_input('Enter p_name: '))

    process_queue[index].append(int(raw_input('Enter p_arrival Time: ')))

    total_wtime += process_queue[index][1]

    process_queue[index].append(int(raw_input('Enter p_bust Time: ')))
    total_burst_time=total_burst_time+process_queue[index][2]
    waiting_queue[index].append(0)
    waiting_queue[index].append(0)

    waiting_time.append(-1)
    turn_time.append(-1)
    wake_up.append(1)
    running_time.append(0)
    auxiliary_queue.append(0)
    print ''



process_queue.sort(key = lambda process_queue:process_queue[1])

print 'ProcessName\tArrivalTime\tBurstTime'
for index in xrange(no_of_process):

    print process_queue[index][0],'\t\t',process_queue[index][1],'\t\t',process_queue[index][2]


for count in xrange(total_burst_time+1):
   for index in xrange(no_of_process):
      if process_queue[index][2] is 0:
         do_nothing=do_nothing+1
      elif process_queue[index][2]>0 and  process_queue[index][2] <=interrupt  and wake_up[index] is 1 : 
         if source_check is 0:
            remaining_time_queue.append(process_queue[index][1])
            time_count=time_count+process_queue[index][1]
            source_check=source_check+1
         if source_check>0:
            if waiting_time[index] is -1:
               waiting_time[index]=time_count
            remaining_time_queue.append(process_queue[index][0])
            time_count=time_count+process_queue[index][2]
            remaining_time_queue.append(time_count)
            check_interrupt=time_count
            remaining_time_queue.append('f')
            total_burst_time=total_burst_time-time_count
            process_queue[index][2]=0
            turn_time[index]=time_count
            print 'in else 1'



      elif process_queue[index][2]>0 and  process_queue[index][2]>interrupt and wake_up[index] is 1  :
 

         if source_check is 0:
            remaining_time_queue.append(process_queue[index][1])
            time_count=time_count+process_queue[index][1]
            source_check=source_check+1
         if source_check>0:
            if waiting_time[index] is -1:
               waiting_time[index]=time_count
               
               remaining_time_queue.append(process_queue[index][0])
               time_count=time_count+interrupt
               remaining_time_queue.append(time_count)
               check_interrupt=time_count
               waiting_queue[index][0]=quantum_time - interrupt
               waiting_queue[index][1]=time_count+wait
               print waiting_queue[index][1],'wake up process-->',
               wake_up[index]=0
               remaining_time_queue.append('nf')
               total_burst_time=total_burst_time+wait
               running_time[index]=0
               total_burst_time=total_burst_time-time_count
               process_queue[index][2]=process_queue[index][2]-interrupt
               print 'in else 2'



      elif process_queue[index][2]>0 and  waiting_queue[index][0]> 0 and time_count is waiting_queue[index][1]:
         process_queue[index][2]=process_queue[index][2]-waiting_queue[index][0]
         if process_queue[index][2] is 0:
            print process_queue[index][0],'finish-->',time_count
            turn_time[index]=time_count

         waiting_queue[index][1]=waiting_queue[index][1]-1
         remaining_time_queue.append(process_queue[index][0])
         print 'in else if 3'
         time_count=time_count+waiting_queue[index][0]
         remaining_time_queue.append(time_count)
         waiting_queue[index][0]=0
         check_interrupt=time_count
      else:
         
         time_count=time_count+1
         for ll in xrange(no_of_process):
            if time_count is waiting_queue[ll][1]:
               wake_up[ll]=1
         remaining_time_queue.append(time_count)
         remaining_time_queue.append('-->')
         






check=0
for x in xrange(no_of_process):
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
print 'ProcessName\tArrivalTime\tBurstTime'
for index in xrange(no_of_process):

    print process_queue[index][0],'\t\t',process_queue[index][1],'\t\t',process_queue[index][2]
