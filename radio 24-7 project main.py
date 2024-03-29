from tkinter import *  # import all library tkinter
import pyttsx3
import tkinter.messagebox as mbox  # import yes or no first connect canvas
import tkinter as tk  # just shortcust
import webbrowser
root = Tk()
root.geometry("750x530")
background_image = tk.PhotoImage(file='mashroomsme2.png')
background_lable = tk.Label(root, image=background_image)
background_lable.place(relwidth=1, relheight=1)
engine = pyttsx3.init()
engine.say("choose a mode?")
engine.runAndWait()
answer = tk.messagebox.OK
def talk (url):
    engine = pyttsx3.init()
    engine.runAndWait()
    if answer == 'yes':
        engine.say("sorry, until this function not ready. we are working on it")
        engine.runAndWait()
    else:
        answer == 'no'
        engine.say("Great, enjoy")
        engine.runAndWait()
        webbrowser.open(url)
genres = {'Vintage radio': "https://www.youtube.com/watch?v=kxf5P0ejS9s",
          'Electronic': "https://www.youtube.com/watch?v=thd6h-ZZIfo",
          'dance music': 'https://www.youtube.com/watch?v=ARbjFgb-URw',
          'Hip-hop': 'https://www.youtube.com/watch?v=L9Q1HUdUMp0',
          'Indie': 'https://www.youtube.com/watch?v=qi3Hfy8waFo',
          'rock': 'https://www.youtube.com/watch?v=OPYwHUYjQWc',
          'Jazz': 'https://www.youtube.com/watch?v=Dx5qFachd3A',
          'blues': 'https://www.youtube.com/watch?v=pT9RPH-ga9w',
          'Metal': 'https://www.youtube.com/watch?v=dGfdGZ8cH-o',
          'Fallout Radio': 'https://www.youtube.com/watch?v=Ya3WXzEBL1E',
          'reggae': 'https://www.youtube.com/watch?v=jBLapoJrkf8',
          'Rap': 'https://www.youtube.com/watch?v=05689ErDUdM',
          'Minimal_Techno': 'https://www.youtube.com/watch?v=n0Zli_fQeP8',
          'drum&bass': 'https://www.youtube.com/watch?v=xevHCoYIXus',
          'Trance' : 'https://www.youtube.com/watch?v=839IFrk-Xig' ,
          'telegram MetalBot':'https://t.me/NewsMetaLutzi',
          'donate': 'https://www.paypal.com/donate?hosted_button_id=Q7JBNHULDUQ74',
          'fallout radio' : 'https://www.youtube.com/watch?v=tzBGEqkwCoY'}
key , val = next(iter(genres.items()))
bg1 = "lime green"
bg2 = 'Antique white'
bg3 =  'pink'
f1 = ('Arial', 12)
v = tk.StringVar()  # keep changes of variables over time
mb = Button(root, text='Would you like your Vibes \n from the following genres?',
            font=('Arial', 18), bg='chocolate').grid(row=0, column=1)
b1 = Radiobutton(root, variable=v, value=genres.get("Vintage"), text='1. Vintage radio', font=f1, bg=bg1,command=lambda aurl=genres.get('Vintage radio'): talk(aurl)).grid(row=2, column=0, sticky=W)
b2 = Radiobutton(root, variable=v, value=genres.get("Electronic"), text='2. Electric Music', font=f1, bg=bg1, command=lambda aurl=genres.get('Electronic'): talk(aurl)).grid(row=3, column=0, sticky=W)
b3 = Radiobutton(root, variable=v, value=genres.get('Dance Music'), text='3. Dance Music', font=f1, bg=bg1, command=lambda aurl=genres.get('dance music'): talk(aurl)).grid(row=4, column=0, sticky=W)
b4 = Radiobutton(root, variable=v, value=genres.get('Hip-Hop'), text='4. Hip-Hop', font=f1, bg=bg1, command=lambda aurl=genres.get('Hip-hop'): talk(aurl)).grid(row=5, column=0, sticky=W)
b5 = Radiobutton(root, variable=v, value=genres.get('Indie'), text='5.Indie', font=f1, bg=bg1, command=lambda aurl=genres.get('Indie'): talk(aurl)).grid(row=6, column=0, sticky=W)
b6 = Radiobutton(root, variable=v, value=genres.get('Classic Rock'), text='6. Rock and Roll', font=f1, bg=bg1, command=lambda aurl=genres.get('rock'): talk(aurl)).grid(row=7, column=0, sticky=W)
b7 = Radiobutton(root, variable=v, value=genres.get('Jazz'), text='7.Jazz', font=f1, bg=bg1, command=lambda aurl=genres.get('Jazz'): talk(aurl)).grid(row=8, column=0, sticky=W)
b8 = Radiobutton(root, variable=v, value=genres.get('blues'), text='8. blues', font=f1, bg=bg1, command=lambda aurl=genres.get('blues'): talk(aurl)).grid(row=9, column=0, sticky=W)
b9 = Radiobutton(root, variable=v, value=genres.get('Metal'), text='9. Metal', font=f1, bg=bg1, command=lambda aurl=genres.get('Metal'): talk(aurl)).grid(row=10, column=0, sticky=W)
b10 = Radiobutton(root, variable=v, value=genres.get('Fallout Radio'), text='10. Fallout Radio', font=f1, bg=bg1, command=lambda aurl=genres.get('Fallout Radio'): talk(aurl)).grid(row=11, column=0, sticky=W)
b11 = Radiobutton(root, variable=v, value=genres.get('Reggae'), text='11. Reggae', font=f1, bg=bg1, command = lambda aurl=genres.get('reggae'): talk(aurl)).grid(row=12, column=0, sticky=W)
b12 = Radiobutton(root, variable=v, value=genres.get('Rap'), text='12. Rap', font=f1, bg=bg1,command = lambda aurl=genres.get('Rap'): talk(aurl)).grid(row=13, column=0, sticky=W)
b13 = Radiobutton(root, variable=v, value=genres.get('Minimal Techno'), text='13. Minimal Techno', font=f1, bg=bg1, command=lambda aurl=genres.get('Minimal_Techno'): talk(aurl)).grid(row=14, column=0, sticky=W)
b14 = Radiobutton(root, variable=v, value=genres.get('Drum and Bass'), text='14. Drum and Bass', font=f1, bg=bg1, command=lambda aurl=genres.get('drum&bass'): talk(aurl)).grid(row=15, column=0, sticky=W)
b15 = Radiobutton(root, variable=v, value=genres.get('Trance'), text='14. Trance-Goa+Dark+Psy', font=f1, bg=bg1, command=lambda aurl=genres.get('Trance'): talk(aurl)).grid(row=16, column=0, sticky=W)
b16 = Radiobutton(root, variable=v, value=genres.get('telegram MetalBot'), text='16. telegram-Metal-Bot~~Daily-News~~', font=f1, bg=bg3, command=lambda aurl=genres.get('telegram MetalBot'): talk(aurl)).grid(row=14, column=1, sticky=W)
b17 = Radiobutton(root, variable=v, value=genres.get('donate'), text='donate to support us~~PAYPAL', font=f1, bg=bg2, command=lambda aurl=genres.get('donate'): talk(aurl)).grid(row=15, column=1, sticky=W)
b18 = Radiobutton(root, variable=v, value=genres.get('fallout radio'), text='fallout radio 24/7', font=f1, bg=bg2, command=lambda aurl=genres.get('fallout radio'): talk(aurl)).grid(row=16, column=1, sticky=W)
root.mainloop()
