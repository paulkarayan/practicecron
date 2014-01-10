import pywapi
import sendgrid
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

weather_com_result = pywapi.get_weather_from_weather_com('94080', units="imperial")
yahoo_result = pywapi.get_weather_from_yahoo('94080', units="imperial")

weathercomstr = string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] 
yahoostr = string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp']


# Your From email address
fromEmail = "info@paulkarayan.com"
# Recipient
toEmail = "yourname@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Weather from the White Rabbit"
msg['From'] = fromEmail
msg['To'] = toEmail

# Create the body of the message (a plain-text and an HTML version).
# text is your plain-text email
# html is your html version of the email
# if the reciever is able to view html emails then only the html
# email will be displayed
text = "Hi!\nHow are you?\n"


html = """\n
<html>
  <head></head>
  <body>
    Hi!<br>
       How are you?<p>

     Weather.com says: It is %s F now in South San Francisco. <p>

     Yahoo says: It is %s F now in South San Francisco. <p>
     
     smooches, <br>
    the white rabbit
  </body>
</html>
 """ % (weathercomstr, yahoostr)

# Login credentials - update them with your own!

username = ''
password = ""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
msg.attach(part1)
msg.attach(part2)

# Open a connection to the SendGrid mail server
s = smtplib.SMTP('smtp.sendgrid.net', 587)

# Authenticate
s.login(username, password)

# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(fromEmail, toEmail, msg.as_string())

s.quit()
