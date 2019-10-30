import datetime
import fileinput


time = datetime.datetime.strptime('2019-10-27T17:32:16.00', '%Y-%m-%dT%H:%M:%S.%f')
time_step = 17.56 #[sec]

editing_time = False
for line in fileinput.input('Desktop\gpx_data.txt', inplace=1):
    if '<time>' in line:
        editing_time = True
        time += datetime.timedelta(seconds=17.56)
        continue #want to replace the line in this case
    else:
        if editing_time:
            print('<time>' + datetime.datetime.strftime(time, '%Y-%m-%dT%H:%M:%S.%f') + 'Z</time>')
        editing_time = False
    print(line)
