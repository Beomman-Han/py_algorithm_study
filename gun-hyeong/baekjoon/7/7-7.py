split_number = input().split(" ")

for i in range(len(split_number)):
    
    split_number[i] = split_number[i][::-1]

print (max(split_number))