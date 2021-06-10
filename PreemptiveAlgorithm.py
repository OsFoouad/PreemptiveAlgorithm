"""
Andvanced  Operating System 
Dr.Salah Eldin Shaban
lab examination 
-- Q.2 -- preemptive scheduling
Osama Fouad Mohamed Nada
Sec : 1  , ID : 1500441  
Serial Number :  24
"""


import matplotlib.pyplot as plt

# intial the fig and gnt
fig, gnt = plt.subplots()
# y - limits
gnt.set_ylim(0, 50)
# x - limits
gnt.set_xlim(0, 70)
#axis titles
gnt.set_xlabel('Tasks')
gnt.set_ylabel('Priority')
# turn on gird
gnt.grid(True)


"""
The Example :-
T1 = (0 , 60, 25,50)
T2 = (15 , 60 ,10 ,40)
T3 = (20 , 60 , 15 , 60)
"""

# Release , period  , Execution and Deadline times lists
colorQ = ['tab:red' ,'tab:blue'  , 'tab:grey']
jobReleaseTimeQ = [0  , 15 , 20]
jobPeriodTimeQ =  [60 , 60 , 60]
jobExecuteTimeQ = [25 , 10 , 15]
jobDeadlineQ =    [50 , 40 , 60]
arrangedRT =      []
remainingET =     []
jobNum = 3
notFinished =     []

# communicate with user to get the tasks to be scheduling information
def getTasksInfo():
    global jobReleaseTimeQ ; global jobPeriodTimeQ ; global jobExecuteTimeQ ; global jobDeadlineQ
    global jobNum 
    jobNum= int(input("Enter the Number of Jobs : \n"))
    print(" Must enter tasks arranged according to Release Time from low to high ")
    for i in range(jobNum):
        print("Enter task " , i+1 , " Release time  , period  , execute time and deadline time")
        rt  = int(input())
        jobReleaseTimeQ.append(rt)
        pt = int(input())
        jobPeriodTimeQ.append(pt)
        et = int(input())
        jobExecuteTimeQ.append(et)
        dt = int(input())
        jobDeadlineQ.append(dt)

# additional function to show the data enterd for the tasks
def showTasksInfo():
    print("Release Times   : " ,jobReleaseTimeQ)
    print("Period Times    : " ,jobPeriodTimeQ)
    print("Execution Times : " ,jobExecuteTimeQ)
    print("Deadline Times  : " ,jobDeadlineQ)

# preprocessing for the algorithm
def preprocessingSetup():
    global remainingET
    global notFinished
    remainingET = list(jobExecuteTimeQ)
    for i in range(jobNum):
        notFinished.append(i+1)
    
# the algorithm implementation
def firstRound():
    
    print("=======================================")
    #make a copy of Release time Queue and arrange it from low to high
    global arrangedRT
    arrangedRT = list(jobReleaseTimeQ)
    arrangedRT.sort()
    preprocessingSetup()
    global notFinished
    print("The first round :-->")
    # scheduling the tasks
    for i in range (jobNum):       
        taskN = arrangedRT[i]
        taskN = jobReleaseTimeQ.index(taskN)
    
        print("Task" , taskN+1  , "is processing now" )
        if i != jobNum-1:
            remainingET[taskN] = remainingET[taskN] - (jobReleaseTimeQ[taskN+1] - jobReleaseTimeQ[taskN] )
            print(f"Task {taskN+1} interrupted by task {taskN+2} , with remain Execution time : {remainingET[taskN]} ")
            
            gnt.broken_barh( [(jobReleaseTimeQ[i] , jobExecuteTimeQ[i] - remainingET[i])] ,
            (i*10 , 6),
				 facecolors =colorQ[i%3])
        else:
            print(f"Task {taskN+1} has been finished")
            notFinished.pop()
            remainingET[i] = 0
            print("----------------------------------------")
            print("* * * * * Scheduling details * * * * *")
            print(f"The remaining execution time is :{remainingET}")
            print("Unfinished Tasks                :" ,notFinished)
            gnt.broken_barh([(jobReleaseTimeQ[i] , jobExecuteTimeQ[i])] ,
				 (i*10 , 6),
				 facecolors =colorQ[i%3])
    print("=======================================")
    # end of first round.

# preemptive algorithm - with a recursion till all tasks finished
def preemptiveAlgorithm(notFinished):
    starter  = 0
    theRange = len(notFinished)
    print("New Round :-->")
    for i in range(theRange):
        if i != theRange -1 :
            print(f"Task {i+1} paused with remain Execution time {remainingET[i]}")
        else:
            print(f"Task {i+1} is processing now")
            print(f"Task {i+1} has been finished")
            for j in range(jobNum):
                if j > i :
                    starter = starter + jobExecuteTimeQ[j]
                else:
                    starter = starter + (jobExecuteTimeQ[j] - remainingET[j])
            gnt.broken_barh([( starter , remainingET[i])] ,
				 (i*10  , 6),
				 facecolors =colorQ[i%3])
            remainingET[i] = 0
            notFinished.pop()
            print("----------------------------------------")
            print("* * * * * Scheduling details * * * * *")
            print(f"The remaining execution time is :{remainingET}")
            print(f"Unfinished Tasks                :{notFinished}")
            print("=======================================")
    if notFinished:
        preemptiveAlgorithm(notFinished)
    
    #end of preemptive Algo function


### Main Driver ###
print("Welcome to Preemptive Scheduling Algorithm")
print("1 - Run with the Example \n2 - Run with Differnt problem")
choice = int(input("Enter your choice number : "))
if choice == 1:
    #show the Example data
    showTasksInfo()
    #start the algorithm
    firstRound()
    preemptiveAlgorithm(notFinished)
    print("All Tasks has been Preemptively schedualed")
    plt.show()

elif choice ==2:
    #Clear the initial Queues -lists- for new data 
    jobReleaseTimeQ = []
    jobPeriodTimeQ = []
    jobExecuteTimeQ = []
    jobDeadlineQ = []
    #get data from user
    getTasksInfo()
    #show user entries
    showTasksInfo()
    #start the algorithm
    firstRound()
    preemptiveAlgorithm(notFinished)
    print("All Tasks has been Preemptively schedualed")
    plt.show()
    
else:
	print("Wrong Entry , Run and Try again .")
    
    