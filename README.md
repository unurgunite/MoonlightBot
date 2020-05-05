# MoonlightBot Python

Here you can see chat bot for VK Social Network written in Python. Wanna use this bot? No problems. Just follow the instructions on.

## Requirements
Firstly, clone the project to your computer and don't forget to install Python `--version 3.7` or higher.
* Clone the project to your local machine: <br>
`git clone https://github.com/NekoDerek/MoonlightBot`
* Install additional packages with `pip3`: <br>
`pip3 install vk_api` 

## Starting

### Linux users
* First of all you need to set ENV _(environment variables)_ with **_group token and bot owner id**: <br>
 `echo "GROUP_ID=your_group_id" >> ~/.bashrc && echo "OWNER_ID=owner_id" >> ~/.bashrc && echo "TOKEN=your_group_token" >> ~/.bashrc && source ~/.bashrc`<br>
 Example: <br>
 `echo "GROUP_ID=135178620" >> ~/.bashrc && echo "OWNER_ID=233676147" >> ~/.bashrc && echo "TOKEN=dfbipvsvbuir9u34938420fehwf" >> ~/.bashrc && source ~/.bashrc`<br> 
* Open directory with Bot and type inside Terminal: <br>
 `cd MoonlightBot; python3 bot.py`<br>
Perfect! Now the bot running!

### Windows users
* First of all you need to set ENV _(environment variables)_ with **_group token and bot owner id**: <br>
    * Click Right mouse button on My PC icon
    * Click on additional system parameters 
    * Click on Environmental Variables and set them. You need to set `OWNER_ID` and `TOKEN` variables
    * To check for environment variables available type in cmd.exe `set`, then find your variables
* Open directory with Bot and find bot.py file. Click on it.
Perfect! Now the bot running!

### ~~Docker users~~
* ~~In next patch~~


### Contribution
Contribute to the project development always welcome! You will need to create new branch and then push changes to the repository.<br>
`$ git branch new-feature`<br>
`$ <edit your files>`<br>
`$ git commit -am 'Here is a new feature'`<br>
`$ git pull-request`
