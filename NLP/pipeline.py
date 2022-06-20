from numpy import argmax
from models import fake_news_models
from preprocessing import fake_news_preprocessing
import sys
import os

class fake_news_pipeline:
    __models = None
    __preprocessing = None

    def __init__(self, filename=None, models=None):
        if not models:
            self.__models = fake_news_models(filename)
        else:
            self.__models = models
        self.__preprocessing = fake_news_preprocessing()

    def predict(self, str, model="sc"):
        data = self.__preprocessing.preprocess(str)

        if not set(["svd","bow"]).issubset(set(self.__models.get_models_names())):
            raise Exception("Invalid model file, SVD and BoW not found!")
        
        data = ' '.join(data)
        bow = self.__models.get_model("bow")
        data = bow.transform([data])

        svd = self.__models.get_model("svd")
        data = svd.transform(data)


        pred_model = self.__models.get_model(model)
        prob = pred_model.predict_proba(data)
        return {"prob":prob,"class":argmax(prob)}


if __name__ == "__main__":
    models = fake_news_models(os.getcwd()+'/models/models.bin')
    pipeline = fake_news_pipeline(models=models)

    if len(sys.argv) != 3:
        print("Usage: <News> <Classifier Name>!")
        exit(1)
    
    print(pipeline.predict(sys.argv[1],sys.argv[2]))
