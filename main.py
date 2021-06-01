import discum
import os
t = os.getenv("discord_token")
bot = discum.Client(token=t)
@bot.gateway.command
def resptest(resp):
    if resp.event.message:
        print("React with any emoji to claim!" in resp.raw['d']['embeds'][0]['description'])
        if resp.raw['d']['author']['id'] == '780731609060999178' and resp.raw['d']['embeds'][0]['author']['name'] == "Jax" and "React with any emoji to claim!" in resp.raw['d']['embeds'][0]['description']:
            bot.addReaction(resp.raw['d']['channel_id'],resp.raw['d']['id'], "👍")
bot.gateway.run()
