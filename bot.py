import datetime
import random
import json
import requests

import discord
import os
import asyncio
from discord import Spotify
from discord.ext import commands



bot = commands.Bot(command_prefix='/')

bot.remove_command('help')


@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print((bot.user.name) + '#' + (bot.user.discriminator))
    print(bot.user.id)
    print('------')
    

@bot.command(pass_context=True)
async def say(ctx, *, args):
    await ctx.message.delete(delay=0.5)
    return await ctx.send(args)

@bot.command(pass_context=True)



        


class Moderation(commands.Cog): 
    def __init__(self, bot):   
        self.bot = bot

bot.add_cog(Moderation(bot))        
class Action(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def pat(self, ctx, user: discord.Member= None):
        await ctx.message.delete(delay=0.5)
        random_number = random.randint(1 , 8)
        with open('pat.json') as f:
            imeg= json.load(f) 
            em= discord.Embed(title= '', description=(f"**✋{ctx.author.display_name} **Pats** {user.display_name}**"), color = (ctx.author.colour))
            em.set_image(url= (imeg[f'{random_number}']))
        await ctx.send(embed = em)
        
    @commands.command()
    async def kill(self, ctx, user: discord.Member= None):
        await ctx.message.delete(delay=0.5)
        random_number = random.randint(1 , 11)
        with open('kill.json') as f:
            imeg= json.load(f)
            em= discord.Embed(title= '', description=(f"** {ctx.author.display_name} **killed** {user.display_name}** R.I.P!"), color = (ctx.author.colour))
            em.set_image(url= (imeg[f'{random_number}']))
        await ctx.send(embed = em)
    
    @commands.command()
    async def poke(self, ctx, user: discord.Member= None):
        await ctx.message.delete(delay=0.5)
        
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "poke"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**✋{ctx.author.display_name} **poked** {user.display_name}**"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)
        
    @commands.command()
    async def stink(self, ctx, user: discord.Member= None):
        await ctx.message.delete(delay=0.5)
        
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "stink"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**{user.display_name}** stinks!! Ewww"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)
        
    @commands.command()
    async def hug(self, ctx, user: discord.Member= None):
        await ctx.message.delete(delay=0.5)
        
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "anime couple hug"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**🤗🤗{ctx.author.display_name} **hugged** {user.display_name}**"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)
        
        
    
    @commands.command()
    async def slap(self, ctx, user: discord.Member= None):
        await ctx.message.delete(delay=0.5)
       
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "slap"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**👊{ctx.author.display_name} **slapped** {user.display_name}**"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)
        
    @commands.command()
    async def cry(self, ctx, user: discord.Member= None):
        await ctx.message.delete(delay=0.5)
        
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "cry"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**😢😢 {ctx.author.display_name}** cries "), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)
             
    
    @commands.command()
    async def smile(self, ctx, user: discord.Member= None):
        await ctx.message.delete(delay=0.5)
        
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "smile"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**😊😊 {ctx.author.display_name}** smiles "), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)
        
    @commands.command()
    async def bully(self, ctx, user: discord.Member= None):
        await ctx.message.delete(delay=0.5)
        
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "bully"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**👿👿 {ctx.author.display_name} **bullies** {user.display_name}**"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)
        
    
    @commands.command()
    async def stare(self, ctx, user: discord.Member= None):
        await ctx.message.delete(delay=0.5)
        
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "stare"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"** {ctx.author.display_name} **stares at** {user.display_name}**"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)
        
        
    @commands.command()
    async def punch(self, ctx, user: discord.Member= None):
        await ctx.message.delete(delay=0.5)
       
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "punch"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**👊👊{ctx.author.display_name} **punched** {user.display_name}**"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)
    
    @commands.command()
    async def kiss(self, ctx, user: discord.Member= None):
        await ctx.message.delete(delay=0.5)
        
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "sweet kiss"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**💋{ctx.author.display_name} **kissed** {user.display_name}**"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)

    @commands.command()
    async def cuddle(self, ctx, user: discord.Member= None):
        await ctx.message.delete(delay=0.5)
        
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "cuddle hug"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**✋{ctx.author.display_name} **cuddled** {user.display_name}**"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)

    @commands.command()
    async def angry(self, ctx, user: discord.Member= None):
        await ctx.message.delete(delay=0.5)
        
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "angry"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**😠{ctx.author.display_name}** pissed off"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)

    @commands.command()
    async def drink(self, ctx, user: discord.Member= None):
        await ctx.message.delete(delay=0.5)
        """"""
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "drinking"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**✋{ctx.author.display_name}** drinks"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)
 

bot.add_cog(Action(bot))

@bot.command(pass_context=True)
async def lyrics(ctx,*, lyrics_name):
    lyrics_url = f"https://api.ksoft.si/lyrics/search?q={lyrics_name}&limit=1"
    r =requests.get(lyrics_url, headers={"Authorization":(os.getenv('ksoft_key'))})
    response_json= json.loads(r.text)
    text= response_json['data'][0]['lyrics']
    artist= response_json['data'][0]['artist']
    name_song= response_json['data'][0]['name']
    art= response_json['data'][0]['album_art']

    len_text= len(text)
    if len_text>2048:
        s= text[:2047]
        s1=text[2048:4095]
        em= discord.Embed(title=f'{artist} - {name_song}', description= (s), color= 0xd8a903)
        em.set_thumbnail(url= (art))
        em1= discord.Embed(title= '', description=(s1), color=0xd8a903)
        await ctx.send(embed= em)
        await ctx.send(embed= em1)

    elif len_text<2047:
        em= discord.Embed(title=f'{artist} - {name_song}', description= (text), color= 0xd8a903)
        em.set_thumbnail(url= (art))
        await ctx.send(embed= em)

#CFG PC
import platform
import psutil
import cpuinfo
from cpuinfo import get_cpu_info

#CPU
cpu_count= psutil.cpu_count()
cpu_name= get_cpu_info()['brand']

@bot.command()
async def infosys(ctx):


#RAM
    totalmem= psutil.virtual_memory().total //1024//1024
    used= psutil.virtual_memory().used  //1024//1024
    freemem= psutil.virtual_memory().available //1024//1024

#OS

    nOS= platform.uname().system
    vOS= platform.uname().release

    em1= discord.Embed(title= (bot.user.display_name), color=(bot.user.colour))
    em1.add_field(name= "CPU", value= f"> {cpu_name}[{cpu_count}х Héx]",inline= False)    
    em1.add_field(name= "RAM(Total / Free / Busy)", value= f"> {totalmem}mb/{freemem}mb/{used}mb", inline= False)
    em1.add_field(name= "OS", value=f"> {nOS} {vOS}")
    em1.add_field(name= "Version Python", value= f"> {platform.python_version()}", inline= True)
    await ctx.send(embed= em1)

        
bot.run(os.getenv('TOKEN'))
