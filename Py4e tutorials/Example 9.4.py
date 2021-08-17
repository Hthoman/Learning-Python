name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emails=list()
emailcount={}

for line in handle:
    if not line.startswith('From '): continue
    words=line.split()
    email=words[1]
    emails.append(email)

for email in emails:
    emailcount[email]= emailcount.get(email, 0) +1

big_email_number=None
big_emailer=None

for emailer,count in emailcount.items():
    if count==max(emailcount.values()):
        print(emailer,count)


        





    



