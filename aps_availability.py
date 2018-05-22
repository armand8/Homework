import datetime

# definition of AP list
foo_airport = []
for i in range(0, 100):
    foo_airport.append("AP" + str(i+1))

# dict of days present in log file
days = {}

# new text file for output results
output_file = open("ap_avaibility.txt", "w")

# parsing of log file, a dict of dict of set contains the number of sec. where each ap is seen per day
with open("system_logs.txt") as f:
    for line in f:
        log = line.rstrip().replace(" ","").split(',')
        if not log[0] in days:
            days[log[0]] = dict.fromkeys(foo_airport, "")
            for key in days[log[0]]:
                 days[log[0]][key] = set()
        t = datetime.datetime.strptime(log[1], '%H:%M:%S')
        time_in_seconds = int(datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second).total_seconds())
        days[log[0]][log[2]].add(time_in_seconds)

# here begins output in text file, sorry for the file layout :/
output_file.write("               ")
for ap in foo_airport:
    output_file.write(ap + "   ")


output_file.write("\n")
for key in days:
    output_file.write(key + "   ")
    for ap in days[key]:
        # seconds of the day where ap was seen divided by number of seconds per day times 100 (percentage)
        output_file.write(str(int(len(days[key][ap])/864)) + "%      ")
    output_file.write("\n")


output_file.close()


