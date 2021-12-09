import yagmail
import os
import pandas

sender = 'sushruti.python@gmail.com'

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

df = pandas.read_csv('contacts.csv')

def generate_file(filename,content):
  with open(filename,'w') as file:
    file.write(str(content))

for index, row in df.iterrows():
  name=row['name']
  amount=row['amount']
  filename = name +".txt"
  reciever_email = row['email']

  generate_file(filename,amount)

  

  subject=['This is the subject']
  contents= [f"""
  hey {name} you have to pay {amount}. 
  Bill is attached!""",filename,]

  yag.send(to=reciever_email,subject=subject,contents=contents)
  print("EmailSent")
