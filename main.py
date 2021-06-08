import discum
import os
import requests
ch = ["zero two", "richard watterson"]
t = os.getenv("discord_token")
bot = discum.Client(token=t)
@bot.gateway.command
def respnowish(resp):
    if resp.event.message:
        if (resp.raw['d']['author']['id'] == '432610292342587392' or resp.raw['d']['author']['id'] == '780731609060999178') and resp.raw['d']['embeds'][0]['author']['name'].lower() in ch and "React with any emoji to claim!" in resp.raw['d']['embeds'][0]['description']:
            bot.addReaction(resp.raw['d']['channel_id'],resp.raw['d']['id'], "👍")
    if resp.event.reaction_added:
        msg = bot.getMessage(resp.raw['d']['channel_id'],resp.raw['d']['message_id']).json()
        if (msg[0]['author']['id'] == '432610292342587392' or msg[0]['author']['id'] == '780731609060999178') and (resp.raw['d']['member']['user']['id'] == '432610292342587392' or resp.raw['d']['member']['user']['id'] == '780731609060999178') and msg[0]['embeds'][0]['author']['name'].lower() in ch and "Wished by" in msg[0]['content']:
            bot.addReaction(msg[0]['channel_id'],msg[0]['id'], "👍")
bot.gateway.run()
