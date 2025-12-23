def childernNum(num_children):
    final_families = []  #list of the final familiy options
    total_options = 2 ** num_children #calc all the options of combination

    for i in range(total_options): #loop from 0 to the num not included
        current_family = [] #temporary familly count
        temp_num = i #temporary index
        while temp_num > 0:
            if temp_num % 2 == 0:
                current_family.append('Boy')
            else:
                current_family.append('Girl')
            temp_num = temp_num // 2
        while len(current_family) < num_children: #Padding to get the lengh we want if too short
            current_family.append('Boy')
        final_tuple = tuple(current_family[::-1]) #only after we have the list completed and full move to tuple
        final_families.append(final_tuple) #add it to the final_families to print
    printl(final_families)
    #calc the space sample
    count_two_girls = 0 #define the beggeing of the count
    for family in final_families: #naive Definition of Probability calc:
        girls = 0
        for child in family:
            if child == 'Girl': #count how many girls there are
                girls += 1
        if girls == 2: #check if we reached 2 girls
            count_two_girls += 1
    if total_options > 0:
        print(count_two_girls / total_options) # print the probility of 2 girls in familly
    else:
        print(0)

try:
    print("enter the number of children: ")
    num_input = int(input())
    if num_input < 0:
        print("please enter a positive number of children")
    else:
        childernNum(num_input)
except ValueError:
    print("invalid input, please enter an integer")
except Exception as er: #check for other errors and tell the user which it is
    print(f'an error occurred: {er}')