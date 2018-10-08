from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator


def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", "i", "that", "for", "you", "he", "with",
                   "on", "do", "say", "this", "they", "is", "an", "at", "but", "we", "his", "from", "that", "not", "by",
                   "she", "or", "as", "what", "go", "their", "can", "who", "get", "if", "would", "her", "all", "my",
                   "make", "about", "know", "will", "as", "up", "one", "time", "has", "been", "there", "year", "so",
                   "think", "when", "which", "them", "some", "me", "people", "take", "out", "into", "just", "see",
                   "him", "your", "come", "could", "now", "than", "like", "other", "how", "then", "its", "our", "two",
                   "more", "these", "want", "way", "look", "first", "also", "new", "because", "day", "more", "use",
                   "no", "man", "find", "here", "thing", "give", "many", "well"]
    for word in ngram:
        if word in commonWords:
            return True
    return False


def cleanText(input):
    input = re.sub('\n+', " ", input).lower()
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = re.sub("u\.s\.", "us", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    return input


def cleanInput(input):
    input = cleanText(input)
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    print(len(cleanInput))
    return cleanInput


def getNgrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input) - n + 1):
        ngramTemp = " ".join(input[i:i + n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output


def getFirstSentenceContaining(ngram, content):
    # print(ngram)
    sentences = content.split(".")
    # print(sentences)
    for sentence in sentences:
        if ngram in sentence.lower():
            return sentence
    return ""


content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
# print(content)
ngrams = getNgrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(len(sortedNGrams))

selected_ngrams = []
for item in sortedNGrams:
    if item[1] > 2 and not isCommon(item[0].split()):
        selected_ngrams.append(item)
print(selected_ngrams)
print('the number of the significant 2-grams is:' + str(len(selected_ngrams)))

count = 0
for ngram in selected_ngrams:
    count += 1
    print(ngram)
    print(getFirstSentenceContaining(ngram[0], content))
    if count > 5:
        break