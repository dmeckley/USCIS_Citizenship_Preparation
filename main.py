from tkinter import *
from uscis import USCIS


def main():

    uscis = USCIS()

    window = Tk()
    window.title("USCIS Citizenship Preparation")
    window.geometry("750x125")

    topFrame = Frame(window)
    bottomFrame = Frame(window)

    welcomeLabel = Label(topFrame, text="Welcome to the USCIS Preparation Program", bg="black", fg="yellow")
    welcomeLabel.pack()

    value = IntVar()
    value.set(0)

    studyRadioButton = Radiobutton(bottomFrame, text="Study", variable=value, value=1, command=uscis.study)
    studyRadioButton.pack()
    practiceRadioButton = Radiobutton(bottomFrame, text="Practice", variable=value, value=2, command=uscis.practice)
    practiceRadioButton.pack()
    quitRadioButton = Radiobutton(bottomFrame, text="Exit", variable=value, value=3, command=window.destroy)
    quitRadioButton.pack()

    topFrame.pack()
    bottomFrame.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
    print("Exiting USCIS...")