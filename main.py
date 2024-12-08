from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

font_path = r"C:\Users\masum\Desktop\Python'\Avigea Italic.TTF"
with open('names.txt', 'r') as file:
    text = file.read()
python_mask = np.array(PIL.Image.open("masum.png"))

wc = WordCloud(stopwords=STOPWORDS, mask=python_mask, background_color="white", contour_color="red",contour_width=8, min_font_size=0,max_words=50, font_path=font_path).generate(text)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
