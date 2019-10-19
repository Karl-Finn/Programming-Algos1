# Does what was required of Lab 5 but instead of just printing the answer it adds the required lines to
# a new text file (lab5_answer.txt)

output = "lab5_answer.txt"

with open(output, 'w') as out:  # opens the txt file and deletes its current content
    filename = 'hnr1.abc'
    with open(filename, 'r') as f:
        X, T, M, K = "", "", "", ""
        for line in f:
            if line[0] == "X":
                X = line[2:-1]
            elif line[0] == "T":
                if T:  # multiple T lines in each block (we only want the first) this checks if T is already assigned
                    continue  # If it is, then we go back to line 7 and continue with the next line in the file!
                else:
                    T = line[2:-1]
            elif line[0] == "M":
                M = line[2:-1]
            elif line[0] == "K":
                K = line[2:-1]
                out.write("{0} ... {1} ... Time sig: {2} ... Key sig: {3}\n".format(X, T, M, K))
                X, T, M, K = "", "", "", ""
# Line 22 writes each of the required lines extracted from hnr1.abc to lab5_answer.txt
