import sys, os, time
import tweepy
import tkinter as tk

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()

except tweepy.TweepError:
    print('Error! Failed to get request token.')

session.set('request_token', auth.request_token['oauth_token'])

# Example w/o callback (desktop)
verifier = raw_input('Verifier:')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
token = session.get('request_token')
session.delete('request_token')
auth.request_token = { 'oauth_token' : token,
                         'oauth_token_secret' : verifier }

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print('Error! Failed to get access token.')


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
