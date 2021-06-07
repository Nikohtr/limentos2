import discum
import os
import time
ch = ["zero two", "richard watterson"]
t = os.getenv("discord_token")
bot = discum.Client(token=t)
@bot.gateway.command
def resptest(resp):
    if resp.event.message:
        if (resp.raw['d']['author']['id'] == '432610292342587392' or resp.raw['d']['author']['id'] == '780731609060999178')and resp.raw['d']['embeds'][0]['author']['name'].lower() in ch and ("React with any emoji to claim!" in resp.raw['d']['embeds'][0]['description'] or "Wished by" in resp.raw['d']['content']):
            time.sleep(0.2)
            print(bot.getMessage(resp.raw['d']['channel_id'],resp.raw['d']['id']))
            bot.addReaction(resp.raw['d']['channel_id'],resp.raw['d']['id'], "👍")
bot.gateway.run()
