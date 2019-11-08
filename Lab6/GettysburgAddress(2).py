import self_functions

# 1. Get the files from the net
speech_url = "http://193.1.33.31:88/pa1/gettysburg.txt"
body = self_functions.get_text_file_from_net(speech_url)

stopwords_url = "http://193.1.33.31:88/pa1/stopwords.txt"
stopwords = self_functions.get_text_file_from_net(stopwords_url)

# 2. Make a list of the words of each file
speech_word_list = self_functions.format_txt_file_as_list(body)
stopwords_list = stopwords.split(sep=",")

# 3. Create a list of UNIQUE words I.E. words in the speech that are not in stopwords_list.
unique_words = self_functions.uniqueWordsList(speech_word_list, stopwords_list)

# 4. Create a dictionary that counts the unique words.
unique_words_dict = dict()
for word in unique_words:
    if word not in unique_words_dict:
        unique_words_dict[word] = 1
    else:
        unique_words_dict[word] += 1

# 6. Output the total amount of unique words; what they are; and their count in the speech.
print("----------------------------------------------------------------")
print(f"There are {len(unique_words_dict)} unique words in the speech.")
print("----------------------------------------------------------------")
print(f"Each word and how many times it appears in the speech:\n")
# 6.1. PRINT ROWS OF 10 key-value pairs INSTEAD OF ONE LONG COLUMN
count = 1
for k, v in unique_words_dict.items():
    if count < 10: # will print 9 key-value pairs in a row
        print(f"'{k}': {v}", end='    ')
        count += 1
    else: # on the 10th key-value pair 'count' be re-initialized to 1
        count = 1
        print(f"'{k}': {v}") # and we print the 10th key-value pair for that row
