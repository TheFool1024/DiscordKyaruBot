import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(722086294662152215)
    await channel.send(f'{member}加入了美食殿堂！')
    print(f'{member}join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(722086294662152215)
    await channel.send(f'{member}被佩可误食，离开了我们...')
    print(f'{member}leave!')

@bot.command()
async def 延迟(ctx):
    await ctx.send(f'{bot.latency*1000}ms')

@bot.command()
async def 延遲(ctx):
    await ctx.send(f'{bot.latency*1000}ms')

@bot.command()
async def 变身(ctx):
    await ctx.send(f'我没有梦想，但我可以守护佩可的梦想!')
    await ctx.send(f'Standing by!')
    await ctx.send(f'HenShin!')
    await ctx.send(f'Complete!')

@bot.command()
async def 變身(ctx):
    await ctx.send(f'我沒有夢想，但我可以守護佩可的夢想!')
    await ctx.send(f'Standing by!')
    await ctx.send(f'HenShin!')
    await ctx.send(f'Complete!')

@bot.command()
async def 吃(ctx):
    


bot.run('NzI2ODEzMzA2OTcwNzAxOTQ0.XwHuRQ.RLkGCZxY3EudstH7eHoQeikjVrQ') 
    
