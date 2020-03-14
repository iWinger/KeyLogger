# KeyLogger

## Objective:
An efficient keylogger that tracks every interesting (alphanumerical) key typed and sends an email periodically using SMTP email library with MIME (Multipurpose Internet Mail Extensions).
In addition to being able to track what is being typed, it also takes a periodic snapshot from time to time, and also 
sends an email accordingly. **This project is intended for security purposes, so what you might do with this project is your own responsibility.**

### Build:
To make this project an executable, I recommend using the command *pyinstaller -F key_logger_driver.pyw* in order to run it in the background.
This will make a standalone executable that will have the correct DLL's in place when running. 
**Important**: Uncomment the line and change the sender_email, sender_password, and receiver_email to your appropiate information in order to run
the key_logger_driver.pyw file.


#### Example:
![KeyloggingText](https://user-images.githubusercontent.com/33408526/76672060-947a3180-6570-11ea-9190-0932a48129ba.png)

![KeyLoggingPicture](https://user-images.githubusercontent.com/33408526/76672063-99d77c00-6570-11ea-9906-e024d9b2bd99.png)

