import pickle

class fake_news_models:
    __models = None

    def __init__(self, filename):
        with open(filename, "rb") as fp:
            __models = pickle.load(fp)
            print("Models are loaded successfuly: ",__models.keys())

    def get_model(self,key):
        return self.__models[key]

    def get_accuracy(self,key):
        pass