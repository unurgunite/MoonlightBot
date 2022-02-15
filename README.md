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
 cd MoonlightBot; echo "GROUP_ID=your_group_id" >> config.py && echo "OWNER_ID=owner_id" >> config.py && echo "TOKEN=\"your_group_token\"" >> config.py
 ```
 Example: <br>
 ```bash
 cd MoonlightBot; echo "GROUP_ID=135178620" >> config.py && echo "OWNER_ID=123456789" >> config.py && echo "TOKEN=\"dfbipvsvbuir9u34938420fehwf\"" >> config.py
 ```
* Open directory with Bot and type within Terminal: <br>
 ```bash
 cd MoonlightBot; python3 bot.py
 ```
Perfect! Now the bot running! **Don't forget to enable LongpoolServer in your group settings!**

### Windows users
* First of all you need to set ENV _(environment variables)_ with **_group token and bot owner id_**: <br>
    * Click Right mouse button on My PC icon
    * Click on additional system parameters 
    * Click on Environmental Variables and set them. You need to set `OWNER_ID`, `GROUP_ID` and `TOKEN` variables
    * To check for environment variables enter in cmd.exe `set`, then find your variables
* Open directory with Bot and find bot.py file. Run it.
Perfect! Now the bot running! **Don't forget to enable LongpoolServer in your group settings!**

### ~~Docker users~~
* ~~In next patch~~

## Modify roles
* Open `roles.json` file and type there user id who needs admins rights.
Example: <br>
```json5
{
 "Admin lvl2": [1234567],
 "Admin lvl1": [1234567]
}
```
**~~_Notice: Admin lvl1 role higher than Admin lvl2 role (in next patch this function will be added)_~~**

## Contribution
Contribute to the project development always welcome! You will need to fork this project then create new branch and push changes to the repository.<br>
```bash
$ git branch new-feature
$ edit your files
$ git commit -am 'Here is a new feature'
$ git pull-request
```
[1]:https://github.com/unurgunite/MoonlightBot#requirements
[2]:https://github.com/unurgunite/MoonlightBot#starting
[3]:https://github.com/unurgunite/MoonlightBot#linuxmacos-users
[4]:https://github.com/NekoDerek/MoonlightBot#windows-users
[5]:https://github.com/NekoDerek/MoonlightBot#docker-users
[6]:https://github.com/NekoDerek/MoonlightBot#contribution
