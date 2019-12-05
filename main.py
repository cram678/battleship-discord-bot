import discord
import replit
import os

from keep_alive import keep_alive




from ships import place_ship, destroyer
from board import playerI_defense
from board import playerII_defense



keep_alive()
client = discord.Client()
token =os.environ.get("DBS")
client.run(token)



def seperator(x):
  grid="\n".join(["".join(elem) for elem in x])
  return grid



@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
  if message.author != client.user:
    if message.content('\battle'): 
      await client.send_message(message.channel, "If you would like to play battle ship with"+message.author+"please type \battle1")
      #await client.send_message(message.private, message.author+"you are in")
      #playerI=message.author
      #await client.send_message(message.private, message.author+"please set up ur ships to do this first send the name of the ship you would like to place: carrier=6 spaces     x1       battleship=4 spaces    x1     submarines=3 spaces    x2     destroyer=2 spaces    x1 then in a new message send the coordinates you would like you're ship to start at example=7,3 then in a new message send the direction up, down, right, left here is your board: "+ playerI_defense)

@client.event
async def on_message(message):          
  if message.author != client.user:
    if message=="\battle1":
      await client.send_message(message.channel, "game starting "+playerI+" vs "+message.author)
      await client.send_message(message.private, message.author+"you are in")
      playerII=message.author
      await client.send_message(message.private, message.author+"please set up ur ships to do this first send the name of the ship you would like to place: carrier=6 spaces     x1       battleship=4 spaces    x1     submarines=3 spaces    x2     destroyer=2 spaces    x1 then in a new message send the coordinates you would like you're ship to start at example=7,3 then in a new message send the direction up, down, right, left")
Isubmarine=0
IIsubmarine=0
@client.event
async def on_message(message):          
  if message.author == playerI:
    if message == "destroyer":
      if Idestroyer==True:
        await client.send_message(message.private, message.author+"you have already placed this ship try again")
        return
      Idestroyer= True
      ship="destroyer"
    if message == "carrier":
      if Icarrier==True:
        await client.send_message(message.private, message.author+"you have already placed this ship try again")
        return
      Icarrier= True
      ship="carrier"
    if message == "battleship":
      if Ibattleship==True:
        await client.send_message(message.private, message.author+"you have already placed this ship try again")
        return
      Ibattleship= True
      ship="battleship"
    if message == "submarine":
      if Isubmarine==2:
        await client.send_message(message.private, message.author+"you have already placed this ship try again")
        return
      Isubmarine+=1
      ship="submarine"
    else:
      await client.send_message(message.private, message.author+"you have already used this ship or this is not a ship please try again or **die**")
@client.event
async def on_message(message):          
  if message.author == playerI:
    if message[1]==int:
      Ix=10
      if len(message)==6:
        Iy=10
      Iy=message[4]
    elif len(message)==5:
      if message[1]!= int:
        Iy=10
    else:
      Ix=message[0]
      Iy=message[3]

@client.event
async def on_message(message):          
  if message.author == playerI:
    direction=message



#place_ship(5,5,"right",destroyer,playerI_defense)
#print(seperator(playerI_defense))'''


