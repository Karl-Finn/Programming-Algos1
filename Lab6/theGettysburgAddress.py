import requests

# 1. RETRIEVE THE SPEECH FROM THE WEB
speech_retrieve = requests.get("http://193.1.33.31:88/pa1/gettysburg.txt")
speech_headers = speech_retrieve.headers
body = speech_retrieve.text  # '.text' produces the content as <str>

# 2. FORMAT THE SPEECH CONTENTS TO SOMETHING WE CAN WORK WITH (will result in 1 long sentence)
speech_formatted = body.lower()\
    .replace(".", "")\
    .replace(",", "")\
    .replace("-", " ")\
    .replace("\n\n", " ")
speech_word_list = speech_formatted.split()

# 3. RETRIEVE THE STOPWORDS FROM THE WEB & CREATE A LIST OF EACH WORD
stopwords_retrieve = requests.get("http://193.1.33.31:88/pa1/stopwords.txt")
stopwords_headers = stopwords_retrieve.headers
stopwords = stopwords_retrieve.text
stopwords_list = stopwords.split(sep=",") # creates a list of each word

# 4. CREATE A LIST OF UNIQUE WORDS (WORDS IN SPEECH MINUS ANY STOP-WORDS)
unique_words = [word for word in speech_word_list if word not in stopwords_list] # list comprehension

# 5. CREATE A DICTIONARY THAT COUNTS HOW MANY TIMES A UNIQUE WORD APPEARS IN THE SPEECH
unique_words_dict = dict()
for word in unique_words:
    if word not in unique_words_dict:
        unique_words_dict[word] = 1
    else:
        unique_words_dict[word] += 1

# 6. OUTPUT THE TOTAL AMOUNT OF UNIQUE WORDS AND HOW MANY TIMES EACH WORD OCCURS IN SPEECH
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
        print(f"{k}: {v}") # and we print the 10th key-value pair for that row

