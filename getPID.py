import os
Description = input("name: ")
# Running the aforementioned command and saving its output
output = os.popen("wmic service where name=\"{}\" get Processid".format(Description)).read()
# Displaying the output
lines = output.split("\n")
print(lines[2])