"Kenneth Horsman (UCID: 30260797)"

file_name = input("Enter the name of a file: ")

file_contents = open(file_name).readlines()

num_commas = 0
num_lines = 0

for line in file_contents:
    for char in line:
        if char == ",":
            num_commas += 1
            
    num_lines += 1

print(f"That file contains {num_commas + num_lines} values.") # On each line, there's 1 more value than there is commas, so I'm adding a 1 per line