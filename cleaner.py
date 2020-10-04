import os
from glob import glob
from shutil import copy
import tensorflow as tf

def cleaner(counter):
    for root, dirs, files in os.walk('/Users/compton/Downloads/Emotion_labels(2)'):
        if files:
            with open("{}/{}".format(root, files[0])) as f:
                emotion_score = float(f.readline().strip())
                file_list = glob(
                    '/Users/compton/Downloads/extended-cohn-kanade-images(4)/cohn-kanade-images/{}/*'.format(
                        "/".join(root.split('/')[-2:])))
                file_list.sort()
                if emotion_score == 0:
                    copy_all(file_list, '/Users/compton/Downloads/faces/neutral/', counter)
                elif emotion_score == 1:
                    copy_all(file_list, '/Users/compton/Downloads/faces/anger/', counter)
                elif emotion_score == 2:
                    copy_all(file_list, '/Users/compton/Downloads/faces/contempt/', counter)
                elif emotion_score == 3:
                    copy_all(file_list, '/Users/compton/Downloads/faces/disgust/', counter)
                elif emotion_score == 4:
                    copy_all(file_list, '/Users/compton/Downloads/faces/fear/', counter)
                elif emotion_score == 5:
                    copy_all(file_list, '/Users/compton/Downloads/faces/happiness/', counter)
                elif emotion_score == 6:
                    copy_all(file_list, '/Users/compton/Downloads/faces/sadness/', counter)
                elif emotion_score == 7:
                    copy_all(file_list, '/Users/compton/Downloads/faces/surprise/', counter)
            print("==================================")


def copy_all(from_dir, to, count):
    file_count = len(next(os.walk(to))[2])
    if file_count < 100 and len(from_dir) >= count:
        for i in from_dir[-count:]:
            copy(i, to)


def classifier():
    anger_count = len(next(os.walk("/Users/compton/Downloads/faces/anger/"))[2])
    contempt_count = len(next(os.walk("/Users/compton/Downloads/faces/contempt/"))[2])
    disgust_count = len(next(os.walk("/Users/compton/Downloads/faces/disgust/"))[2])
    fear_count = len(next(os.walk("/Users/compton/Downloads/faces/fear/"))[2])
    happiness_count = len(next(os.walk("/Users/compton/Downloads/faces/happiness/"))[2])
    sadness_count = len(next(os.walk("/Users/compton/Downloads/faces/sadness/"))[2])
    neutral_count = len(next(os.walk("/Users/compton/Downloads/faces/neutral/"))[2])
    surprise_count = len(next(os.walk("/Users/compton/Downloads/faces/surprise/"))[2])
    lens = [anger_count, contempt_count, disgust_count, surprise_count, sadness_count, happiness_count, fear_count, neutral_count]
    min_len = min(lens)

    counter = 1
    print(min_len)
    for i in lens:
        print(i)
    while min_len < 100:
        print(min_len)
        cleaner(counter)
        anger_count = len(next(os.walk("/Users/compton/Downloads/faces/anger/"))[2])
        contempt_count = len(next(os.walk("/Users/compton/Downloads/faces/contempt/"))[2])
        disgust_count = len(next(os.walk("/Users/compton/Downloads/faces/disgust/"))[2])
        fear_count = len(next(os.walk("/Users/compton/Downloads/faces/fear/"))[2])
        happiness_count = len(next(os.walk("/Users/compton/Downloads/faces/happiness/"))[2])
        sadness_count = len(next(os.walk("/Users/compton/Downloads/faces/sadness/"))[2])
        surprise_count = len(next(os.walk("/Users/compton/Downloads/faces/surprise/"))[2])
        lens = [anger_count, contempt_count, disgust_count, surprise_count, sadness_count, happiness_count, fear_count]
        min_len = min(lens)
        counter += 1


classifier()
