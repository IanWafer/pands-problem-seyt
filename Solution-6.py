# Ian Wafer 03-03-2019
# Solution to problem 6
# Output every second word of user string input

print(" ".join(input("Please enter a sentence: ").split(" ")[0::2]))    # From list generated by splitting string x with seperated words by " " (space) between them join the obtained words starting at the initial point (0). Make a new list in increments of 2 till the end of the original list. Join these values together seperated by a " " (space) and print output.  