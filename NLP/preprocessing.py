from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from tqdm.notebook import tqdm as tqdm

class fake_news_detector:
    __nltk_STOPWORDS = None

    def __init__(self):
        self.__nltk_STOPWORDS = set(stopwords.words("english"))
        print("Data and Model Loaded!")
    
    def __toLower(self,tokens):
        return [t.lower() for t in tokens]

    def __removePunctuation(self, tokens):
        return [t for t in tokens if t.isalpha()]

    def __removeStopwords(self,tokens):
        return [t for t in tokens if t not in self.__nltk_STOPWORDS]
    
    def __removeSingleLenWords(self,tokens):
        return [t for t in tokens if len(t) >= 2]
    
    def __lematize(self, tokens, lematizer):
        tokens = [lematizer.lemmatize(t, pos = "v") for t in tokens]
        return [lematizer.lemmatize(t, pos = "n") for t in tokens]

    def preprocess(self,str):
        MAX_LEN = 18064
        data = None
        #tokenize
        data = word_tokenize(str)
        #converting text to lowercase
        data = self.__toLower(data)
        #Removing punctuations
        data = self.__removePunctuation(data)
        #removing stopwords
        data = self.__removeStopwords(data)
        #remove words less then 3 char
        data = self.__removeSingleLenWords(data)
        #lemitization
        lemme = WordNetLemmatizer()
        data = self.__lematize(data,lemme)

        return data


    