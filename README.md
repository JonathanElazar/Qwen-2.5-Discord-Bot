# Qwen 2.5 Discord Bot 🤖
## About ❔
Qwen 2.5 Discord Bot is a discord bot based on the Qwen 2.5:0.5b LLM model. It runs on its own discord server and allows the user to open a DM with the bot and chat with it.
## How to run
You can run this on pretty much any device. Windows and Linux guides will be listed here. Before following these guides make sure you have [Ollama](https://ollama.com/) and [Python](https://www.python.org/) installed.
# Run on windows 🪟
First you need to install qwen2.5:0.5b which can be done with the terminal command ```ollama pull qwen2.5:0.5b``` and test it with  ```ollama run qwen2.5:0.5b```  
Next create a virtual environment with the command ```py -m venv venv```  
If you are on command prompt than enter the venv with ```venv\Scripts\activate.bat```  
If you are on powershell than enter the venv with ```.\venv\Scripts\Activate.ps1```  
Now use the command ```pip install -r requirements.txt``` to install the required dependencies.
Now open credentials.py and fill in the credentials with the credentials of your bot.
Finally use the command ```py main.py``` to run the program

# Run on linux 🐧
First you need to install qwen2.5:0.5b which can be done with the terminal command ```ollama pull qwen2.5:0.5b```  and test it with  ```ollama run qwen2.5:0.5b```    
Next create a virtual environment with the command ```python3 -m venv venv```  
Enter the venv with ```source venv/bin/activate```  
Now use the command ```pip install -r requirements.txt``` to install the required dependencies.  
Now open credentials.py and fill in the credentials with the credentials of your bot.  
Finally use the command ```python3 main.py``` to run the program
