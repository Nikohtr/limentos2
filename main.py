import discord
from discord.ext import commands
import asyncio
import contextlib
import io
import inspect
import ast
import nacl
import ffmpeg
import os
import sys
intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix='!', intents=intents)
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    
def insert_returns(body):
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


@client.command()
async def eval_fn(ctx, *, cmd):
    if ctx.message.author.id == 263685060819943425:
        fn_name = "_eval_expr"

        cmd = cmd.strip("` ")

        cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

        body = f"async def {fn_name}():\n{cmd}"

        parsed = ast.parse(body)
        body = parsed.body[0].body

        insert_returns(body)

        env = {
            'bot': ctx.bot,
            'discord': discord,
            'commands': commands,
            'ctx': ctx,
            'niko': client.get_user(263685060819943425),
            'niko_server': client.get_guild(358325566891360256).get_member(263685060819943425),
            'server': client.get_guild(358325566891360256),
            '__import__': __import__
        }
        exec(compile(parsed, filename="<ast>", mode="exec"), env)
        result = (await eval(f"{fn_name}()", env))
        try:
            await ctx.send(result)
        except:
            pass
    else:
        pass
    
@client.command()
async def clear(ctx):
    if ctx.message.author.id == 263685060819943425:
        await ctx.send("Restarting!")
        os.system("python3 main.py")
        sys.exit()
    else:
        pass
        
token = os.getenv("DISCORD_BOT_SECRET")
client.run(token)
