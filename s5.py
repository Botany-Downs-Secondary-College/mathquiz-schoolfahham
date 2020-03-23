#MathQuiz programme that uses GUI with classes, generates questions, responds to user answer and gives a report/
#s5.py
#Fahham Ahmad 3/20

from tkinter import * #imports all modules of tool kit interface (tkinter), * is a called wildcard/
from random import *

class MathQuiz: #OOP will have classes and functions will be part of classes. Keep the widgets in (__init__) method, each instance (object) must have 'self' as prefix/

    def __init__(self, parent):

        #Widgets for frame 1/

        self.frame1 = Frame(parent)
        self.frame1.grid(row = 0, column = 0)

        self.TitleLabel = Label(self.frame1, bg = "black", fg = "white", width = 30, padx = 30, pady = 10, text = "Welcome to Math Quiz", font = ("Times", "16", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)

        self.NameLabel = Label(self.frame1, text = "Name", width = 20, font = ("Times", "14", "bold italic"))
        self.NameLabel.grid(row = 2, column = 0, sticky = W)

        #Checking to see something is entered/

        self.name = StringVar()
        self.name.set("")
        self.NameEntry = Entry(self.frame1, textvariable = self.name, width = 20) #Text box/
        self.NameEntry.grid(row = 2, column = 1, sticky = W)

        self.AgeLabel = Label(self.frame1, text = "Age", width = 20, font = ("Times", "14", "bold italic"))
        self.AgeLabel.grid(row = 3, column = 0, sticky = W)

        self.age = IntVar()
        self.age.set("")
        self.AgeEntry = Entry(self.frame1, width = 20, textvariable = self.age) #Text box/
        self.AgeEntry.grid(row = 3, column = 1, sticky = W)

        self.warning = Label(self.frame1, text = "")
        self.warning.grid(row = 4, column = 1, columnspan = 3)

        self.SelectLabel = Label(self.frame1, text = "Select DIfficulty", width = 20, font = ("Times", "14", "bold italic"))
        self.SelectLabel.grid(row = 5, column = 0, sticky = W)

        #Radio buttons with 'for' loop for efficiency/

        self.diff = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        self.diff_btns = []

        for i in range(len(self.diff)):
            rb = Radiobutton(self.frame1, variable = self.diff_lvl, value = i, text = self.diff[i], anchor = W, padx = 50, width = "10", height = "2")
            self.diff_btns.append(rb)
            rb.grid(row = i+6, column = 0, sticky = W)

        #Buttons that call frame2/

        self.submit = Button(self.frame1, text = "Next", command = self.show_frame2)
        self.submit.grid(row = 9, column = 1)

        #Widgets for frame2/

        self.index = 0
        self.score = 0
        self.frame2 = Frame(parent, height = "450", width = "400") #notice grid() method is missing here/

        self.questions = Label(self.frame2, bg = "black", fg = "white", width = 30, padx = 30, pady = 10, text = "Quiz Questions", font=("Times", "14", "bold italic"))
        self.questions.grid(row = 0, columnspan = 3)

        self.QuestionLabel = Label(self.frame2, text = "Click Next", width = 15, height = 3) #empty lable to print questions/
        self.QuestionLabel.grid(row = 1, column = 0, sticky = W)

        self.AnswerEntry = Entry(self.frame2, width = 20) #Text box/
        self.AnswerEntry.grid(row = 1, column = 1, sticky = W)

        self.quiz_label = Label(self.frame2, text = "Problems", font = ("Times", "14", "bold italic"))
        self.quiz_label.grid(row = 1, column = 2, columnspan = 5, sticky = "EW")

        self.feedback = Label(self.frame2, text = "Click Check Answer Button")
        self.feedback.grid(row = 2, column = 0, columnspan = 4)

        self.home = Button(self.frame2, text = "Home", anchor = W, command = self.show_frame1)
        self.home.grid(row = 3, column = 0)

        self.check = Button(self.frame2, text = "Check Answer", anchor = W, command = self.check_answer)
        self.check.grid(row = 3, column = 1)

        #Widgets for report frame/
        self.report_frame = Frame(parent, height = "450", width = "400")
        self.report_frame.grid_propagate(0)
        #creating labels for report headings using 'for' loop/
        report_page = ["Name", "Age", "Score"]
        self.report_labels = []

        for i in range(len(report_page)):
            lb = Label(self.report_frame, text = report_page[i], anchor = W, width = "7", height = "2", font = ("Times", "22", "bold"))
            self.report_labels.append(lb)
            lb.grid(row = 1, column = i+1, sticky = "EW")

        self.report_name = Label(self.report_frame, textvariable = self.name)
        self.report_name.grid(row = 3, column = 1, sticky = "EW")

        self.report_age = Label(self.report_frame, textvariable = self.age)
        self.report_age.grid(row = 3, column = 2, sticky = "")

        self.report_score = Label(self.report_frame, text = "")
        self.report_score.grid(row = 3, column = 3)

    def show_frame1(self):
        self.frame2.grid_remove()#removes frame 2/
        self.report_frame.grid_remove()
        self.frame1.grid()

    def show_frame2(self):
        try:
            #instances created to check if input data is correct for the variables/
            if self.name.get() == "":
                self.warning.configure(text = "Please enter your name")
                self.NameEntry.focus()
            elif self.name.get().isalpha() == False:
                self.warning.configure(text = "Please enter text")
                self.NameEntry.delete(0, END)
                self.NameEntry.focus()

            elif self.AgeEntry.get() == "":
                self.warning.configure(text = "Please enter a number")
                self.AgeEntry.delete(0, END)

            elif self.age.get()>12:
                self.warning.configure(text = "You're too old to play this game!!!")
                self.age_entry.delete(0, END)

            elif self.age.get()<=0:
                self.warning_configure(text = "Please enter a number greater than 0")
                self.age_entry.delete(0, END)

            elif self.age.get() <=7:
                self.warning.configure(text = "Oh No! You're too young to play this game!!!")

            else:
                self.frame1.grid_remove()
                self.frame2.grid(row = 1, columnspan = 4)
                self.next_problem()

        except ValueError:
            self.warning.configure(text = "Please enter a number")
            self.AgeEntry.delete(0, END)
            self.AgeEntry.focus()

    def check_answer(self):
        #instance created to check answer uses has inputed/
        try:
            ans = int(self.AnswerEntry.get())

            if ans == self.answer:
                self.feedback.configure(text = "Correct!")
                self.score += 1
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_problem()
            else:
                self.feedback.configure(text = "Unlucky! Try again next time!")
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_problem()

        except ValueError:
            self.feedback.configure(text = "This is not a number")
            self.AnswerEntry.delete(0, END)
            self.AnswerEntry.focus()

        if self.score <=5:
            self.report_score.configure(text = str(self.score))

    def next_problem(self):
        #Creates a problem, stores the correct answer/
        x = randrange(10)
        y = randrange(10)
        self.select = self.diff_lvl.get()

        if self.select == "0":
            easy_text = str(x) + "  +  " + str(y) + "  =  "

            self.answer = x + y
            self.index += 1

            self.QuestionLabel.configure(text = easy_text)
            self.quiz_label.configure(text = "Question" + str(self.index)+ "/5")

        elif self.select == "1":
            medium_text = str(x) + "  -  " + str(y) + "  =  "

            self.answer = x - y
            self.index += 1

            self.QuestionLabel.configure(text = medium_text)
            self.quiz_label.configure(text = "Question" + str(self.index)+ "/5")

        else:

            hard_text = str(x) + "  x  " + str(y) + "  =  "

            self.answer = x * y
            self.index += 1

            self.QuestionLabel.configure(text = hard_text)
            self.quiz_label.configure(text = "Question" + str(self.index) + "/5")

        if self.index >= 6:
            self.frame2.grid_remove()
            self.report_frame.grid(row = 1, columnspan = 4)


#code in the main routine

if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("MathQuiz")
    root.mainloop()
