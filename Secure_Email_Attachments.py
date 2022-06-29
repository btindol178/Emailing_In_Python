from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import io
import pandas as pd
import numpy as np

data = np.random.randint(5,30,size=(10,3))
df = pd.DataFrame(data, columns=['random_numbers_1', 'random_numbers_2', 'random_numbers_3'])

print(df)

def export_csv(df):
  with io.StringIO() as buffer:
    df.to_csv(buffer)
    return buffer.getvalue()
#   
# def export_excel(df):
#   with io.BytesIO() as buffer:
#     with pd.ExcelWriter(buffer) as writer:
#         df.to_excel(writer)
#     return buffer.getvalue()
#   
# #EXPORTERS = {'dataframe.csv': export_csv, 'dataframe.xlsx': export_excel}

EXPORTERS = {'dataframe.csv': export_csv}

def send_dataframe(send_to, subject, body, df):
  multipart = MIMEMultipart()
  multipart['From'] = "*******@stryker.com"
  multipart['To'] = send_to
  multipart['Subject'] = subject
  for filename in EXPORTERS:    
    attachment = MIMEApplication(EXPORTERS[filename](df))
    attachment['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
    multipart.attach(attachment)
  multipart.attach(MIMEText(body, 'html'))
  s = smtplib.SMTP('*******.strykercorp.com')
  s.sendmail("*******@stryker.com", send_to, multipart.as_string())
  s.quit()
  
send_dataframe("*******.*******@stryker.com","Test email","This is a test email check out the file!",df)



def emailmessage(subject,reciever):
    msg = MIMEMultipart() 
    msg['From'] = "*******@stryker.com"  
    msg['To'] = reciever
    msg['Subject'] = "Compliance Action Items"
    msg.attach(MIMEText(subject, 'plain')) 
    print("message",msg)
    s = smtplib.SMTP('*******.strykercorp.com') 
    text = msg.as_string() 
    s.sendmail("*******@stryker.com", reciever, text) 
    s.quit()
    return print("Done")
