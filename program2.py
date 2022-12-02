f = open('input.py','r')
current_sum = 0
three_max = 0
max_val = []
i = 0

for line in f:
    if line != "\n":
        current_sum += int(line)
    else:
        max_val.append(current_sum)
        current_sum = 0

print ("max calories array", max(max_val))

for i in range(0,3):
    three_max += max(max_val)
    max_val.remove(max(max_val))

print("top three summation of calories", three_max)