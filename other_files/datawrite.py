# Open function to open the file "MyFile1.txt"
# (same directory) in read mode and
file1 = open("MyFile.txt" , "w")

# store its refernce in the variable file1
# and "MyFile2.txt" in D:/Text in file2
file2 = open(r"C:/Users/19168/Documents/GitHub/BE2324/MyFile.txt", "w+")

# Opening and Closing a file "MyFile.txt"
# for object name file1.
file1 = open("MyFile.txt", "w")
file1.close()
    
# Python program to demonstrate
# writing to file

# Opening a file
file1 = open('myfile.txt' , 'w')
L = ["This is up /n" , "This is down /n"]
S = "Ok/n"

# Writing a string to file
file1.write(S)

# Writing multiple strings
# at a time
file1.close()

# Checking if the data is
# written to file or not
file1 = open('myfile.txt' , 'r')
print(file1.read())
file1.close()

# Open the file for writing
with open('file.txt' , 'w') as f:
    # Define the data to be written
    data = ['This is the first line', 'This is the second line', 'This is the third line']
    # Use a for loop to write each line of data to the file
    for line in data:
        f.write(line + '/n')
        # Optioanlly, print the data as it is written to the file
        print(line)
# The file is automatically closed when the 'with' block ends
# Python program to keep the old content of the file
# when using write

# Opening the file with append mode
file = open("gfg input file.txt", "a")   

# Content to be added
content = "/n/n# This Content is added through the program #"

# Writing the file
file.write(content)

# Closing the opened file
file.close()
