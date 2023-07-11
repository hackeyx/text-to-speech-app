import tkinter as tk
import pyttsx3
from tkinter import filedialog, ttk
from tkinter import *
# used for tab2
import PyPDF3
from PyPDF3 import PdfFileReader
import os
window = tk.Tk()
my_notebook = ttk.Notebook(window)
window.geometry("400x400")
window.title("Text2Speech")
window.configure(bg="#252525")
window.resizable(True, True)

tab1 = Frame(my_notebook, width=400, height=400, bg='#252525')
tab2 = Frame(my_notebook, width=400, height=400, bg='#252525')
tab3 = Frame(my_notebook, width=400, height=400, bg='#252525')
tab4 = Frame(my_notebook, width=400, height=400, bg='#252525')

my_notebook.pack(fill="both", expand=1)
my_notebook.pack(fill="both", expand=1)
my_notebook.pack(fill="both", expand=1)
my_notebook.pack(fill="both", expand=1)

my_notebook.add(tab1, text="INSTRUCTIONS")
my_notebook.add(tab2, text="Read Text") #use to be 1
my_notebook.add(tab3, text="Read PDF") # use to be 2
my_notebook.add(tab4, text="About") # use to be 3



def speck():
    global engine
    global filename
    filename = filedialog.asksaveasfile(initialfile='Untitled.wav', title='Save File',
                                        defaultextension='.wav',
                                        filetypes=(('Audio File', '.wav'), ("Text file", ".txt"), ('all Files', '*.*')))
    if filename is None:
        return
    result = str(label_entry.get("1.0", "end-1c"))
    gend_result = gender_entry.get()
    if gend_result == "Joseph".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()

    elif gend_result == "Samad".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gend_result == "DanAnny".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[7].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gend_result == "Michael".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[4].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gend_result == "Goriola".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[6].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gend_result == "Helena".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gend_result == "Caroline".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[5].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gend_result == "Linda".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[9].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gend_result == "Zira".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[10].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gend_result == "Victory".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[8].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gend_result == "papa".lower() or gend_result == "old man".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[3].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()

# tab1
label = tk.Label(tab1, text="Text2Speech Instructions", font=("Roman", 12))
label.configure(fg="white", bg="#252525")
label.pack(padx=40, pady=40)

label = tk.Label(tab1, text="1. So the audio file made will be save in the same"
                            "folder in which the app was downloaded in.\n"
                            "\n"
                            "\n"
                            "2. There are 10 voices of 5 different forms of languages on this app and by"
                            "to activate the languages put in the name of the voice."
                            "\n"
                            "\n"
                            "Samad (Male English)\n"
                            "\n"
                            "Joseph (Male English)\n"
                            "\n"
                            "Zira (Female English)\n"
                            "\n"
                            "Linda (Female canadian English)\n"
                            "\n"
                            "Victory (Female UK English)\n"
                            "\n"
                            "Caroline (Female French)\n"
                            "\n"
                            "Helena (Female Spanish)\n"
                            "\n"
                            "Michael (Male Spanish)\n"
                            "\n"
                            "Goriola (Female Japanese)\n"
                            "\n"
                            "DanAnny (Japanese)\n"
                            "\n", font=("Arial", 12))
label.configure(fg="white", bg="#252525")
label.pack(padx=40, pady=10)



# tab2
# Add text for header field
label = tk.Label(tab2, text="Text2Speech", font=("Roman", 12))
label.configure(fg="white", bg="#252525")
label.pack(padx=40, pady=40)

# input fields for text
text_label = tk.Label(tab2, text="Type Text: ", font=("Roman", 12))
text_label.configure(fg="white", bg="#252525")
text_label.place(x=600, y=80)

label_entry = tk.Text(tab2, height=5, width=30, font="Arial 12")
label_entry.place(x=600, y=110)

# input field for male or female
gender_label = tk.Label(tab2, text="Voice Name: ", font=("Roman", 12))
gender_label.configure(fg="white", bg="#252525")
gender_label.place(x=600, y=250)

gender_entry = tk.Entry(tab2, font="Arial 14")
gender_entry.place(x=600, y=290)

button = tk.Button(tab2, text="Convert", height=1, width=20, borderwidth=0, font=("Roman", 18),
                   command=speck)
button.configure(fg="black", bg="white")
button.place(x=600, y=330)


# tab3

# read file as rb mode

def nice():
    global file
    gender_result = gend_entry.get()

    file = filedialog.askopenfilename(title='Select File',
                                           defaultextension='.pdf',
                                           filetypes=(('pdf Files', '*.pdf'), ('all Files', '*.*')))

    with open(file, "rb") as f:
        pdfReader = PyPDF3.PdfFileReader(f)
        pageObj = pdfReader.getPage(0)
        fresult = pageObj.extractText()

        convertion = str(fresult)
        engine = pyttsx3.init()
        engine.say(convertion)
        engine.runAndWait()
        filename = filedialog.asksaveasfile(initialfile='Untitled.wav', title='Save File',
                                            defaultextension='.wav',
                                            filetypes=(
                                            ('Audio File', '.wav'), ("Text file", ".txt"), ('all Files', '*.*')))
        if filename is None:
            return
    if gender_result == "Joseph".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(convertion, filename.name.split("/")[-1])
        engine.runAndWait()

    elif gender_result == "samad".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(convertion, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gender_result == "DanAnny".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[7].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gender_result == "Michael".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[4].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gender_result == "Goriola".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[6].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gender_result == "Helena".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gender_result == "Victory".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[8].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gender_result == "Linda".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[9].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gender_result == "Zira".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[10].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gender_result == "papa".lower() or gender_result == "old man".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[3].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()
    elif gender_result == "Caroline".lower():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[5].id)  # changing index changes voices but ony 0 and 1 are working here
        engine.say(label_entry.get("1.0", "end-1c"))
        mad = str(label_entry.get("1.0", "end-1c"))
        engine.save_to_file(mad, filename.name.split("/")[-1])
        engine.runAndWait()




nice_label = tk.Label(tab3,
                      text="Click start to select a file from your computer, so the software can read it to you and you can save it",
                      font=("Italic", 15))
nice_label.configure(fg="white", bg="#252525")
nice_label.place(x=200, y=100)
gend_label = tk.Label(tab3, text="Voice Name: ", font=("Roman", 12))
gend_label.configure(fg="white", bg="#252525")
gend_label.place(x=600, y=200)

gend_entry = tk.Entry(tab3, font="Arial 14")
gend_entry.place(x=600, y=250)

buttonEnd = tk.Button(tab3, text="START", width=15, height=5, borderwidth=3, font=("Roman", 18),
                      command=nice)
buttonEnd.configure(bg="white", fg="black")
buttonEnd.place(x=600, y=300)

# tab4
thrid_label = tk.Label(tab4, text="This is a Text To Speech Desktop Application in which text can be\n"
                                  " inputted and can convert it to audio of male or female voices and it can read\n"
                                  "out a PDF in 'Read PDF' section for you in which ever voice you type down in your  "
                                  "\n"
                                  "'Read PDF' section and it can also be saved. It was made in 2023 \n"
                                  " of july by salami samad (twitter- @salamisamad5).\n"
                                  "if you want to check another desktop application i've worked on search for dissect\n"
                                  "on microsoft store"
                       , font=("Bold", 20))
thrid_label.configure(fg="white", bg="#252525")
thrid_label.place(x=220, y=100)
fourth_label = tk.Label(tab4, text="So as always, Enjoy ;)"
                        , font=("Roman", 15))
fourth_label.configure(fg="white", bg="#252525")
fourth_label.place(x=350, y=325)
window.mainloop()
# The reason there is a roman font in every tab is a tribute to the past romans and the way they
# have advanced science and arts for us. it shows they are always around. so this app was released on
# july 20 on Ludi Victoriae Caesarae. Enjoy the ludus.
