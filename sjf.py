# Shortest Job First (Non-Preemptive) CPU Scheduling
# Operating Systems

def sjf(processes, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Sort processes based on burst time
    sorted_data = sorted(zip(burst_time, processes))
    burst_time_sorted, processes_sorted = zip(*sorted_data)

    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time_sorted[i - 1]

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time_sorted[i]

    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes_sorted[i]}\t{burst_time_sorted[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print("\nAverage Waiting Time:", round(avg_wt, 2))
    print("Average Turnaround Time:", round(avg_tat, 2))


# -------- MAIN PROGRAM --------
processes = ["P1", "P2", "P3"]
burst_time = [10, 5, 8]

sjf(processes, burst_time)

📤 Sample Output

Process  Burst Time  Waiting Time  Turnaround Time
P2       5           0             5
P3       8           5             13
P1       10          13            23

Average Waiting Time: 6.0
Average Turnaround Time: 13.67