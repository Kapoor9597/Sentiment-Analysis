#loading libraries
import nltk
import tkinter as tk
import tkinter.messagebox
import re

class myapp(tk.Tk):
    #The Tk class is instantiated without arguments. This creates a toplevel widget of Tk which usually is the main window of an application.
    #Each instance has its own associated Tcl interpreter.

    def __init__(self):
        tk.Tk.__init__(self)
        w = 140
        h = 200
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        #center the window on screen
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.geometry('%dx%d+%d+%d' %(w,h,x,y))
        
        #The Entry widget is a standard Tkinter widget
        #used to enter or display a single line of text.
        self.entry = tk.Entry(self)
        self.entry.pack()
        close_button = tk.Button(self, text='Close', command=self.close)
        close_button.pack()
        run_button = tk.Button(self, text='Analyze', command=self.analyze)
        run_button.pack()
        l1 = tk.Label(text="Positive")
        l1.pack()
        self.entry1 = tk.Entry(self.getvalue1())
        self.entry1.pack()
        l2 = tk.Label(text="Negative")
        l2.pack()
        self.entry2 = tk.Entry(self.getvalue2())
        self.entry2.pack()
        self.string = ""
        result_btn = tk.Button(self, text='Result', command=self.result)
        result_btn.pack()

    def result(self):
        pos_result = self.getvalue1()
        neg_result = self.getvalue2()

        if(pos_result > neg_result):
            tk.messagebox.showinfo("Sentiment Analysis", "The statement you entered conveyed a positive meaning")
        elif (pos_result < neg_result):
            tk.messagebox.showinfo("Sentiment Analysis", "The statement you entered conveyed a negative meaning")
        elif (pos_result == neg_result):
            tk.messagebox.showinfo("Sentiment Analysis", "The statement you entered is neutral (nor positive neither negative)")

    def analyze(self):
        self.string = self.entry.get()
        val = self.string
        process(val)
        self.entry1.delete(0,'end')
        self.entry2.delete(0,'end')
        self.entry1.insert(0,myvalue1())
        self.entry2.insert(0,myvalue2())

    def close(self):
        global result
        self.string = self.entry.get()
        self.destroy()

    def mainloop(self):
        tk.Tk.mainloop(self)
        return self.string

    def getvalue1(self):
        return myvalue1()

    def getvalue2(self):
        return myvalue2()

pos_ratio , neg_ratio = 0, 0

def get_word_features(wordList):
    wordlist = nltk.FreqDist(wordList)
    print(wordlist)
    #print (wordlist.most_common(5))
    word_features = wordlist.keys()
    return word_features

def process(stmt):
    sentence = re.sub('[!@#$%&*,;:]', '', stmt)
    #print (sentence)
    words_filter = []
    for words in  sentence:
         words_filter = [e.lower() for e in sentence.split() if len(e) >= 3]

    print(words_filter)
    stmnt = []
    pos_count = 0
    neg_count = 0
    word_features = get_word_features(words_filter)
    print(word_features)
    file_content = open("positive.txt").read()
    pos_words = nltk.word_tokenize(file_content)
    #print(pos_words)
    file_content = open("negative.txt").read()
    neg_words = nltk.word_tokenize(file_content)

    for i in word_features:
        for j in pos_words:
            if(i == j):
                pos_count += 1

    for i in word_features:
        for j in neg_words:
            if(i == j):
                neg_count += 1

    #print(pos_count)
    #print(neg_count)
    global pos_ratio
    global neg_ratio
    pos_ratio = (pos_count/(pos_count + neg_count))*100
    neg_ratio = (neg_count/(neg_count + pos_count))*100
    #print(pos_ratio)
    #print(neg_ratio)

def myvalue1():
    global pos_ratio
    return pos_ratio

def myvalue2():
    global neg_ratio
    return neg_ratio

print ("Please Enter a String ")
app = myapp()
result = app.mainloop()
process(result)
print("You Entered : ", result)
