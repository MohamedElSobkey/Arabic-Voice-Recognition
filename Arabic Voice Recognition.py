import speech_recognition
import arabic_reshaper
from bidi.algorithm import get_display
from tkinter import *
from tkinter import font

#to define tkinter
root = Tk()
#to set the size of the window
root.geometry("500x300")
root.title("التعرف على الكلام")

#to open the mic and record the voice
def voiceReco():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)
        text = recognizer.recognize_google(audio, language='ar-AR')
        reshaped_text = arabic_reshaper.reshape(text)
        #to modify the text
        bidi_text = get_display(reshaped_text)
        print(bidi_text)
        # to delete any text before
        textF.delete("1.0", "end")
        #to insert the modify text
        textF.insert(END, bidi_text)
        #to show our text in the center
        textF.tag_add("center", 1.0, "end")





# to set the font 
ButtonFont = font.Font(size=20)
LabelFont = font.Font(size=15)

#to put the label in the window
Label(root, text="النص المسجل سوف يظهر هنا", font=LabelFont).pack()


#to create text lable
textF = Text(root, height=5, width=52, font=LabelFont)
#to show the text in the center
textF.tag_configure("center", justify='center')
textF.pack()

# to make a button to record the voice
Button(root, text='استمع', font=ButtonFont, command=voiceReco).place(x=220, y=200)



#to let the window open
root.mainloop()