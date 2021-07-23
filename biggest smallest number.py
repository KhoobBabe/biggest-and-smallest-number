num = int(input("Enter the number: "))

#we convert the number in a string
y = [int(n) for n in str(num)]

#this finds the biggest bumber that can be made with the digits
#len(y) finds the length of string
for num_1 in range(len(y)):
    for num_2 in range(num_1 + 1, len(y)):
#we place the numbers in ascending order by using the Bubble sort algorithm
        if y[num_1] > y[num_2]:
            y[num_1], y[num_2] = y[num_2], y[num_1]
str_num = ''.join(str(i) for i in y)

print("smallest number: ", int(str_num))



      


#this finds the smallest number that can be made with the digits
for num_1 in range(len(y)):
    for num_2 in range(num_1 + 1, len(y)):
#again Bubble sort algorithm is used 
        if y[num_1] < y[num_2]:
            y[num_1], y[num_2] = y[num_2], y[num_1]
#we join the numbers back with no commas or space between them 
str_num = ''.join(str(i) for i in y)
#the joined number is converted into an integer
print("biggest number: ", int(str_num))



      




