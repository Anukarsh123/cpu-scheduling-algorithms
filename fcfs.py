# FCFS CPU Scheduling Algorithm
# Operating Systems

def fcfs(processes, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Waiting time for first process is 0
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

    # Turnaround time = waiting time + burst time
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print("\nAverage Waiting Time:", round(avg_wt, 2))
    print("Average Turnaround Time:", round(avg_tat, 2))


# -------- MAIN PROGRAM --------
processes = ["P1", "P2", "P3"]
burst_time = [10, 5, 8]

fcfs(processes, burst_time)

📤 Sample Output

Process  Burst Time  Waiting Time  Turnaround Time
P1       10          0             10
P2       5           10            15
P3       8           15            23

Average Waiting Time: 8.33
Average Turnaround Time: 16.0