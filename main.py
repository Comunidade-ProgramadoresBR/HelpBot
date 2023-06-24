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

