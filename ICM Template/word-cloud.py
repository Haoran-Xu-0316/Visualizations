import jieba  # 分词库
import matplotlib.pyplot as plt  # 数学绘图库
import numpy as np  # 科学数值计算包，可用来存储和处理大型矩阵
from PIL import Image
from wordcloud import ImageColorGenerator, WordCloud  # 词云库

#text = open(r"C:\Users\徐浩然\Desktop\DDL-January 28, 2023\Proposal (revised).docx", encoding="utf-8").read()

f = open(r'C:\Users\徐浩然\Desktop\轻食商家访谈.docx','r',encoding = 'utf-8')
text = f.read()
f.close
image = Image.open(r'C:\Users\徐浩然\Desktop\微信图片_20230222180652.jpg')
graph = np.array(image)

wc = WordCloud(font_path=r"C:\Windows\Fonts\pala.ttf", background_color='white', max_font_size=500,mask=graph,scale=40)
wc.generate(text)

image_color = ImageColorGenerator(graph)
wc.recolor(color_func=image_color)
# wc.to_file(r'C:/Users/徐浩然/Desktop/美赛Figure_Template\346346123432.png')

plt.imshow(wc,interpolation='bilinear')
plt.axis("off")  # 关闭图像坐标系
plt.show()

'''
width                                                          # 指定词云对象生成图片的宽度，默认400像素
height                                                         # 指定词云对象生成图片的高度，默认200像素
min_font_size                                                  # 指定词云中字体的最小字号，默认4号
max_font_size                                                  # 指定词云中字体的最大字号，默认根据高度自动调节
font_step                                                      # 指定词云中字体字号的步进间隔，默认为1
font_path                                                      # 指定字体文件的路径，默认None
max_words                                                      # 指定词云显示的最大单词数量，默认200
stop_words                                                     # 指定词云的排除词列表，即不显示的单词列表
background_color                                               # 指定词云图片的背景颜色，默认为黑色


wordcloud = WordCloud(background_color="white",\
                      width = 800,\
                      height = 600,\
                      max_words = 200,\
                      max_font_size = 80,\
                      mask = mask,\
                      contour_width = 3,\
                      contour_color = 'steelblue'
                      ).generate(txt)
wordcloud.to_file('Alice_词云图.png')

'''