#task 2
import smtplib #library for mail purpose
import random as np #library for generating random 6 digit otp

def sendOtp(user):
  server=smtplib.SMTP('smtp.gmail.com',587)
  server.starttls()
  server.login('senders mail','senders mail password')
  msg=str(np.randint(99999,1000000))
  server.sendmail('senders mail',user,msg)
  print('mail sent')
  return msg
  server.quit()

def verifyMail(otp,msg):
  print(msg)
  if(otp==msg):
    print("Verification sucessful...")
  else:
    print("Ohhh! sorry I guess you have entered wrong otp")

user=input("Please enter your email:")
msg=sendOtp(user)
otp=input("Please enter otp that you have received:")
verifyMail(otp,msg)
