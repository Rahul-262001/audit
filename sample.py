
# num = 0
i = '1'
for j in range(0,1000):
    i+='0'
low = -1*int(i)
up = int(i)
num = r.randint(low,up)
count = 0
print("The number to guess is ",num)
while True:
    count+=1
    val = r.randint(low,up)
    if val == num:
        print("Program guessed right",val)
        break;
    elif val < num and val > low:
        low = val
        print("low changed, the random number was ",val)
    elif val > num and val < up:
        up = val
        print("high changed the random number was ",val)


print(f"the total number of step {count}")
