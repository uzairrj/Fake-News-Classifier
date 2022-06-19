from numpy import argmax
from models import fake_news_models
from preprocessing import fake_news_preprocessing

class fake_news_pipeline:
    __models = None
    __preprocessing = None

    def __init__(self, filename):
        self.__models = fake_news_models(filename)
        self.__preprocessing = fake_news_preprocessing()

    def predict(self, str, model="sc"):
        data = self.__preprocessing.preprocess(str)

        if ["svd","bow"] not in self.__models.keys():
            raise Exception("Invalid model file, SVD and BoW not found!")
        
        bow = self.__models.get_model("bow")
        data = bow.transform(data)

        svd = self.__models.get_model("svd")
        data = svd.transform(data)

        pred_model = self.__models.get_model(model)
        prob = pred_model.predict_proba(data)
        return {"prob":prob,"class":argmax(prob)}
