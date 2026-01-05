import os

# Specify the directory path (you can change this)
directory = "."

# Get the list of all entries in the directory
contents = os.listdir(directory)

# Print the entries one by one
print(f"Contents of directory '{directory}':")
for item in contents:
    print(item)
