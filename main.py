from tkinter import *
import pandas as pd
import random
import time



BACKGROUND_COLOR = "#B1DDC6"

try:
  data = pd.read_csv('words_to_learn.csv')
except:
  original_data = pd.read_csv('punjabi_words.csv')
  to_learn = original_data.to_dict(orient='records')
else:
  to_learn = data.to_dict(orient='records')


current_card = {}
def next_card():
  global current_card, flip_timer
  window.after_cancel(flip_timer)
  current_card = random.choice(to_learn)
  
  canvas.itemconfig(card_title,text='Punjabi',fill='black')
  canvas.itemconfig(card_text,text=current_card['Punjabi'],fill='black')
  canvas.itemconfig(card_background,image = card_front_img)
  flip_timer = window.after(3000,func=flip_card)



def flip_card():
  canvas.itemconfig(card_title,text='English',fill='white')
  canvas.itemconfig(card_text,text=current_card['English'],fill='white')
  canvas.itemconfig(card_background,image = card_back_img)


def is_known():
  to_learn.remove(current_card)
  data = pd.DataFrame(to_learn)
  data.to_csv('words_to_learn.csv',index=FALSE)
  next_card()


# ---------- UI SETUP ----------

window = Tk()
window.title('Flashcard App')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(height=526,width=800,bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file='card_front.png')
card_back_img = PhotoImage(file='card_back.png')
card_background = canvas.create_image(400,263,image=card_front_img)
card_title = canvas.create_text(400,150,text='Title',font=('Ariel',40,'italic'))
card_text = canvas.create_text(400,263,text='Word',font=('Ariel',60,'bold'))


canvas.config(highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


cross_image = PhotoImage(file='wrong.png')
unknown_button = Button(image=cross_image,highlightthickness=0,borderwidth=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file='right.png')
known_button = Button(image=check_image,highlightthickness=0,borderwidth=0,command=is_known)
known_button.grid(row=1,column=1)

next_card()
window.mainloop()

