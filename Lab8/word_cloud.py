"""An add-on to the Gettysburg exercise: Create a word cloud of the unique words"""

import self_functions as mf

speech_url = "http://193.1.33.31:88/pa1/gettysburg.txt"
speech_body = mf.get_text_file_from_net(speech_url)
speech_word_list = mf.format_txt_file_as_list(speech_body)

stopwords_url = "http://193.1.33.31:88/pa1/stopwords.txt"
stopwords_body = mf.get_text_file_from_net(stopwords_url)
stopwords_list = stopwords_body.split(sep=",")

unique_words = mf.uniqueWordsList(speech_word_list, stopwords_list)

unique_word_hist = mf.wordHist(unique_words)

html_start_text = "<!DOCTYPE html>\n" \
           "<html>\n<head lang=\"en\">\n" \
           "<meta charset=\"UTF-8\">\n" \
           "<title>Tag Cloud Generator</title>\n" \
           "</head>\n" \
           "<body>\n" \
           "<div style=\"text-align: center; vertical-align: middle; font-family: arial; color: white; " \
           "background-color:black; border:1px solid black\">\n"
html_end_text = "</div>\n" \
                "</body>\n" \
                "</html>"

with open("cloud_tag.html", 'w') as cloud:
    cloud.write(html_start_text)
    for k, v in unique_word_hist.items():
        cloud.write(f"<span style=\"font-size: {min(v * 20, 200)}px\"> {k} </span>\n")
    cloud.write(html_end_text)
