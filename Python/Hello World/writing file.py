
employee_file = open("employees1.txt", "w")

'''
a = append - can add at the end
w = overwrites the file
r = read only
r+ = read and write
if using "w" and file not found...it creates a new file(txt\html etc.)
'''

employee_file.write("\nKelly - Costumer service")

employee_file.close()
