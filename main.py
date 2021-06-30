import discord
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.lower() == 'yes':
        await message.channel.send('uploading the data to website')
        msg_history = await  message.channel.history(limit=10).flatten()

        list_gen=[]
        for msg in msg_history:
            if msg.attachments:
                list_gen.append(msg.attachments[0].url)
            else:
                list_gen.append(msg.content)

        start_index=list_gen[2:].index('uploading the data to website')
        print(list_gen[2:start_index+2])

    if message.content.lower() == 'clear':
        await message.channel.send('uploading the data to website')

client.run('DISCORD_KEY')




