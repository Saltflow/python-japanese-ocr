import os
import glob
from splitandocr import remove_dir

path = "./pictures/*.jpg"

dirname = "allresult"
remove_dir(dirname)
os.mkdir(dirname)

files = glob.glob(path)
count = 0
for file in files:
    os.system("python3 ./splitandocr.py "+file)
    os.system("python3 ./splitandocr.py "+file+" --ocr")
    sentence = ""
    article = []
    with open("results.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            sentence += line[0:-1]
            if(line.find('。') != -1):
                article.append(sentence)
                sentence = ""
    pre_name = os.path.splitext(os.path.basename(file))[0]
    os.remove("results.txt")
    with open(os.path.join(dirname,pre_name+".txt"),"w") as f:
        for sentence in article:
            f.write(sentence+"\n")
