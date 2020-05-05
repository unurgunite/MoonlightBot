# MoonlightBot Python

Here you can see chat bot for VK Social Network written in Python. Wanna use this bot? No problems. Just follow the instructions on.

## Documentation content
1. [Requirements][1]
2. [Starting][2]
    * [Linux/MacOS][3]
    * [Windows][4]
    * [~~Docker~~][5]
3. [Contribution][6]    

## Requirements
Firstly, clone the project to your computer and don't forget to install Python `--version 3.7` or higher.
* Clone the project to your local machine: <br>
```bash
git clone https://github.com/NekoDerek/MoonlightBot
```
* Install additional packages with `pip3`: <br>
```bash
pip3 install vk_api 
```
## Starting

### Linux/MacOS users
* First of all you need to set ENV _(environment variables)_ with **_group token and bot owner id_**: <br>
 ```bash
 echo "GROUP_ID=your_group_id" >> ~/.bashrc && echo "OWNER_ID=owner_id" >> ~/.bashrc && echo "TOKEN=your_group_token" >> ~/.bashrc && source ~/.bashrc
 ```
 Example: <br>
 ```bash
 echo "GROUP_ID=135178620" >> ~/.bashrc && echo "OWNER_ID=233676147" >> ~/.bashrc && echo "TOKEN=dfbipvsvbuir9u34938420fehwf" >> ~/.bashrc && source ~/.bashrc
 ```
* Open directory with Bot and type within Terminal: <br>
 ```bash
 cd MoonlightBot; python3 bot.py
 ```
Perfect! Now the bot running!

### Windows users
* First of all you need to set ENV _(environment variables)_ with **_group token and bot owner id_**: <br>
    * Click Right mouse button on My PC icon
    * Click on additional system parameters 
    * Click on Environmental Variables and set them. You need to set `OWNER_ID` and `TOKEN` variables
    * To check for environment variables enter in cmd.exe `set`, then find your variables
* Open directory with Bot and find bot.py file. Run it.
Perfect! Now the bot running!

### ~~Docker users~~
* ~~In next patch~~

## Modify roles
* Open `roles.json` file and type there user id who needs admins rights.
Example: <br>
```json5
{
 "Admin lvl2": [233676147],
 "Admin lvl1": [233676147]
}
```
**~~_Notice: Admin lvl1 role higher than Admin lvl2 role (in next patch this function will be added)_~~**

## Contribution
Contribute to the project development always welcome! You will need to create new branch and then push changes to the repository.<br>
```bash
$ git branch new-feature
$ edit your files
$ git commit -am 'Here is a new feature'
$ git pull-request
```
[1]:https://github.com/NekoDerek/MoonlightBot#requirements
[2]:https://github.com/NekoDerek/MoonlightBot#starting
[3]:https://github.com/NekoDerek/MoonlightBot#linuxmacos-users
[4]:https://github.com/NekoDerek/MoonlightBot#windows-users
[5]:https://github.com/NekoDerek/MoonlightBot#docker-users
[6]:https://github.com/NekoDerek/MoonlightBot#contribution
