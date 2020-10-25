import sys, os, time
import tweepy
import tkinter as tk
from secret import private as p


user = p.user_name

auth = tweepy.OAuthHandler(p.consumer_key, p.consumer_secret)
auth.set_access_token(p.access_token, p.access_token_secret)
api = tweepy.API(auth)

def tweet(msg):
        api.update_status(msg)
        textBox.delete(1.0, tk.END)
        textBox.insert(tk.END, "Tweet Sent!")


def getText():
    text = textBox.get("1.0","end-1c")
    tweet(text)

window = tk.Tk()
window.title('Twitter for Neurolinker')
window.geometry('500x110')
window.configure(background='black')
window.resizable(False, False)

#Text fields
textBox = tk.Text(window, height = 5, width = 100)
textBox.configure(background='black', foreground='white')
textBox.pack()

#Button
sendButton = tk.Button(window, height = 1, width = 10, text = "Tweet",
 command=lambda: getText())
sendButton.configure(background='black', foreground='white')
sendButton.pack()

tk.mainloop()
