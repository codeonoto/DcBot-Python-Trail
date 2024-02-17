# <==== IMPORTING LIBS ====>
import discord
import asyncio
import datetime
import random
from urllib import response
from discord.ext import commands, tasks
from discord.ui import Button, View

# <--- IMPORTING FROM CHANNEL --->
# <--- Server IDs --->
from dc_roles import *
from dc_channel import *

# <--- IMPORTING FROM CHANNEL --->
from python_helper import *
from javascript_helper import *
from cpp_helper import *
from java_helper import *
from dsa_helper import *
from web_helper import *
from truth_dare import *
from imp_list import *

# <--- BOT TOKEN --->
from apikeys import TOKEN

# <==== SETTING CLIENT & PREFIX ====>
client = commands.Bot(command_prefix="c!", intents=discord.Intents.all())


# <--- ACTIVITY --->
# Function to get the status text
# <--- ACTIVITY --->
# Function to get the status text
def get_status():
    guild = client.get_guild(SERVER_ID)  # Replace YOUR_GUILD_ID with your server's ID
    if not guild:
        return "Server Not Found", discord.ActivityType.playing

    online_members = sum(
        1
        for member in guild.members
        if member.status in [discord.Status.online, discord.Status.dnd]
    )
    human_members = sum(1 for member in guild.members if not member.bot)
    total_members = guild.member_count

    status_text = f"Online : {online_members}"
    alt_status_text = f"Members: {human_members}"
    final_status_text = f"Total : {total_members}"

    return (
        status_text,
        alt_status_text,
        final_status_text,
        discord.ActivityType.watching,
    )


@tasks.loop(
    seconds=10
)  # Update status every 10 seconds, you can adjust this time as you like
async def update_status():
    (
        status_text,
        alt_status_text,
        final_status_text,
        activity_type,
    ) = get_status()

    # Display online members status for 10 seconds
    activity = discord.Activity(type=activity_type, name=status_text)
    await client.change_presence(activity=activity)
    await asyncio.sleep(10)

    # Display human members status for the next 10 seconds
    activity = discord.Activity(type=activity_type, name=alt_status_text)
    await client.change_presence(activity=activity)
    await asyncio.sleep(10)

    # Display total members status for the next 10 seconds
    activity = discord.Activity(type=activity_type, name=final_status_text)
    await client.change_presence(activity=activity)
    await asyncio.sleep(10)


# <==== BOT STARTING ====>
@client.event
async def on_ready():
    print("<--- ONOTO USED STARTING JUTSU --->")
    update_status.start()


# <==== BOT WELCOMING ====>
@client.event
async def on_member_join(member):
    # Get the guild (server) where the member joined
    guild = discord.utils.get(client.guilds, id=SERVER_ID)

    if guild is not None:
        # Get the welcome channel in the guild using the provided channel ID
        welcome_channel = discord.utils.get(guild.channels, id=WELCOME_CHANNEL_ID)

        if welcome_channel is not None:
            welcome_message_em_des = f"""**⊸ | Read {SR_RULE} and follow them.**\n\n**⊸ | Assign yourself roles in {SELF_ROLE_CHANNEL_ID}.**\n\n**⊸ | Read {SR_AN} for server/smp related annoucement.**\n\n**⊸ | Check {GIVEAWAY_CHANNEL_ID} for Giveaways Announcement.**\n\n**⊸ | Head towards {PUB_CHAT_CHANNEL_ID} for Chatting.**"""
            welcome_message = (
                f"Welcome {member.mention} to {guild.name}! Enjoy your stay."
            )
            wel = discord.Embed(
                title="**INFIRALS PARIVAAR APKA HARDIK SHWAGAT KARTA HAI !!**",
                description=f"{welcome_message_em_des}",
                color=0x00FFAA,
            )
            wel.set_image(
                url="https://cdn.discordapp.com/attachments/940114117199536159/1135119918744993852/standard_3.gif"
            )
            wel.set_footer(
                text="------------------------------------------------------------------\nIF YOU NEED ANY TYPE OF HELP THEN FEEL FREE TO PING STAFF !!"
            )
            yt_btn = Button(
                label="Subscribe Crow !!",
                url="https://www.youtube.com/@SBlockGamer",
                style=discord.ButtonStyle.link,
                emoji="🍟",
            )
            insta_btn = Button(
                label="Follow Crow !!",
                url="https://www.instagram.com/_ig_sblockgamer__/",
                style=discord.ButtonStyle.link,
                emoji="🌭",
            )
            view = View()
            view.add_item(yt_btn)
            view.add_item(insta_btn)

            await welcome_channel.send(welcome_message)
            await welcome_channel.send(embed=wel, view=view)
        else:
            print("Welcome channel not found.")
    else:
        print("Guild not found.")


# <==== BOT COMMANDS - HELLO ====>
@client.command(
    aliases=[
        "hey",
        "hi",
        "hii",
        "hiii",
        "Hullo",
        "Heyo",
        "Helu",
        "Ello",
        "Holla",
        "Haylo",
        "Heiyo",
        "Aloha",
        "uh-loh-ha",
        "Howdy",
    ]
)
async def hello(ctx):
    user = ctx.author
    admin_role = ctx.guild.get_role(S_MANGER_ROLE_ID)
    hmod_role = ctx.guild.get_role(CHIEF_ROLE_ID)
    kitty_role = ctx.guild.get_role(KIITIES_ROLE_ID)

    # <--- OWNER HELLO --->
    if await client.is_owner(user):
        await ctx.send(f"Aryy {user.mention}, **Hello!!**")
    # <--- ADMIN HELLO --->
    elif admin_role in user.roles:
        await ctx.send(f"**Hello**, Sigma Boii {user.mention} !!")
    # <--- HMOD HELLO --->
    elif hmod_role in user.roles:
        await ctx.send(f"**Hello**, Sakt Ladke {user.mention} !!")
    # <--- KITTY HELLO --->
    elif kitty_role in user.roles:
        await ctx.send(f"**Hello**, Kitty {user.mention} !!")
    # <--- NORMAL HELLO --->
    else:
        await ctx.send(f"**Hello** {user.mention} !!")


# <==== BOT COMMANDS - RULES ====>
@client.command()
async def rules(ctx):
    em_description = "\n".join(rules_list)
    rule = discord.Embed(
        title="**INFIRALS RULES**", description=f"{em_description}", color=0x00FFAA
    )
    rule.add_field(
        name="CHECK ANNOUNCEMENT",
        value=f"**To Stay `Up-To-Date` in server:** {SR_AN}",
        inline=False,
    )
    # rule.set_image(
    #     url="https://cdn.discordapp.com/attachments/940114117199536159/1135097547942277201/standard_4.gif"
    # )
    rule.set_footer(
        text="------------------------------------------------------------------\nIF YOU NEED ANY TYPE OF HELP THEN FEEL FREE TO PING STAFF !!"
    )
    # <!-- Wait 5 Sec && Delete Msg -->
    await ctx.send(embed=rule)
    await asyncio.sleep(5)
    await ctx.message.delete()


# <==== BOT COMMANDS - ROLE INFO ====>
@client.command()
async def rolesinfo(ctx):
    user = ctx.author
    s_manger_role = discord.utils.get(ctx.guild.roles, id=S_MANGER_ROLE_ID)
    s_manger_mention = s_manger_role.mention
    chief_role = discord.utils.get(ctx.guild.roles, id=CHIEF_ROLE_ID)
    chief_mention = chief_role.mention
    hmod_role = discord.utils.get(ctx.guild.roles, id=HMOD_ROLE_ID)
    hmod_mention = hmod_role.mention
    mod_role = discord.utils.get(ctx.guild.roles, id=MOD_ROLE_ID)
    mod_mention = mod_role.mention
    mmod_role = discord.utils.get(ctx.guild.roles, id=M_MOD_ROLE_ID)
    mmod_mention = mmod_role.mention
    role_info = f"""**Server Manager:** {s_manger_mention}
The Server Manager is responsible for overseeing the entire Discord server. They handle administrative tasks, manage server settings, and ensure the smooth functioning of the community. They work closely with other staff members to maintain a positive environment, resolve conflicts, and make important decisions concerning the server's direction and growth.

**Chief Moderator:** {chief_mention}
The Chief Moderator is a senior staff member who supervises the moderation team. They lead and guide other moderators, ensuring that rules are enforced consistently and fairly. They may assist in creating and updating server rules, and act as a point of contact between the moderation team and server management.

**Head Moderator:** {hmod_mention}
The Head Moderator is responsible for the day-to-day moderation of the Discord server. They monitor chats, enforce rules, and address any issues that arise within the community. They work closely with other moderators to maintain a friendly and welcoming atmosphere and are often the first line of action when it comes to maintaining order.

**Moderator (Mod):** {mod_mention}
Moderators are essential team members who keep the Discord server safe and friendly. They enforce rules, warn or mute disruptive users, and may have the ability to kick or ban offenders if necessary. Moderators actively engage with the community, assist users with questions or concerns, and foster a positive environment for everyone.

**Minecraft Moderator (Minecraft Mod):** {mmod_mention}
This role is specifically tailored for Minecraft-related servers. Minecraft Moderators have the same responsibilities as regular moderators but with a focus on maintaining order within the Minecraft game environment. They ensure players adhere to the server's rules, prevent cheating or griefing, and help create a fun and enjoyable experience for all players.
"""
    em_description = role_info
    rule = discord.Embed(
        title="**INFIRALS STAFF ROLES INFO**",
        description=f"{em_description}",
        color=0x00FFAA,
    )

    rule.set_image(
        url="https://cdn.discordapp.com/attachments/940114117199536159/1135097547942277201/standard_4.gif"
    )
    rule.set_footer(
        text="------------------------------------------------------------------\nIF YOU NEED ANY TYPE OF HELP THEN FEEL FREE TO PING STAFF !!"
    )
    # <!-- Wait 5 Sec && Delete Msg -->
    await ctx.send(embed=rule)
    await asyncio.sleep(5)
    await ctx.message.delete()


# <==== BOT COMMANDS - HHS3-RULES ====>
@client.command()
async def hhrules(ctx):
    em_description = "\n".join(hhs3_rules_list)
    rule = discord.Embed(
        title="**HALF HEART SEASON 3 - RULES**",
        description=f"{em_description}",
        color=0x00FFAA,
    )
    rule.set_image(
        url="https://cdn.discordapp.com/attachments/1126696313292079175/1127500327176896552/half-heart.gif"
    )

    rule.add_field(
        name="CHECK ANNOUNCEMENT",
        value=f"**To Stay `Up-To-Date` in SMP:** {SR_AN}",
        inline=False,
    )
    rule.add_field(
        name="READ & FOLLOW RULES",
        value=f"**To see if any `rules` were updated:** {SR_RULE}",
        inline=False,
    )
    rule.set_footer(
        text="------------------------------------------------------------------\nIF YOU NEED ANY TYPE OF HELP THEN FEEL FREE TO PING STAFF !!"
    )
    # <!-- Wait 5 Sec && Delete Msg -->
    await ctx.send(embed=rule)
    await asyncio.sleep(5)
    await ctx.message.delete()


# <==== BOT COMMANDS - VOTE ====>
vote_message = """
> **┅┅┅┅┨ ⛏ INFIRALS SEASON 1 - VOTING  ⛏ ┠┅┅┅┅**
> 
> **Vote for our Minecraft Survival Server on the mentioned websites and earn exciting in-game rewards! Your support makes our community stronger !**
> 
> **┅┅┅┅┨ ⛏ VOTE HERE  ⛏ ┠┅┅┅┅**
> 
> - **Pocket/Bedrock Player have to use `B_` as a prefix**
>  - **Eg: ** `B_SBlockGamer` 
> 
> - **Minecraft Best Servers :**
>  - [**CLICK ME !**](<https://minecraftbestservers.com/server-infirals.1458/vote>)
> 
> - **Topg Org :**
>  - [**CLICK ME !**](<https://topg.org/minecraft-servers/server-658103>)
> 
> - **Minecraft-Mp :**
>  - [**CLICK ME !**](<https://minecraft-mp.com/server-s325384>)
> 
> **┅┅┅┅┨ ⛏ THANKING YOU  ⛏ ┠┅┅┅┅**
"""


# Define a command to send the message
@client.command()
async def vote(ctx):
    await ctx.send(vote_message)
    # <!-- Wait 5 Sec && Delete Msg -->
    await asyncio.sleep(5)
    await ctx.message.delete()
    # <!-- Wait 55 Sec (Total Wait = 60 sec) && Delete Msg -->
    await asyncio.sleep(55)
    await response.delete()


# <==== BOT COMMANDS - IP ====>
kit_message = """
> **┅┅┅┅┨ ⛏ INFIRALS SEASON 1 - KITS  ⛏ ┠┅┅┅┅**
> 
> - **Purchase kits to support our server. Your small contribution will take our server to the next level.**
> 
> **┅┅┅┅┨ ⛏ KIT PRICE ⛏ ┠┅┅┅┅**
> 
> - **We have three kits available for purchase. **
> 
> - **VAMPIRE KIT :** `₹150`
> - **PHANTOM KIT :** `₹200`
> - **SUPREME KIT :** `₹350`
> 
> **┅┅┅┅┨ ⛏ SPECIAL ENCHANTMENT BOOK ⛏ ┠┅┅┅┅**
> 
> - **WINGS : ** `₹150` **_This will help you to flyyyyyyyyy !!_**
> - **TRENCH IX : ** `₹100` **_This will help you to mine 3x3 area !!_**
> 
> **Create a ticket to claim your perks:** <#1154313625780101171>
> 
> - **IF YOU WILL PURCHASE SUPREME KIT WITH CE BOOKS**
> `₹350 + ₹150 + ₹100 = ₹600`
> 
> - **"BUT YOU WILL GET IT FOR ONLY :**  `₹420`
> 
>  - **MAKE TICKET TO GET EARLY DISCOUNT**
> 
> **┅┅┅┅┨ ⛏ THANKING YOU  ⛏ ┠┅┅┅┅**
"""


# Define a command to send the message
@client.command()
async def kit(ctx):
    await ctx.send(kit_message)
    # <!-- Wait 5 Sec && Delete Msg -->
    await asyncio.sleep(5)
    await ctx.message.delete()
    # <!-- Wait 55 Sec (Total Wait = 60 sec) && Delete Msg -->
    await asyncio.sleep(55)
    await response.delete()


# <==== BOT COMMANDS - IP ====>
@client.command(aliases=["infip, smp"])
async def ip(ctx):
    ip = discord.Embed(
        title="INFIRALS SEASON 1",
        description="\n-----------------------\n",
        color=0x00FFAA,
    )
    ip.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/940114117199536159/1162603208443711578/chr_INF_S1-Logo.png?"
    )
    ip_field_value = " `play.infirals.in`"
    ip_port = "  `25596`\n"
    ip.add_field(
        name="**MINECRAFT JAVA IP :**",
        value=ip_field_value,
        inline=False,
    )
    ip.add_field(
        name="**MINECRAFT POCKET/BEDROCK PORT :**",
        value=ip_port,
        inline=False,
    )
    ip.add_field(name="CHECK ANNOUNCEMENT", value=INF_AN, inline=False)
    ip.add_field(name="READ & FOLLOW RULES", value=INF_RULE, inline=False)
    ip.set_image(
        url="https://media.discordapp.net/attachments/1158400466707820614/1160845898549567588/standard_1.gif?"
    )
    ip.set_footer(
        text="------------------------------------------------------------------\nIF YOU NEED ANY TYPE OF HELP THEN FEEL FREE TO PING STAFF !!"
    )
    response = await ctx.send(embed=ip)

    # <!-- Wait 5 Sec && Delete Msg -->
    await asyncio.sleep(5)
    await ctx.message.delete()
    # <!-- Wait 55 Sec (Total Wait = 60 sec) && Delete Msg -->
    await asyncio.sleep(55)
    await response.delete()


ip_message = """
> **┅┅┅┅┨ ⛏ INFIRALS SEASON 1  ⛏ ┠┅┅┅┅**
> 
> - **JAVA :**
>  - **Ip:** `play.infirals.in`
> 
> - **Bedrock :**
>  - **Ip:** `play.infirals.in`
>  - **Port:** `25596`
> 
> **┅┅┅┅┨ ⛏ ENJOY ⛏ ┠┅┅┅┅**
"""


@client.event
async def on_message(message):
    if message.author.bot:  # Ignore messages from bots
        return
    content = message.content.lower()
    if "ip" in content:
        await message.channel.send(ip_message)
    await client.process_commands(message)


# <=== AUTO EMBED CREATION ===>
@client.command(aliases=["eu"])
async def emburl(ctx, *, args):
    args = args.split('"')

    args = list(filter(lambda x: x.strip() != "", args))

    if len(args) != 3:
        await ctx.send(
            'Invalid arguments. Usage: o!emburl "Title" "Description" "URL Link"'
        )
        return

    title, description, url_link = args
    embed = discord.Embed(title=title, description=description, color=0x00FFAA)

    view = discord.ui.View()
    view.add_item(Button(label="Click Me", url=url_link, emoji="🥪"))
    await ctx.send(embed=embed, view=view)
    await ctx.message.delete()


# <=== AUTO MSG ===>
@client.command(aliases=["em"])
async def embmsg(ctx, *, args):
    args = args.split('"')

    args = list(filter(lambda x: x.strip() != "", args))

    if len(args) != 2:
        await ctx.send('Invalid arguments. Usage: o!embmsg "Message" "URL Link"')
        return

    message, url_link = args
    embed = discord.Embed(description=message, color=0x00FFAA)

    view = discord.ui.View()
    view.add_item(Button(label="Click Me", url=url_link, emoji="🥪"))
    await ctx.send(embed=embed, view=view)
    await ctx.message.delete()


# <=== APPLY FOR SMP ===>
@client.command()
async def apply(ctx):
    ip = discord.Embed(
        title="HALF HEART SEASON 3",
        description=" - To apply for smp please fill the below mentioned form.",
        color=0x00FFAA,
    )
    ip.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1126696313292079175/1127500327176896552/half-heart.gif"
    )
    ip.set_footer(
        text="------------------------------------------------------------------\nIF YOU NEED ANY TYPE OF HELP THEN FEEL FREE TO PING STAFF !!"
    )
    application_btn = Button(
        label="APPLY FOR SMP !!",
        url="https://forms.gle/BHWTBSrjXETB63zS9",
        style=discord.ButtonStyle.link,
        emoji="📃",
    )

    application_view = View()
    application_view.add_item(application_btn)

    response = await ctx.send(embed=ip, view=application_view)
    # <!-- Wait 5 Sec && Delete Msg -->
    await asyncio.sleep(5)
    await ctx.message.delete()
    # <!-- Wait 55 Sec (Total Wait = 60 sec) && Delete Msg -->
    await asyncio.sleep(55)
    await response.delete()


# <=== PERMANENT APPLICATION ==>
@client.command()
async def application(ctx):
    ip = discord.Embed(
        title="HALF HEART SEASON 3",
        description=" - To apply for smp please fill the below mentioned form.",
        color=0x00FFAA,
    )
    ip.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1126696313292079175/1127500327176896552/half-heart.gif"
    )
    ip.set_footer(
        text="------------------------------------------------------------------\nIF YOU NEED ANY TYPE OF HELP THEN FEEL FREE TO PING STAFF !!"
    )
    application_btn = Button(
        label="APPLY FOR SMP !!",
        url="https://forms.gle/BHWTBSrjXETB63zS9",
        style=discord.ButtonStyle.link,
        emoji="📃",
    )

    application_view = View()
    application_view.add_item(application_btn)

    await ctx.send(embed=ip, view=application_view)
    # <!-- Wait 5 Sec && Delete Msg -->
    await asyncio.sleep(5)
    await ctx.message.delete()


# <==== SBLOCK LINKS LINKS ====>
@client.command(aliases=["links", "sblink", "socialmedia"])
async def sm(ctx):
    ip = discord.Embed(
        title="SBLOCK",
        description="** - 🎮🔥 Join me, a passionate Minecraft gamer, on epic quests and creative builds! Subscribe on YouTube & follow on Instagram for thrilling content and pixelated adventures!**",
        color=0x00FFAA,
    )
    ip.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/940114117199536159/1132699504148217937/INFIRALS.png"
    )
    ip.set_footer(
        text="------------------------------------------------------------------\nIF YOU NEED ANY TYPE OF HELP THEN FEEL FREE TO PING STAFF !!"
    )
    yt_btn = Button(
        label="Subscribe Crow !!",
        url="https://www.youtube.com/@SBlockGamer",
        style=discord.ButtonStyle.link,
        emoji="🥵",
    )
    insta_btn = Button(
        label="Follow Crow !!",
        url="https://www.instagram.com/_ig_sblockgamer__/",
        style=discord.ButtonStyle.link,
        emoji="😊",
    )
    view = View()
    view.add_item(yt_btn)
    view.add_item(insta_btn)

    await ctx.send(embed=ip, view=view)
    # <!-- Wait 5 Sec && Delete Msg -->
    await asyncio.sleep(5)
    await ctx.message.delete()


# <==== YOUTUBE LINKS ====>
@client.command(aliases=["yt"])
async def youtube(ctx):
    ip = discord.Embed(
        title="SBLOCK - YOUTUBE",
        description="** - Discover endless blocks of fun and excitement! Subscribe to my channel for epic adventures and creative building in the pixelated universe.**",
        color=0x00FFAA,
    )
    ip.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/940114117199536159/1132699762886443100/main-sbg.jpg"
    )
    ip.set_footer(
        text="------------------------------------------------------------------\nIF YOU NEED ANY TYPE OF HELP THEN FEEL FREE TO PING STAFF !!"
    )
    yt_btn = Button(
        label="Subscribe Crow !!",
        url="https://www.youtube.com/@SBlockGamer",
        style=discord.ButtonStyle.link,
        emoji="🥵",
    )

    yt_view = View()
    yt_view.add_item(yt_btn)

    await ctx.send(embed=ip, view=yt_view)
    # <!-- Wait 5 Sec && Delete Msg -->
    await asyncio.sleep(5)
    await ctx.message.delete()


# <==== INSTA LINKS ====>
@client.command(aliases=["ig"])
async def insta(ctx):
    ip = discord.Embed(
        title="SBLOCK",
        description="** - 🎮🔥 Join me, a passionate Minecraft gamer, on epic quests and creative builds! Subscribe on YouTube & follow on Instagram for thrilling content and pixelated adventures!**",
        color=0x00FFAA,
    )
    ip.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/940114117199536159/1132699504148217937/INFIRALS.png"
    )
    ip.set_footer(
        text="------------------------------------------------------------------\nIF YOU NEED ANY TYPE OF HELP THEN FEEL FREE TO PING STAFF !!"
    )
    insta_btn = Button(
        label="Follow Crow !!",
        url="https://www.instagram.com/_ig_sblockgamer__/",
        style=discord.ButtonStyle.link,
        emoji="😊",
    )
    view = View()
    view.add_item(insta_btn)

    await ctx.send(embed=ip, view=view)
    # <!-- Wait 5 Sec && Delete Msg -->
    await asyncio.sleep(5)
    await ctx.message.delete()


# <==== TIER LINKS ====>
# @client.command(aliases=["tt"])
# async def tiertest(ctx):
#     tt = discord.Embed(
#         title="Asia NethPot Tierlist",
#         description="** - Introducing our vibrant and dynamic Competitive Gaming Discord Server! Are you ready to take your gaming skills to the next level and connect with like-minded players? Look no further! Join our growing community of passionate gamers and immerse yourself in exhilarating competitions, challenging tournaments, and exciting events across various popular games. Whether you're a seasoned pro or a rising star, our supportive environment fosters growth, teamwork, and friendly competition. Gain access to expert tips, strategies, and coaching sessions, all while making new friends and building lasting gaming connections. Level up your gaming journey and become a part of something truly extraordinary. Join our Competitive Gaming Discord Server today and embrace the thrill of competitive gaming like never before! **",
#         color=0x00FFAA,
#     )
#     tt.set_image(
#         url="https://cdn.discordapp.com/attachments/940114117199536159/1135265464252112957/standard_5.gif"
#     )
#     tt.set_footer(
#         text="------------------------------------------------------------------\nIF YOU NEED ANY TYPE OF HELP THEN FEEL FREE TO PING STAFF !!"
#     )
#     tt_btn = Button(
#         label="TierTest HERE !!",
#         url="https://discord.gg/raqbjDRE",
#         style=discord.ButtonStyle.link,
#         emoji="⚔️",
#     )
#     view = View()
#     view.add_item(tt_btn)

#     await ctx.send(embed=tt, view=view)
#     # <!-- Wait 5 Sec && Delete Msg -->
#     await asyncio.sleep(5)
#     await ctx.message.delete()


# <==== BOT ENDING ====>
@client.command()
# <--- Only the bot owner can execute this command --->
@commands.is_owner()
async def close(ctx):
    response = await ctx.send("<--- CLOSING JUTSU --->")
    await ctx.message.delete()
    await response.delete()
    await client.close()


@close.error
async def close_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "> Oops! You don't have the required permissions to use this command. `LOL` 😂 ",
            delete_after=5,
        )


# <==== CLEARING MSG ====>
@client.command(aliases=["c"])
async def clear(ctx, amount: int):
    if any(role.id in AUTHORIZED_ROLES for role in ctx.author.roles):
        try:
            # Delete the requested amount of messages (add 1 to also delete the command message)
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(
                f"> Successfully cleared `{amount}` messages.", delete_after=5
            )
        except discord.Forbidden:
            await ctx.send(
                "Oops! I don't have the required permissions to clear messages.",
                delete_after=5,
            )
    else:
        await ctx.send(
            "> You don't have permission to use this command. `LOL` 😂 ", delete_after=5
        )

    await asyncio.sleep(5)
    await ctx.message.delete()


# <==== KICK ====>
@client.command(aliases=["k"])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided."):
    try:
        await member.kick(reason=reason)
        await ctx.send(
            f"{member.mention} has been kicked from the server. Reason: {reason}",
            delete_after=5,
        )
    except discord.Forbidden:
        await ctx.send(
            "Oops! I don't have the required permissions to kick members.",
            delete_after=5,
        )
    except discord.HTTPException:
        await ctx.send(
            "An error occurred while trying to kick the member.", delete_after=5
        )

    await asyncio.sleep(5)
    await ctx.message.delete()


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "> Oops! You don't have the required permissions to use this command. `LOL` 😂 ",
            delete_after=5,
        )


# <==== BAN ====>
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided."):
    try:
        await member.ban(reason=reason)
        await ctx.send(
            f"{member.mention} has been banned from the server. Reason: {reason}",
            delete_after=5,
        )
    except discord.Forbidden:
        await ctx.send(
            "Oops! I don't have the required permissions to ban members.",
            delete_after=5,
        )
    except discord.HTTPException:
        await ctx.send(
            "An error occurred while trying to ban the member.", delete_after=5
        )

    await asyncio.sleep(5)
    await ctx.message.delete()


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "> Oops! You don't have the required permissions to use this command. `LOL` 😂 ",
            delete_after=5,
        )


# <==== TIMEOUT ====>
@client.command(aliases=["to"])
@commands.has_permissions(manage_roles=True)
async def timeout(
    ctx, member: discord.Member, duration: int, *, reason="No reason provided."
):
    try:
        muted_role = discord.utils.get(
            ctx.guild.roles, name="Muted"
        )  # Make sure you have a role named "Muted"
        if not muted_role:
            await ctx.send(
                "The 'Muted' role does not exist. Please create it first.",
                delete_after=5,
            )
            return

        await member.add_roles(muted_role)
        await ctx.send(
            f"{member.mention} has been muted for {duration} minutes. Reason: {reason}",
            delete_after=5,
        )

        # Unmute the member after the specified duration (in minutes)
        await discord.utils.sleep_until(
            ctx.message.created_at + discord.timedelta(minutes=duration)
        )
        await member.remove_roles(muted_role)
        await ctx.send(
            f"{member.mention} has been unmuted after {duration} minutes.",
            delete_after=5,
        )
    except discord.Forbidden:
        await ctx.send(
            "Oops! I don't have the required permissions to manage roles.",
            delete_after=5,
        )
    except discord.HTTPException:
        await ctx.send(
            "An error occurred while trying to mute/unmute the member.", delete_after=5
        )
    await asyncio.sleep(5)
    await ctx.message.delete()


async def unmute_after_timeout(member, unmute_time):
    while datetime.datetime.utcnow() < unmute_time:
        await discord.utils.sleep_until(unmute_time)

    muted_role = discord.utils.get(member.guild.roles, name="Muted")
    await member.remove_roles(muted_role)
    await member.send(f"You have been unmuted after the timeout.")

@timeout.error
async def timeout_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "> Oops! You don't have the required permissions to use this command. `LOL` 😂 ",
            delete_after=5,
        )


# <==== RELEASE TIMEOUT ====>
@client.command(aliases=["rto"])
@commands.has_permissions(manage_roles=True)
async def release_timeout(ctx, member: discord.Member):
    try:
        muted_role = discord.utils.get(
            ctx.guild.roles, name="Muted"
        )  # Make sure you have a role named "Muted"
        if not muted_role:
            await ctx.send(
                "The 'Muted' role does not exist. Please create it first.",
                delete_after=5,
            )
            return

        if muted_role in member.roles:
            await member.remove_roles(muted_role)
            await ctx.send(
                f"{member.mention} has been released from timeout.", delete_after=5
            )
        else:
            await ctx.send(
                f"{member.mention} is not currently in timeout.", delete_after=5
            )
    except discord.Forbidden:
        await ctx.send(
            "Oops! I don't have the required permissions to manage roles.",
            delete_after=5,
        )
    except discord.HTTPException:
        await ctx.send(
            "An error occurred while trying to release the member from timeout.",
            delete_after=5,
        )
    await asyncio.sleep(5)
    await ctx.message.delete()


@release_timeout.error
async def release_timeout_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "> Oops! You don't have the required permissions to use this command. `LOL` 😂 ",
            delete_after=5,
        )


# <==== TRUTH CMDS ====>
def is_allowed_channel(ctx):
    return ctx.channel.id == TRUTH_DARE_CHANNEL_ID


@client.command(aliases=["t"])
@commands.check(is_allowed_channel)
async def truth(ctx):
    await ctx.send(f"{ctx.author.mention}, {random.choice(truths)}")


@truth.error
async def truth_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        # If the command is used in a non-allowed channel, mention the allowed channel in the response
        channel_mention = f"<#{TRUTH_DARE_CHANNEL_ID}>"
        await ctx.send(
            f" > The `{ctx.invoked_with}` command can only be used in {channel_mention}."
        )
        await asyncio.sleep(5)
        await ctx.message.delete()


# <==== DIRTY TRUTH CMDS ====>
@client.command(aliases=["dt"])
@commands.check(is_allowed_channel)
async def dtruth(ctx):
    await ctx.send(f"{ctx.author.mention}, {random.choice(dirty_truths)}")


@dtruth.error
async def dtruth_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        # If the command is used in a non-allowed channel, mention the allowed channel in the response
        channel_mention = f"<#{TRUTH_DARE_CHANNEL_ID}>"
        await ctx.send(
            f" > The `{ctx.invoked_with}` command can only be used in {channel_mention}."
        )
        await asyncio.sleep(5)
        await ctx.message.delete()


# <==== DARE CMDS ====>
@client.command(aliases=["d"])
@commands.check(is_allowed_channel)
async def dare(ctx):
    await ctx.send(f"{ctx.author.mention}, {random.choice(dares)}")


@dare.error
async def dare_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        # If the command is used in a non-allowed channel, mention the allowed channel in the response
        channel_mention = f"<#{TRUTH_DARE_CHANNEL_ID}>"
        await ctx.send(
            f" > The `{ctx.invoked_with}` command can only be used in {channel_mention}."
        )
        await asyncio.sleep(5)
        await ctx.message.delete()


# <==== BOT MESSAGE ====>


# <--- GREATING --->
@client.event
async def on_message(message):
    if message.author.bot:  # Ignore messages from bots
        return

    content_lower = message.content.lower()

    greetings = [
        "hello",
        "hemlo",
        "hey",
        "Hullo",
        "Heyo",
        "Helu",
        "Ello",
        "Holla",
        "Haylo",
        "Heiyo",
        "Aloha",
        "uh-loh-ha",
        "Howdy",
        "Ello",
        "ello",
    ]

    if content_lower in greetings:
        user = message.author
        admin_role = discord.utils.get(user.roles, id=ADMIN_ROLE_ID)
        hmod_role = discord.utils.get(user.roles, id=HMOD_ROLE_ID)
        kitty_role = discord.utils.get(user.roles, id=KIITIES_ROLE_ID)

        # <--- OWNER HELLO --->
        if await client.is_owner(user):
            await message.channel.send(f"Aryy {user.mention} **Hello!!**")
            return

        # <--- ADMIN HELLO --->
        if admin_role:
            await message.channel.send(f"**Hello**, Sigma Boii {user.mention} !!")
        # <--- HMOD HELLO --->
        elif hmod_role:
            await message.channel.send(f"**Hello**, Sakt Ladke {user.mention} !!")
        # <--- KITTY HELLO --->
        elif kitty_role:
            await message.channel.send(f"**Hello**, Kitty {user.mention} !!")
        # <--- NORMAL HELLO --->
        else:
            await message.channel.send(f"**Hello** {user.mention} !!")

    await client.process_commands(message)


client.run(TOKEN)
