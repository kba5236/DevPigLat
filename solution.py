#Kayla Armstrong
def enhanceThis(text):
    wordList = text.split(' ',100)
    vowelList = ['a','e','i','o','u']
    wordListIndex = 0
    enhancedList = []
    while wordListIndex<len(wordList):
        word = wordList[wordListIndex]
        vowelIndex=-1
        letterIndex=0

        while letterIndex<len(word):
            letter = word[letterIndex:letterIndex+1]
         
            for vowel in vowelList:
         
                if letter==vowel and vowelIndex==-1:
                    vowelIndex = letterIndex
                    break

            letterIndex+=1
           # print('word: {}  vowelIndex: {}'.format(word,vowelIndex))
        if vowelIndex==0:
            word = word + "yay"
        else:
            word = word[vowelIndex:] + word[0:vowelIndex] + "ay"
        wordListIndex+=1
        enhancedList.append(word)
    s = ' '
    enhancedString = s.join(enhancedList)
    return enhancedString