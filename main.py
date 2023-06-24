import nextcord
from nextcord import ChannelType, Embed, Interaction
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import re
with open('token.txt', 'r') as f:
    token = f.read()

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
client = nextcord.Client(intents=intents)
keyword = ['me ajuda', 'em ajuda', 'preciso de ajuda com', 'me dá um help', 'pra dar um help', 'socorro', 'me dar um help', 'me da um help']
langs = ['python', 'javascript', 'js', 'java', 'c#', 'csharp', 'c++', 'assembly', 'cobol', 'html', 'css','ruby', 'php', 'sql', 'rust', 'go', 'perl', 'dart', 'delphi','lua', 'swift', ' c ',]
linguagem = None

@bot.event
async def on_ready():
    print("Bot online!")

ids = {
    "python": 868255267257745428,
    'javascript': 868255311683801108,
    'js': 868255311683801108,
    'java': 868255357133258814,
    'go': 868255410329632789,
    'html': 868255678551187467,
    'css' : 868255678551187467,
    'php': 868255757982908467,
    'ruby': 868255807270178846,
    'sql': 868255869882744902,
    'perl': 868256077140095006,
    'dart': 904828645569355786,
    'rust': 904828645569355786,
    ' c ': 911329133362053210,
    'c++': 911329133362053210,
    'csharp': 994738761197949078,
    'c#': 994738761197949078,
    'delphi': 911329478574243890,
    'lua': 1068943358002733116,
    'cobol': 1075909042595180667,
    'assembly': 1075909080901759047,
    'swift': 86825622905359159
}

def find_api_key(code:str):
    '''It detects if are there any api key in the code strings'''

    '''If the keyword didnt work, lets try by the size of this'''
 
    strings = [i for i in code.split() if i.startswith(("'",'"',"'''"))]
    for string in strings:
            if len(string) > 20 and not ' ' in string and not ':' in string:
                return string
    return False



@bot.listen()
async def on_message(message:nextcord.Message):
    if '```' in message.content:
        leaked = find_api_key(message.content)
        if leaked != False and message.author.bot == False:
            await message.delete()
            embed = nextcord.Embed(title=f"Mensagem de {message.author.display_name}", description=f"Uma API KEY foi vazada na mensagem original")
            embed.set_thumbnail(url=message.author.avatar.url)
            censored = re.sub(pattern=leaked, repl='"******"', string=message.content)
            embed.add_field(name="Mensagem:", value=censored)
            try:
                await message.channel.send(embed=embed)
            except:
                await message.channel.send(f'Uma key foi vazada na mensagem original de {message.author.mention} \n {censored}')

@bot.listen()
async def on_message(message:nextcord.Message):
    '''It checks if a used used a bot command in a channel'''
    if message.author != bot.user:
        if (message.author.bot == True and message.channel.id not in [755830614170665012, 930185571219943464, 1091776861849276416]) or (message.content.startswith(';compile') and message.channel.id != 1067938880810131517 and message.channel.id not in ids.values()):
            await message.delete()

        


@bot.listen()
async def on_message(message: nextcord.Message):
    """
    Listens for messages and sends a specific help message to the user if a message contains a keyword and a programming language. 
    
    Args:
        message (nextcord.Message): The message to check for keywords and programming languages.

    Returns:
        None
    """
    global foi
    foi = False
    if message.channel.id == 755490391771316384 or message.channel.id == 1096918504634064949 or message.channel.id == 1097302040901844992 and message.author.id != 715325435185201283:
        for word in keyword:
            if foi == False:
                if word in message.content.lower():
                    foi = True
                    for lang in langs:
                        if lang in message.content.lower():
                            if lang == 'js':
                                linguagem_c = 'Javascript'
                            else:
                                linguagem_c = lang.capitalize()
                            #--------------------------------------
                            user = message.author
                            #--------------------------------------
                            if lang in ids:
                                channel_id = ids[lang]
                            else:
                                channel_id = None             
                            #--------------------------------------
                            if channel_id is not None:
                                await message.delete()
                                embed=nextcord.Embed(title=f"Buscando ajuda com {linguagem_c}?", description="Procure ajuda nos canais específicos.")
                                embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/k51Oof3dHMpdigW9kJFUQqUGb-PEzFcBipmpjyBINxk/%3Fsize%3D256/https/cdn.discordapp.com/icons/755483507698172045/a_37598d0798568f4f22860744fd5fc6ce.gif?width=192&height=192")
                                embed.add_field(name=f"Envie sua dúvida no canal <#{channel_id}>, e seja mais específico em sua dúvida.", value=f"Não tem acesso? Receba o cargo no canal <#931934867791425646>", inline=False)
                                embed.set_footer(text="Bot desenvolvido por Apenas_um_nerd#7866")
                                await user.send(embed=embed)
                    

bot.run(token)