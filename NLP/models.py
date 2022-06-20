import pickle

class fake_news_models:
    __models = None

    def __init__(self, filename):
        with open(filename, "rb") as fp:
            self.__models = pickle.load(fp)
            print("Models are loaded successfuly: ",self.__models.keys())

    def get_model(self,key):
        return self.__models[key]["model"]

    def get_models_names(self):
        return self.__models.keys()

    def get_accuracy(self,key):
        return round(self.__models[key]["acc"]*100,2)