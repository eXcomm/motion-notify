__author__ = 'adean'

import smtplib
from datetime import datetime

from objects import motion_event


class SmtpEmailNotifyAction:
    @staticmethod
    def doEventStartAction(config, motionEvent):
        msg = config.get('SmtpEmailNotifier', 'event_started_message')
        msg += '\n\n' + config.get('SmtpEmailNotifier', 'image_and_video_folder_link')
        SmtpEmailNotifyAction.sendEmail(config, motionEvent, msg)

    @staticmethod
    def doEventEndAction(config, motionEvent):
        msg = config.get('SmtpEmailNotifier', 'message')
        msg += '\n\n' + motionEvent.uploadUrl
        SmtpEmailNotifyAction.sendEmail(config, motionEvent, msg)

    @staticmethod
    def doAction(config, motionEvent):
        SmtpEmailNotifyAction.sendEmail(config, motionEvent, "")

    @staticmethod
    def sendEmail(config, motionEvent, msg):
        # SMTP account credentials
        username = config.get('SmtpEmailNotifier', 'user')
        password = config.get('SmtpEmailNotifier', 'password')
        from_name = config.get('SmtpEmailNotifier', 'name')
        sender = config.get('SmtpEmailNotifier', 'sender')

        # Recipient email address (could be same as from_addr)
        recipient = config.get('SmtpEmailNotifier', 'recipient')

        # Subject line for email
        subject = config.get('SmtpEmailNotifier', 'subject')

        senddate = datetime.strftime(datetime.now(), '%Y-%m-%d')
        m = "Date: %s\r\nFrom: %s <%s>\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n" % (
        senddate, from_name, sender, recipient, subject)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(sender, recipient, m + msg)
        server.quit()
