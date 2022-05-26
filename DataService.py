from typing import List
import nltk
from nltk.corpus import wordnet


class DataService:
    @staticmethod
    def getRelatedWords(words: List):

        resObj = {}

        for word in words:

            synonyms = []
            antonyms = []

            for syn in wordnet.synsets(word):
                for l in syn.lemmas():
                    synonyms.append(l.name())
                    if l.antonyms():
                        antonyms.append(l.antonyms()[0].name())

            resObj[word.lower()] = {
                "synonyms": list(set(synonyms)),
                "antonyms": list(set(antonyms)),
            }
            
        return resObj
