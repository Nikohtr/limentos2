import discum
import os
t = os.getenv("discord_token")
bot = discum.Client(token=t)
@bot.gateway.command
def resptest(resp):
    if resp.event.message:
        if resp.raw['d']['author']['id'] == '432610292342587392' and resp.raw['d']['embeds'][0]['author']['name'] == "Jax":
            bot.addReaction(resp.raw['d']['channel_id'],resp.raw['d']['id'], "👍")
bot.gateway.run()
