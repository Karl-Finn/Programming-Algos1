import requests

# 1. RETRIEVE THE SPEECH FROM THE WEB
speech_retrieve = requests.get("http://193.1.33.31:88/pa1/gettysburg.txt")
speech_headers = speech_retrieve.headers
body = speech_retrieve.text  # .text produces the content as <str>

# 2. FORMAT THE SPEECH CONTENTS TO SOMETHING WE CAN WORK WITH (will result in 1 long sentence)
# speech_lower = body.lower() # converts all letters to lower case
# speech_no_period = speech_lower.replace(".", "") # removes all full-stops by replacing them with "" (i.e. nothing)
# speech_no_comma = speech_no_period.replace(",", "") # removes all commas by replacing them with ""
# speech_no_el = speech_no_comma.replace("\n\n", " ") # removes the end-line characters

# NB: Lines 8, 9, 10, 11 can all be done with the following
speech_formatted = body.lower().replace(".", "").replace(",", "").replace("-", " ").replace("\n\n", " ")
speech_word_list = speech_formatted.split()

# 3. RETRIEVE THE STOPWORDS FROM THE WEB
stopwords_retrieve = requests.get("http://193.1.33.31:88/pa1/stopwords.txt")
stopwords_headers = stopwords_retrieve.headers
stopwords = stopwords_retrieve.text
stopwords_list = stopwords.split(sep=",")

# 4. CREATE A LIST OF WORDS FROM THE SPEECH THAT DOES NOT INCLUDE ANY OF THE STOP-WORDS
unique_words = [word for word in speech_word_list if word not in stopwords_list]

# 5. CREATE A DICTIONARY THAT COUNTS HOW MANY TIMES A UNIQUE WORD APPEARS IN THE SPEECH
unique_words_dict = dict()
for word in unique_words:
    if word not in unique_words_dict:
        unique_words_dict[word] = 1
    else:
        unique_words_dict[word] += 1
for k, v in unique_words_dict.items():
    print(f"'{k}': {v}")
