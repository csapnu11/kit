# Project Kit


# Description
- This project is a Python-based Discord bot that listens to messages in specified Discord channels and executes predefined scripting tasks based on command triggers. It allows users to automate routine tasks or interact with external scripts directly from Discord in real-time.

The bot uses the Discord API via the discord.py library (or similar) and supports modular command handling, making it easy to extend with new features or automation scripts.


# Installation

## Create a venv
> python3 -m venv venv

## Activate venv
> source venv/bin/activate

## Add config.py (Contains global vars and configs)
> nano config.py

## Install requirements 
> pip install -r requirements.tx

## Run script
> python3 bot.py


# Installation script

## Linux
> bash install.sh



# Converting Script into Linux systemd service

0. Create installation script

- Make it executable 
> sudo chmod +x ./install.sh


1. Create a dedicated non sudo user for the service

- Create user
> sudo adduser --system --no-create-home --group discordbot

2. Set up project directory

- Project files destination. Copy repo and run the install.sh here
> sudo mkdir -p /opt/kit

- Change ownership of the folder to newly created dedicated user
> sudo chown -R discordbot:discordbot /opt/kit

- Run install script
> bash ./install.sh

3. Create start script
> sudo chmod +x ./start.sh
> sudo chown -R discordbot:discordbot /opt/kit/start.sh

4. Create the systemd service file
- Create file
> sudo nano /etc/systemd/system/kit.service


- Paste the ff:
```
[Unit]
Description=Kit Discord Bot Service
After=network.target

[Service]
Type=simple
User=discordbot
Group=discordbot
WorkingDirectory=/opt/kit
ExecStart=/opt/kit/start.sh
Restart=always
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target

```

6. Enable the service

- Reload daemon
> sudo systemctl daemon-reload

- Enable service
> sudo systemctl enable kit.service

- Start the service
> sudo systemctl start kit.service


7. Check the status of the service

> sudo systemctl status kit.service

- Check logs
> journalctl -u kit.service -f



# Optional: Removing kit as a service

1. Stop the service
> sudo systemctl stop kit.service

2. Disable the service
> sudo systemctl disable kit.service

3. Delete the service file
> sudo rm /etc/systemd/system/kit.service

4. Reload the services
> sudo systemctl daemon-reload


# Misc commands: 

- Checking if user is a sudoer, check if sudo is in return string
> groups #username#

- Delete user
> sudo deluser -R #username#

- Kill task
> sudo kill #PID#

> sudo kill -9 #PID#

- Stop processes by the user
> sudo pkill -u #username#

- Check what is the process by PID
> ps -fp #PID#