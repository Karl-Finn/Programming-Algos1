# Please see contents description.txt for what this program was required to do

filename = 'hnr1.abc'

with open(filename, 'r') as f:
    X, T, M, K = "", "", "", ""
    for line in f:
        if line[:2] == "X:":
            if X:
                X, T, M, K = "", "", "", ""
            X = line[2:-1]
        elif line[:2] == "T:":
            if T: #as the are multiple T lines in each block (and we only want the first in each) this checks if T is already assigned
                continue #If it is, then we go back to line 7 and continue with the next line in the file!
            else:
                T = line[2:-1]
        elif line[:2] == "M:":
            M = line[2:-1]
        elif line[:2] == "K:":
            K = line[2:-1]
            print("{0} ... {1} ... Time sig: {2} ... Key sig: {3}".format(X, T, M, K))
            # X, T, M, K = "", "", "", ""

# originally lines 9 and 10 were not in the program 
# this won't work correctly if, by chance, K: comes before M:
# if this happens then all variables will be wiped (re-initialized as empty strings)
# ***added lines 7 and 8 to fix it*** 
