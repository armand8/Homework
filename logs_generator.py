import datetime
import random

# user inputs
logs_per_day = 8000000
# logs_per_day = 24000000
days_to_log = 2

# definition of AP list
foo_airport = []
for i in range(0, 100):
    foo_airport.append("AP" + str(i+1))

# creation of log file
f = open("system_logs.txt", "w")


# generation of logs starting of the date of today but for 24h from midnight
def logs_generator():
    date = datetime.date.today()
    for day in range(0, days_to_log):
        date = date + datetime.timedelta(days=day)
        # 86400 = seconds per day
        for second in range(1, 86400):
            time = datetime.timedelta(seconds=second)
            for logs_per_second in range(0, int(logs_per_day/86400)):
                ap = random.choice(foo_airport)
                mac = "Mac" + str(random.randint(0, 999))
                wifi_power = str(random.randint(-150, -1)) + "dB"
                log = str(date) + ", " + str(time) + ", " + str(ap) + ", " + str(mac) + ", " + str(wifi_power)
                f.write(log + '\n')


logs_generator()
f.close()




