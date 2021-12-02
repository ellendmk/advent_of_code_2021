# Part 1
# f = open('test.txt')
f = open('in.txt')
sonar_report = [int(k) for k in f.read().split('\n')]
f.close()

print(sonar_report[0:10])

inc_count = 0
for k in range(1,len(sonar_report)):
    if sonar_report[k-1]<sonar_report[k]:
        inc_count+=1

print('Answer part 1: ', inc_count)

# Part 2
# f = open('test.txt')
f = open('in.txt')
sonar_report = [int(k) for k in f.read().split('\n')]
f.close()

inc_count = 0
for k in range(3,len(sonar_report)):
    if (sonar_report[k-3]+sonar_report[k-2]+sonar_report[k-1])<(sonar_report[k-2]+sonar_report[k-1]+sonar_report[k]):
        inc_count+=1

print('Answer part 2: ', inc_count)