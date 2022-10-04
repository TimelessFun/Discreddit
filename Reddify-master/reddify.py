import configparser
import traceback
from datetime import datetime

import apraw
import discord
from discord.ext import commands
from sqlalchemy.sql.expression import and_

from cmds import HelpCommand
from cogs import UserCog
from const import VERSION
from database.database import session
from database.models import DiscordUser, Guild
from helpers import advanced_user

intents = discord.Intents.default()
intents.members = True


class Reddify(commands.Bot):
    def __init__(self, **options):
        super().__init__(
            "!",
            description="The official Reddify bot by Dan6erbond to seamlessly connect Reddit and Discord.",
            help_command=HelpCommand(),
            intents=intents,
            **options)
        self.reddit = apraw.Reddit("TRB")

    async def on_ready(self):
        print(f'{self.user.name} is running.')

    async def on_command_error(self, ctx: commands.Context, error: Exception):
        if isinstance(error, discord.ext.commands.errors.CommandNotFound):
            pass
        else:
            await ctx.message.channel.send(error)
            traceback.print_tb(error.__traceback__)

    async def on_message(self, msg: discord.Message):
        if msg.author.id == self.user.id:
            return
        # await msg.channel.send("Reddify is currently being overhauled to a v2. " +
            #  "For more information check out the GitHub Repo: https://github.com/Dan6erbond/Reddify-v2.")
        await bot.process_commands(msg)

    @property
    def embed(self):
        embed = discord.Embed(
            colour=discord.Colour(0).from_rgb(254, 63, 24)
        )
        embed.set_footer(text=f"Reddify v{VERSION}", icon_url=bot.user.avatar_url)
        embed.timestamp = datetime.utcnow()

        return embed

    def get_embed(self):
        return self.embed

    async def send_error(self, message):
        await self.get_channel(556732041752739840).send(message)

    async def update_guild_user(self, guild: Guild, discord_user: DiscordUser):
        g = bot.get_guild(guild.guild_id)
        if g is None:
            return

        m = g.get_member(discord_user.user_id)
        if m is None:
            return

        verified_accounts = [acc for acc in discord_user.reddit_accounts if acc.verified]

        if guild.set_role:
            role = g.get_role(guild.role)

            if not role:
                role = await g.create_role(name="Verified Redditor",
                                           colour=discord.Colour(0).from_rgb(254, 63, 24),
                                           mentionable=True,
                                           reason="Verified Redditors get this role by the bot.")
                guild.role = role.id
                session.commit()

            if verified_accounts:
                await m.add_roles(role)
            else:
                await m.remove_roles(role)

        if guild.set_username:
            for account in verified_accounts:
                try:
                    await m.edit(nick=f"/u/{account.username}")
                except discord.errors.Forbidden:
                    await self.send_error(f"❗ I don't have the necessary permissions to change {m.mention}'s nickname.")
                finally:
                    break

    @commands.command(help="Get a user's verified Reddit account(s).")
    @commands.check(advanced_user)
    async def reddify(self, ctx: commands.Context, user_id: int):
        pass


extensions = ["cogs.user_cog", "cogs.guild_cog",
              "cogs.channel_cog", "cogs.reddit_cog"]

if __name__ == "__main__":
    bot = Reddify()

    config = configparser.ConfigParser()
    config.read("discord.ini")

    for extension in extensions:
        bot.load_extension(extension)
        print(f"{extension} loaded.")

    bot.run(config["TRB"]["MTAyNjcxMjAwNjAxMjcwNjgyNg.GNDXpc.Fc7q7SllTh8n3e8i03wbKyMv8Hz4y0lX4Y0TXE"])
 