import sys, os, time
import tweepy
import tkinter as tk
from secret.private import consumer_key, consumer_secret, access_token, access_token_secret

try:
    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_token_secret
    )

    api = tweepy.API(auth)

except tweepy.TweepError:
    print('Error! Failed to get access token.')


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
