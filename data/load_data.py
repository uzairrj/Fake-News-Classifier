import pandas as pd
import plotly.express as plot

class fake_news_data:
    __data = None

    def __init__(self, filepath):
        self.__data = pd.read_csv(filepath)

    def get_data(self):
        return self.__data

    def getDataShape(self):
        return self.__data.shape

    def getUniqueAuthors(self):
        return len(self.__data.author.unique())

    def getTopTenAuthors(self):
        topAuthors = self.__data.author.value_counts()[:10]
        return plot.bar(x=topAuthors.keys(), y=topAuthors.values, labels={"x":"Authors","y":"Number of News"}, template="plotly_dark")

    def getTopTenFakeAuthors(self):
        topFakeAuthors = self.__data[self.__data.label == 1].author.value_counts()[:10]
        return plot.bar(x=topFakeAuthors.keys(), y=topFakeAuthors.values, labels={"x":"Authors","y":"Number of Fake News"},template="plotly_dark")

    def getTopTenRealAuthors(self):
        topRealAuthors = self.__data[self.__data.label == 0].author.value_counts()[:10]
        return plot.bar(x=topRealAuthors.keys(), y=topRealAuthors.values, labels={"x":"Authors","y":"Number of Real News"}, template="plotly_dark")

    def getFakeVsRealCount(self):
        labelCount = self.__data.label.value_counts()
        return plot.pie(values = labelCount.values, names=["Fake","Real"], template="plotly_dark")
    
