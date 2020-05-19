
# a calculator to conduct basic stat analysis because i got bored while doing my stats homework

# enter your desired numbers here, separated by commas, in no particular order

data = [20, 40, 13, 19, 3, 3, 9]

# this is where the mean calculation is coming from

total_sum = sum(data)
mean = total_sum / len(data)
print(data)
print("The mean is: " +str(round(mean,2)))

# here is where the median calculation is coming from

data.sort()
if len(data) % 2 == 0:
    first_median = data[len(data) // 2]
    second_median = data[len(data) // 2 - 1]
    median = (first_median + second_median) / 2
else:
    median = data[len(data) // 2]
print("The median is: " +str(median))

# and the mode comes from here:

data.sort()
L1=[]
i = 0
while i < len(data):
    L1.append(data.count(data[i]))
    i += 1
d1 = dict(zip(data, L1))
mode={k for (k,v) in d1.items() if v == max(L1)}
print("The mode is: " +str(mode))