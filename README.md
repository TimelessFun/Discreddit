# Discreddit

Discreddit is the open-source rework of the original [Reddify](https://github.com/Dan6erbond/Reddify) bot. It makes use of [aPRAW's](http://apraw.readthedocs.io/) asynchronous functionality, Discord.py as well as a SQLite3 database to enable a seamless connection between Discord and Reddit.

## Contents

- [Discreddit](#discreddit)
  - [Contents](#contents)
  - [Usage](#usage)
    - [Admin Setup](#admin-setup)
    - [Verification](#verification)
    - [Commands](#commands)
  - [Community and Support](#community-and-support)
    - [Contributing](#contributing)
  - [License](#license)

## Usage

Discreddit is a public bot hosted by r/avatartrading and can be invited to any public server via its [invite link](https://discord.com/api/oauth2/authorize?client_id=1026712006012706826&permissions=8&scope=bot). Upon invitation, Server administrators can use the commands available to configure the bot and should also consider disabling members from changing their nickname if they wish for all of the nicknames to follow the "/u/<reddit-username>" convention.

### Admin Setup

Server admins can use the following commands to configure Reddify:

- `!toggle <role|username|nick>`: Based on the selection of either role, username or nick, the feature will be toggled on or off.
  - **role:** Creates a role in the guild that is assigned to members who have verified their Reddit account.
  - **username:** Automatically sets members' usernames to the format of "/u/<reddit-username>" after the verification process has been completed.
  - **nick:** Allows members to use the `!nick <nickname>` command to change the guild nickname to "<nickname> (/u/<reddit-username>)".
- `!setguildsub <subreddit>`: Sets the subreddit that stats will be fetched for in the guild if no argument is passed to `!substats`.
- `!setchannelsub <subreddit>`: Sets the subreddit that stats will be fetched for in the channel if no argument is passed to `!substats`.
- `!status`: Shows the current status of the bot's configuration in the guild.

### Verification

Users of the Discreddit bot can connect as many Reddit accounts as they wish to a single Discord account. The process is very straightforward:

1.  Initiate the process with the `!verify <reddit-username>` command.
2.  Respond to the message sent by the bot with `verify`.
3.  Wait until a checkmark appears on the bot's message in Discord, and the verification is complete!

To undo the verification or if the bot might have missed the `verify` message on Reddit, the `!unverify <reddit-username>` command can be used. If any errors are found, an issue can be created on GitHub or the developer directly contacted on Discord.

### Commands

Besides verification and server setup, there are a couple commands that help connect Reddit and Discord via Disreddit:

- `!me`: Displays all your (un)verified accounts.
- `!nick <nickname>`: Sets a nickname before the "/u/<reddit-username>" part if the feature has been enabled in the guild.
- `!stats <optional-username>`: Displays the stats of a user's linked accounts.
- `!substats <optional-subreddit>:` Displays the stats of a subreddit.

## Community and Support

Discreddit is actively being maintained. This bot was made for the subreddit [r/avatartrading](https://www.reddit.com/r/avatartrading/)

### Contributing

As Disreddit is open-source under the GPLv3 license, all additions and bug reports in the form of issues and pull requests are encouraged.

## License

Disreddit's source is provided under GPLv3.
