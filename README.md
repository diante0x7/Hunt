# Hunt - The CougarCS InfoSec Bot
Hunt is a swiss-army-knife cybersecurity helper, deployed within the CougarCS InfoSec server to aid users with developing shells, researching CVEs, displaying upcoming CTFs and (*soon*) presenting a leaderboard for HackTheBox pwns!

This bot uses discord\.py slash commands to operate.

*curated for and in loving memory of Nathan Hunt, CougarCS InfoSec 2023 Director and pioneer <3*

## Running the Hunt Client
The Hunt client has 4 distinct commands. They can all be accessed using --help, or are listed here:
#### hunt --configure
Configure your Hunt application by printing the discord token and an update channel ID associated with it's configuration.
#### hunt --config
Prints your current Hunt configuration to stdout.
#### hunt --version
List Hunt version information.

## Installation
Setting up Hunt is easy! All you require is a python3 installation and a discord bot key.

#### The automatic installer is built to target linux devices.

```bash
git clone https://github.com/diante0x7/Hunt.git
cd Hunt
sudo ./install
hunt
```

`./install` features all the setup tasks necessary to run Hunt as easily as possible. It performs the following tasks:
- Checks for current installation and removes it, if any.
- Installs all the required python modules through pip.
- Moves source code to `/usr/local/src/Hunt` for storage.
- Adds symlink from `/usr/local/src/Hunt/hunt` to `/usr/local/bin/hunt`.
- Runs `hunt --install` to obtain discord key information and configuration details.

#### You can also run it directly from source.
```bash
git clone https://github.com/diante0x7/Hunt.git
cd Hunt
pip install -r requirements.txt
cd src
python hunt --install
python hunt
```

## Output & Logs
Hunt logs information every time it starts and the status changes. It also logs each command as its used. All logs are printed through stdout and are displayed as `STATUS`, `WARNING`, or `ERROR`.