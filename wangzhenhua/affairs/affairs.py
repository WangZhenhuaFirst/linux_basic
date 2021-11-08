import pandas as pd


def get_data():
    data = pd.read_csv('https://mirror.coggle.club/dataset/affairs.txt')
    return data
