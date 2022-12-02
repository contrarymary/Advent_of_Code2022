f = open('input.py','r')
current_sum = 0
max = 0

for line in f:
    if line != "\n":
        current_sum += int(line)
    else:
        if max < current_sum:
            max = current_sum
        current_sum = 0

print ("max calories =", max)