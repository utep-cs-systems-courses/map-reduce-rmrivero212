#Ryan Rivero Map Reduce Submission
#WORDS:hate,love,death,night,sleep,time,henry,hamlet,you,my,blood,poison,macbeth,kind,heart,honest
import time
import pymp



def readFile():
    global f1, f2, f3, f4, f5, f6, f7, f8
    f1 = open("shakespeare1.txt", "r")
    f2 = open("shakespeare2.txt", "r")
    f3 = open("shakespeare3.txt", "r")
    f4 = open("shakespeare4.txt", "r")
    f5 = open("shakespeare5.txt", "r")
    f6 = open("shakespeare6.txt", "r")
    f7 = open("shakespeare7.txt", "r")
    f8 = open("shakespeare8.txt", "r")
    

def createArrayOfTexts():
    readFile()
    texts = []
    texts.append(f1.read())
    texts.append(f2.read())
    texts.append(f3.read())
    texts.append(f4.read())
    texts.append(f5.read())
    texts.append(f6.read())
    texts.append(f7.read())
    texts.append(f8.read())
    return texts
    
def countTargetWord(target, texts):
    wordCount = 0;
    for text in texts:
        wordCount += text.count(target)
        wordCount += text.count(target.capitalize())
        wordCount += text.count(target.upper())
    return wordCount

def main():

    
    strings = createArrayOfTexts()
    count = countTargetWord("you", strings)

    print('number of occurences: ', count)
    
    
    
    
    

if __name__=='__main__':
    # execute only if run as a script
    main()
