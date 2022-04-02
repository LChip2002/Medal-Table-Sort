# Feel free to create other helper functions
# def helper_function_name(arguments):
#      pass

import csv #Allows for csv files to be read from and written to

#Function that gets the values from the csv file
def rank_team(file_name):
    # your code starts from here.
    
    #Global variables that will be needed in the sorting function
    global a, b, c, d, e, f, g, h, i, j, row_T1_int, row_T2_int, row_T3_int, row_T4_int, row_T5_int\
        , row_T6_int, row_T7_int, row_T8_int, row_T9_int, row_T10_int, row_int_list, new_list, file_text 
    
    with open(file_name, 'r') as file: #Opens and reads the original medal table in medal.csv

        #Allows for the CSV file to be read
        file_text = csv.reader(file) 
        new_list = [] 

        for row in file_text:            
            new_list.append(row[1:4]) #Adds the contents of the initial spreadsheet to the list
        
        #Sets each row of the table with numbers to variables (a being the top set of numbers of the table)
        a = (new_list[1])
        b = (new_list[2])
        c = (new_list[3])
        d = (new_list[4])
        e = (new_list[5])
        f = (new_list[6])
        g = (new_list[7])
        h = (new_list[8])
        i = (new_list[9])
        j = (new_list[10])

        #Combines the contents of each row and turns them into numbers that can be used in the sort
        row_T1_int = int(a[0]+ a[1]+ a[2]) 
        row_T2_int = int(b[0]+ b[1]+ b[2])
        row_T3_int = int(c[0]+ c[1]+ c[2])
        row_T4_int = int(d[0]+ d[1]+ d[2])
        row_T5_int = int(e[0]+ e[1]+ e[2])
        row_T6_int = int(f[0]+ f[1]+ f[2])
        row_T7_int = int(g[0]+ g[1]+ g[2])
        row_T8_int = int(h[0]+ h[1]+ h[2])
        row_T9_int = int(i[0]+ i[1]+ i[2])
        row_T10_int = int(j[0]+ j[1]+ j[2])

        #The new combined values of the variables above is now put into a list so it can be sorted
        row_int_list = [row_T1_int,row_T2_int,row_T3_int,row_T4_int,row_T5_int,row_T6_int,row_T7_int,row_T8_int,row_T9_int,row_T10_int]
        
#Sorting function using the merge sort algorithm
def merge_sort(row_int_list): 
    global new_row_list
    if len(row_int_list) == 1: #Verification to ensure that there isn't any errors with 1 element lists
        return row_int_list
    else:
        mid = (len(row_int_list))//2 #Performs integer division
        left_half = merge_sort(row_int_list[:mid]) #Left half of list is put in this variable
        right_half = merge_sort(row_int_list[mid:]) #Right half of list is put in this variable
    
    new_row_list = [] #Where the sorted list will go
    
    #Increments for the while loops
    i = 0
    j = 0
    
    #While loop to sort the seperated parts and merge them 
    while(i<len(left_half) and j < len(right_half)):
        if (left_half[i] < right_half[j]):
            new_row_list.append(left_half[i])
            i += 1
        else:
            new_row_list.append(right_half[j])
            j += 1

    #Checks if lefthalf still has elements that haven't merged and adds them
    while (i<len(left_half)):
        new_row_list.append(left_half[i])
        i += 1
    
    #Checks if righthalf still has elements that haven't merged and adds them
    while (j<len(right_half)):
        new_row_list.append(right_half[j])
        j += 1
    return new_row_list #Returns the new sorted list to the main program
    
#Function makes the sorted list into same format as original & makes fields and rows with them
def new_table_maker(new_row_list,row_int_list): 
    global table_row_list, fields, rows
    
    with open('medal.csv', 'r') as file: #Opens and reads the original medal table in medal.csv        
        
        y = 0
        new_row_list_split = [] #Empty list that will add the values of the sorted list once they have been split into individual numbers

        #For loop goes through each line of newrowlist and split them up to convert them to be able to compare to the original table
        for y in range(0,len(new_row_list)):  
            splitter = list(map(int, str(new_row_list[y]))) 
            splitter = list(map(str, splitter)) #Converts the split value back into a string, same format as the original table
            new_row_list_split.append(splitter) #Adds the split value to the newrowlistsplit list

        #Allows for the CSV file to be read
        file_text = csv.reader(file) 
        old_medal_table = []
        old_medal_table_row_strip = []

        #Gets the values from the original medal table to be compared to the new sorted numbers 
        for row in file_text:
            old_medal_table.append(row)
            old_medal_table_row_strip.append(row[1:4]) 
        
        #Increments for while loop
        i = 0

        table_row_list = []

        #Nested while loops to be able to compare 1 element from newrowlist to multiple from oldmedaltable until correct match is found
        while (i <len(new_row_list_split)):
            j = 1 #Increment for 2nd while loop in nested loop
            while(j<len(old_medal_table_row_strip)):
                if new_row_list_split[i] == old_medal_table_row_strip[j]:
                    table_row_list.append(old_medal_table[j])          
                    j += 1
                else:
                    j += 1
            i += 1

        print(table_row_list) #Prints the new sorted list now with the original format after being through the while loops
        table_row_list = table_row_list[::-1] #Reverses the order of the list to match the order of an actual medal table, highest to lowest
        print(table_row_list) #Prints the new reversed list matching the order of an actual medal table     
    
    #Field Names/Table headings
    fields = "Team","Gold","Silver","Bronze" 
    
    #Data rows of CSV File
    rows = table_row_list    
    
    return table_row_list,rows,fields

#Function creates the csv file itself with the sorted medal table
def csv_file_maker(fields, rows): 
    # name of csv file 
    new_file = "medal_table.csv"
    
    # writing to csv file 
    with open(new_file, 'w') as csvfile: 
        # creating a csv writer object 
        write_csv = csv.writer(csvfile) 
        
        # writing the fields 
        write_csv.writerow(fields) 
        
        # writing the data rows 
        write_csv.writerows(rows)

# Program main --- Do not change the code below but feel free to comment out 
print("This is the medal table sorting application")

# Calling Task 1 functions
rank_team('medal.csv') #Calls the function that collects the values of the old medal table
merge_sort(row_int_list) #Calls the merge sort function
print(new_row_list) #Prints the sorted list to terminal
new_table_maker(new_row_list,row_int_list) #Creates the new table to be used in the csv file
csv_file_maker(fields,rows) #Create the new csv file with the new sorted table


