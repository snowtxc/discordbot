import discord 
import asyncio
import mysql.connector
from mysql.connector import Error
import random
from discord.ext import commands




print("llega")

client = commands.Bot(command_prefix = '.')

@client.command()

async def ping(ctx):
    await ctx.send('pong')






@client.command()
async def kick(ctx,member : discord.Member ,*,reason=None):
    await member.kick_members(reason=reason)





@client.event
async def on_message(message):   #Función que esta a la escucha de un mensaje enviado por cualquier usuario#
    if message.author == client.user:
        return

    if  message.content.startswith('hola') or message.content.startswith('Hola'):
        channel = message.channel
        await channel.send('Hola soy el bot toxiano')
        await asyncio.sleep(1)


        await channel.send('A las ordenes')


    if  message.content.startswith('Bien y vos?'):

        channel = message.channel
        await channel.send('Bien ,comiendo sanguchitos')
        await asyncio.sleep(1)
        await channel.send('Todo tranqui?')



    if  message.content.startswith('zoco'):
        channel = message.channel
        await channel.send('cabrita')


    if  message.content.startswith('!tx imagen'):
       
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='discord_boy',
                                                 user='root',
                                                 password='')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(file) from imagenes;")

                result = cursor.fetchone();



                contador = result[0]





                randome = random.randint(1,contador)

                SQL= "SELECT file from imagenes WHERE id='"+str(randome)+"'"

                cursor.execute(SQL)

                query = cursor.fetchone();
                

                
                ruta = 'images/'+query[0]

               

                channel = message.channel

                with open(ruta , 'rb') as f:
                
                   await channel.send(file=discord.File(f))




        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")





            

    if  message.content.startswith('ban'):
        channel = message.channel
        await channel.send('cabrita')


@client.event
async def on_ready():
    print('login in as')
    print(client.user.name)
    print(client.user.id)
    print('==========')



@client.event
async def on_member_join(member):
    await member.create_dm()  #Crea un DM con el usuario ,es decir que puede interactuar con el en privado#
    await member.dm_channel.send(       #usa la funcion de enviar atravez de el DM channel después de averlo creado#
        f' Bienvenido a el clan Toxic {member.name} ,Espero que sobretodo te diviertas! !'
    )

client.run('NjY1NzE2OTA3NjE3NTUwMzM2.XvQMJg.9Zb_9oaHF1dYotO2YyWaNVgnB3U')    
