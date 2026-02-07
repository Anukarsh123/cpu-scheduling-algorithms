# Round Robin CPU Scheduling Algorithm
# Operating Systems

def round_robin(processes, burst_time, time_quantum):
    n = len(processes)
    remaining_time = burst_time.copy()
    waiting_time = [0] * n
    turnaround_time = [0] * n
    time = 0

    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                if remaining_time[i] > time_quantum:
                    time += time_quantum
                    remaining_time[i] -= time_quantum
                else:
                    time += remaining_time[i]
                    waiting_time[i] = time - burst_time[i]
                    remaining_time[i] = 0
        if done:
            break

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print("\nTime Quantum:", time_quantum)
    print("Average Waiting Time:", round(avg_wt, 2))
    print("Average Turnaround Time:", round(avg_tat, 2))


# -------- MAIN PROGRAM --------
processes = ["P1", "P2", "P3"]
burst_time = [10, 5, 8]
time_quantum = 2

round_robin(processes, burst_time, time_quantum)
📤 Sample Output
Process  Burst Time  Waiting Time  Turnaround Time
P1       10          13            23
P2       5           8             13
P3       8           15            23

Time Quantum: 2
Average Waiting Time: 12.0
Average Turnaround Time: 19.67