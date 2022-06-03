import discord
from discord.utils import get
from discord_components import Button, Select, SelectOption, ComponentsBot


bot = ComponentsBot("!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")


@bot.command()
async def button(ctx):
    await ctx.send("Placeholder!", components=[Button(label="Button", custom_id="button1")])
    interaction = await bot.wait_for(
        "button_click", check=lambda inter: inter.custom_id == "button1"
    )
    await interaction.send(content="Button Clicked")


@bot.command()
async def links(ctx):
    embedVar = discord.Embed(
        title="List of Alatoo related links", color=000000)
    embedVar.add_field(name="-------------------------------------------",
                       value="http://alatoo.edu.kg/#gsc.tab=0\n https://www.instagram.com/alatoo.edu.kg/\nhttps://ocs.alatoo.edu.kg\nhttps://my.alatoo.edu.kg", inline=True)
    await ctx.send(embed=embedVar)


@bot.command()
async def select(ctx):
    await ctx.send(
        "Select your department",
        components=[
            Select(
                placeholder="Press this menu",
                options=[
                    SelectOption(label="Computer Science",
                                 value="СomputerScience"),
                    SelectOption(label="Medicine", value="Medicine")
                ],
                custom_id="select1",
            )
        ],
    )

    interaction = await bot.wait_for(
        "select_option", check=lambda inter: inter.custom_id == "select1"
    )
    memberRole = discord.utils.get(
        ctx.guild.roles, name=f"{interaction.values[0]}")
    await interaction.send(content=f"{interaction.values[0]} selected. Role Acquired!")
    await ctx.author.add_roles(memberRole)


@bot.command()
async def help(ctx):
    embedVar = discord.Embed(
        title="List of commands", color=000000)
    embedVar.add_field(name="-------------------------------------------",
                       value="!button\n!links\n!select", inline=True)
    await ctx.send(embed=embedVar)

bot.run(token)
