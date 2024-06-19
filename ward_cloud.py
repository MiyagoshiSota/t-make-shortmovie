from janome.tokenizer import Tokenizer
from wordcloud import WordCloud

file_name = "./tiktok_fashion_en.txt"
stop_words = {"英語", "語", "勉強'"}

with open(file_name, 'r', encoding='UTF-8') as f:
    text = f.read()

t = Tokenizer()

s = []
for token in t.tokenize(text):
    p = token.part_of_speech.split(",")
    if "名詞" in p:
        s.append(token.surface)

wc = WordCloud(width=640,
               height=480,
               stopwords=stop_words,
               font_path="/System/Library/Fonts/Arial Unicode.ttf")

wc.generate(" ".join(s))
wc.to_file('result-j.png')
