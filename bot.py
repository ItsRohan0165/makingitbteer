import datetime
import random
import json
import requests

import discord
import os
import asyncio
from discord import Spotify
from discord.ext import commands



bot = commands.Bot(command_prefix=';')


@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print((bot.user.name) + '#' + (bot.user.discriminator))
    print(bot.user.id)
    print('------')


@bot.command(pass_context=True, aliases=['clean', 'c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit: int):
    await ctx.message.delete(delay=None)
    await ctx.channel.purge(limit=limit)
    
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❗❗❗Ты не можешь этого сделать!")

@bot.command()
async def avatar(ctx, user: discord.Member=None):
    user= user or ctx.author 
    qe = discord.Embed(title=(f"@{user.display_name}"), color=(user.color))
    qe.set_image(url=(user.avatar_url_as(format=None, static_format='png', size=2048)))
    await ctx.send(embed=qe)

@bot.command(pass_context=True)
async def say(ctx, *args):
    mesg= ''.join(args)
    await ctx.message.delete(delay=None)
    return await ctx.send(mesg)


@bot.command()
async def status(ctx, user: discord.Member=None):
    user= user or ctx.author
    check= user.activity.name
    if check == 'Spotify':
        time = user.activity.duration
        minutess = str(datetime.timedelta(seconds= time.seconds))
        em= discord.Embed(title= (user.display_name), description= (f"__Тип__: **{user.activity.name}**\n __Название__: **{user.activity.title}**\n __Исполнитель__: **{user.activity.artist}**\n __Альбом__: **{user.activity.album}**\n__Длительность__: **{minutess}**"), color= (user.activity.color))
        em.set_thumbnail(url=(user.activity.album_cover_url))
        await ctx.send(embed= em)
        pass
        
    else:
        em1= discord.Embed(title= (user.name), description=(f"__Название__: **{user.activity.name}**\n__Детали__: **{user.activity.details}**\n__Время__: **{user.activity.start}**\n__Время 2__: **{user.activity.timestamps}**"))
        em1.set_thumbnail(url=(user.activity.large_image_url))    
    await ctx.send(embed= em1)
    
@bot.command()
async def userinfo(ctx, user: discord.Member= None):
    user = user or ctx.author
    color= user.colour
    #tag = user.tag
    avatarurl= user.avatar_url_as(format=None, static_format='png', size=2048)
    #join_server = user.joined_at
    game_status = user.activity.name
    #roles_list = user.roles
    #acc_create = user.created_at
    accID= user.id
    statusdisc= user.status
    
    em=discord.Embed(title = f"Info **{user.name}**",description=(f"**ID**: {accID}\n**Status**: {statusdisc}\n**•{game_status}**\n"), color= (color))
    em.set_thumbnail(url= avatarurl)
    await ctx.send(embed= em)


@bot.command(pass_context=True)
async def weather(ctx, *, city):
    key= (str(os.getenv('weather')))
    url= f"http://api.apixu.com/v1/current.json?key={key}&q={city}"
    r = requests.get(url)
    response_json = r.json()
    
    
    try:
            location_name= json.loads(r.text)['location']['name']
    except KeyError:
            await ctx.send("Введи нормальный запрос блеять")
            return

    else:
        location_region= response_json['location']['region']
        location_name= response_json['location']['name']
        current_condition_icon= response_json ['current']['condition']['icon']   
        location_localtime= response_json['location']['localtime']
        current_last_updated= response_json['current']['last_updated']
        current_temp_c= response_json['current']['temp_c']  
        current_humidity= response_json['current']['humidity']
        current_wind_kph= response_json['current']['wind_kph']

        c_w_k= current_wind_kph*1000 
        c_w_k1= c_w_k//3600

        em1= discord.Embed(title= "**Weather**") 
        em1.set_footer(text= f"Последнее обновление: {current_last_updated}")
        em1.add_field(name= "🌇Город/Регион", value= f"{location_name}/{location_region}", inline=False)
        em1.add_field(name= "⌚Время", value= f"{location_localtime}", inline= False)
        em1.add_field(name= "🌡Температура", value= f"{current_temp_c} с°", inline= True)
        em1.add_field(name= "🎐Влажность", value= f"{current_humidity}%", inline = True)
        em1.add_field(name="🚩Скорость Ветра", value= f"{c_w_k1}m/s", inline= True)
        em1.set_thumbnail(url=f"https:{current_condition_icon}")
        await ctx.send(embed= em1)


        


class Moderation(commands.Cog): 
    def __init__(self, bot):   
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member):
        await ctx.guild.kick(user)
        await ctx.send(f"**{user.name}** был успешно кикнут")
    
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
         await ctx.send("Ты не можешь этого сделать!")

    @commands.command()
    @commands.has_permissions(ban_members= True)
    async def ban(self, ctx, user: discord.Member):
        await ctx.guild.ban(user)
        await ctx.send(f"🔨 **{user.name}** Был забанен") 

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
         await ctx.send("Ты не можешь этого сделать!")      

    #@commands.command()
    @commands.has_permissions(ban_members= True)
    async def unban(self, ctx, *, id):
        await ctx.guild.unban("id")
        await ctx.send(f"{id} был разбанен")

bot.add_cog(Moderation(bot))        
class Action(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def pat(self, ctx, user: discord.Member= None):
        random_number = random.randint(1 , 8)
        with open('pat.json') as f:
            imeg= json.load(f) 
            em= discord.Embed(title= '', description=(f"**✋{ctx.author.display_name}** погладил **{user.display_name}**"), color = (ctx.author.colour))
            em.set_image(url= (imeg[f'{random_number}']))
        await ctx.send(embed = em)
    
    @commands.command()
    async def poke(self, ctx, user: discord.Member= None):
        
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "poke"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**✋{ctx.author.display_name}** тыкнул **{user.display_name}**"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)
    
    @commands.command()
    async def slap(self, ctx, user: discord.Member= None):
       
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "slap"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**👊{ctx.author.display_name}** ударил **{user.display_name}**"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)
    
    @commands.command()
    async def punch(self, ctx, user: discord.Member= None):
       
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "dropkick"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**👊👊{ctx.author.display_name}** уебал **{user.display_name}**"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)
    
    @commands.command()
    async def kiss(self, ctx, user: discord.Member= None):
        
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "sweet kiss"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**💋{ctx.author.display_name}** сладко поцеловал **{user.display_name}**"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)
    

    @commands.command()
    async def hug(self, ctx, user: discord.Member= None):
        
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "hugging comfort"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**✋{ctx.author.display_name}** обнял **{user.display_name}**"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)

  

    @commands.command()
    async def cuddle(self, ctx, user: discord.Member= None):
        
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "cuddle hug"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**✋{ctx.author.display_name}** нежно прижал **{user.display_name}**"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)

    @commands.command()
    async def angry(self, ctx, user: discord.Member= None):
        
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "angry"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**😠{ctx.author.display_name}** разозлился"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)

    @commands.command()
    async def drink(self, ctx, user: discord.Member= None):
        """"""
        random_number = random.randint(0 , 5)
        api_key = (str(os.getenv('tenor')))
        lmt = 6
        search = "drinking"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api_key, lmt))
        response_json = r.json()
        imeg= response_json['results'][random_number]['media'][0]['gif']['url']
        em= discord.Embed(title= '', description=(f"**✋{ctx.author.display_name}** выпивает"), color = (ctx.author.colour))
        em.set_image(url= imeg)
        await ctx.send(embed = em)
 

bot.add_cog(Action(bot))

@bot.command(pass_context=True)
async def lyrics(ctx,*, lyrics_name):
    lyrics_url = f"https://api.ksoft.si/lyrics/search?q={lyrics_name}&limit=1"
    r =requests.get(lyrics_url, headers={"Authorization":(str(os.getenv('ksoft_key')))})
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

@bot.command(pass_context=True)
async def math(ctx,*, arg1):
    """Калькулятор"""
    res= str(eval(arg1))
    await ctx.send(f'Ваш ответ: {res}')        

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
    em1.add_field(name= "CPU", value= f"> {cpu_name}[{cpu_count}х ядерный]",inline= False)    
    em1.add_field(name= "RAM(Всего/Свободно/Занято)", value= f"> {totalmem}mb/{freemem}mb/{used}mb", inline= False)
    em1.add_field(name= "OS", value=f"> {nOS} {vOS}")
    em1.add_field(name= "Версия Python", value= f"> {platform.python_version()}", inline= True)
    await ctx.send(embed= em1)


@bot.command(pass_context=True)
@commands.has_permissions(manage_emojis=True)
async def createem(ctx, arg1, arg2):
    """Создание Смайлов: createem [url] [Name]"""
    url_img= (arg1)
    r=requests.get(url_img)
    await ctx.guild.create_custom_emoji(name= arg2,image=r.content)
    em1= discord.Embed(title= '', description = f"Успешно создан __**{arg2}**__", color = 0x008000)
    await ctx.send(embed= em1)

@createem.error
async def createem_error(self ,ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❗❗❗Ты не можешь этого сделать!")
        
bot.run(os.getenv('TOKEN'))
