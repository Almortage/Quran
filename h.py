from pyrogram import Client

api_id = "14911221" 
api_hash = "a5e14021456afd496e7377331e2e5bcf"
bot_token = "6235769542:AAFVN1es9frhiiqxJtJ345yuFpbVC7usQ-E"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

app.run()
