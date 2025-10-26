num_list = []

for i in range (1,11):
    num_list.append(i)

first_five = num_list[:5]
reverse_first_five = first_five[::-1]

print (f"Original list: {num_list}")
print (f"Extracted first five elements: {first_five}")
print (f"Reversed extracted elements: {reverse_first_five}")