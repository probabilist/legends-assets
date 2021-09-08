# legends-assets
 
This project is for extracting text assets from Star Trek: Legends. These instructions assume you are working on a Mac with Star Trek: Legends installed, and that you have an active Apple Arcade subscription.

First, download the Asset Studios C# solution (available at https://github.com/TemporalAgent7/AssetStudio/tree/legends). Inside the Asset Studios solution, find 'LegendsData/Program.cs' and replace it with the 'Program.cs' file found in this repository.

Open Star Trek: Legends and let it play a while, giving it time for all the assets to be downloaded.

Open the Asset Studios solution in Visual Studio. Find and run the `LegendsData` project inside the solution. Watch the console. If a new build number was found, update the value of `LAST_KNOWN_DEFAULT` in 'Program.cs'.

Text assets will be automatically extracted and can be found in the Asset Studios directory at 'LegendsData/bin/Debug/net5.0/extracted'.

**Optional:** First run the 'assetlist.py' Python script. (See 'requirements.txt' for the packages needed to run this script.) This will generate a file, 'assetlist.txt', that contains a list of all text assets currently in the game. Then copy this list into 'Program.cs'. This would only be necessary if a new text asset were introduced in a future update.

**Note:** In 'Program.cs', when `download` is set to `false`, the assets are extracted from the copy of the app stored locally; otherwise, assets are downloaded. When a hotfix is released, downloaded assets should be more up-to-date than those stored locally.
