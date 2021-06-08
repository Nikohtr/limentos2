import discum
import os
ch = ["zero two", "richard watterson"]
t = os.getenv("discord_token")
bot = discum.Client(token=t)
@bot.gateway.command
def respnowish(resp):
    if resp.event.message:
        if (resp.raw['d']['author']['id'] == '432610292342587392' or resp.raw['d']['author']['id'] == '780731609060999178')and resp.raw['d']['embeds'][0]['author']['name'].lower() in ch and "React with any emoji to claim!" in resp.raw['d']['embeds'][0]['description']:
            bot.addReaction(resp.raw['d']['channel_id'],resp.raw['d']['id'], "👍")
def respwish(resp):
    if resp.event.reaction_added:
        msg = bot.getMessage(resp.raw['d']['channel_id'],resp.raw['d']['message_id'])
        print("\n\n\n\n\n\n\n\n\n\n\n", msg, msg.raw, "\n\n\n\n\n\n\n\n\n\n\n")
        if (msg['d']['author']['id'] == '432610292342587392' or msg['d']['author']['id'] == '780731609060999178')and msg['d']['embeds'][0]['author']['name'].lower() in ch and "Wished by" in msg['d']['content']:
            bot.addReaction(resp.raw['d']['channel_id'],resp.raw['d']['id'], "👍")
bot.gateway.run()
