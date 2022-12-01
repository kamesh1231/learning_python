# Step 1 - initialize the dictionary
profile_dict = {}

# Step 2 - Ask for Students name and marks
int_studentname = input("Enter student name:")
int_studentmark = int(input(f'How much did {int_studentname} score in maths:'))


# Step 3 - print name and marks
print(f'{int_studentname} scored  {int_studentmark} in maths')

# Step 4 - add student name & mark to Dictionary

profile_dict[int_studentname] = int_studentmark

# Step 5 - Run While loop for adding student names & scores until asked to stop
inpt = True

while inpt:
    c = input(f'do you want to add another students score ? (Yes/No):')
    if c == 'Yes':
        nxt_studentname = input("Enter student name:")
        nxt_studentmark = int(input(f'How much did {nxt_studentname} score in maths:'))
        print(f'{nxt_studentname} scored  {nxt_studentmark} in maths')
        profile_dict[nxt_studentname] = nxt_studentmark

        print(profile_dict)


    elif c == 'No':
        inpt = False

# Step 6 - Find out average by dividing sum/length

dict_sum = (sum(profile_dict.values()))
dict_avg = dict_sum/len(profile_dict)
print(f'Average marks in maths is for this class is {dict_avg}')