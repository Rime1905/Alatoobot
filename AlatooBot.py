import discord
from discord.utils import get
from discord_components import Button, Select, SelectOption, ComponentsBot

token = ('OTY3MDkyODg5MDI2OTY5NzAw.YmLRcA.uZiKdZdYOVpQ2ojoYNlFP3Oqfwk')

bot = ComponentsBot("!")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")


@bot.command()
async def button(ctx):
    await ctx.send("Buttons!", components=[Button(label="Button", custom_id="button1")])
    interaction = await bot.wait_for(
        "button_click", check=lambda inter: inter.custom_id == "button1"
    )
    await interaction.send(content="Button Clicked")

@bot.command()
async def xd(ctx):
    embedVar = discord.Embed(title="Python news", color=000000)
    embedVar.set_image(url="https://img1.wallspic.com/crops/4/9/3/3/6/163394/163394-python_programer-python-programming_language-standing-source_code-3840x2160.png")
    embedVar.add_field(name="----------------------------------------------", value="There will be news from r/Python (Python's Subreddit)", inline=True)
    await ctx.send(embed=embedVar)

@bot.command()
async def select(ctx):
    await ctx.send(
        "Select your department",
        components=[
            Select(
                placeholder="Press this menu",
                options=[
                    SelectOption(label="Computer Science", value="СomputerScience"),
                    SelectOption(label="Medicine", value="Medicine")
                ],
                custom_id="select1",
            )
        ],
    )

    interaction = await bot.wait_for(
        "select_option", check=lambda inter: inter.custom_id == "select1"
    )
    memberRole = discord.utils.get(ctx.guild.roles, name=f"{interaction.values[0]}")
    await interaction.send(content=f"{interaction.values[0]} selected. Role Acquired!")
    await ctx.author.add_roles(memberRole)

bot.run(token)