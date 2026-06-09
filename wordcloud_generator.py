from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = """
Artificial Intelligence is transforming industries across the world.
Machine learning and deep learning are subsets of Artificial Intelligence.
AI helps businesses automate processes, improve decision making,
analyze large amounts of data, and develop intelligent applications.
Natural Language Processing enables computers to understand human language.
Computer Vision helps machines interpret images and videos.
AI is widely used in healthcare, finance, education, cybersecurity,
and software development to improve efficiency and innovation.
"""

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white"
).generate(text)

wordcloud.to_file("wordcloud.png")

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

print("Word cloud saved as 'wordcloud.png'")