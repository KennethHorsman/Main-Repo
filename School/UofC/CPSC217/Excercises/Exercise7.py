"Kenneth Horsman (UCID: 30260797)"

file_name = input("Enter the name of a file: ")

file_contents = open(file_name)

num_commas = 0

for char in file_contents:
    if char == ",":
        num_commas += 1

print(f"That file contains {num_commas + 1} values.")
