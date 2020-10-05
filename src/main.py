import discord
from discord.message import MessageType
import os.path
# Importing libraries 
import imaplib, email 
from imap_tools import MailBox
  
user = 'eadbotifsp@gmail.com'
password = 'ifsp1918'
imap_url = 'imap.gmail.com'  
 
con = imaplib.IMAP4_SSL(imap_url)    
con.login(user, password)    
con.select('Inbox')    

typ, data = con.select('INBOX')
num_msgs = int(data[0]) - 1
#print ('Existem %d e-mails na INBOX' % num_msgs)

with MailBox('imap.gmail.com').login('eadbotifsp@gmail.com', 'ifsp1918', 'INBOX') as mailbox:
    subject = [msg.subject for msg in mailbox.fetch()] 
    sender = [msg.from_ for msg in mailbox.fetch()]  
    bodies = [msg.text for msg in mailbox.fetch()]   

client = discord.Client()

@client.event
async def on_ready():
    print('Logado como :')
    print(client.user.name)
    print(client.user.id)
    print('------------------')

@client.event
async def on_message(message):

     if ".total" in message.content:
           #await Bot.send_message(message.channel, 'yes')
        print("Total")
        channel = message.channel
        await channel.send(content=str('Existem %d e-mails na INBOX' % num_msgs))

     elif ".listar" in message.content:
        print("Lista")
        channel = message.channel
        await channel.send(content=str("De:" + " " + sender[num_msgs]))
        await channel.send(content=str("Assunto:" +  " " + subject[num_msgs]))
        await channel.send(content=str("Texto:"+ " " + bodies[num_msgs]))       

client.run('NzYxMTE1ODM3NzA4MzY5OTUw.X3V6XA.V05UNnzCLRoPpPEitGMad3qk-bk')

