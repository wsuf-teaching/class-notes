##  Intalling SQLite3

Go to the official SQLite download page: [SQLite Download Page](https://sqlite.org/download.html).

![sqlite3page](https://i.imgur.com/Wkrn9Fe.png)

Under the section "Precompiled Binaries for Windows," look for  "sqlite-tools-win32-x64-xxx.zip" (`xxx` representing the current version number, should be 3460000 as of 2024.06.11). Click on the link to download the ZIP file.

Extract the downloaded zip file to a location. For example to `C:\sqlite3`.

![extracc](https://i.imgur.com/dBWt9Ia.png)

Add SQLite3 to the System PATH. 
Search for "environment variables" in the start menu.

![sqsearch](https://i.imgur.com/TzQYzkV.png)

Click on "environment variables...".

![sqenv](https://i.imgur.com/eMqehIY.png)

In the Environment Variables window, scroll down in the "System variables" section, select the "Path" variable, and click on the "Edit..." button.

![sqeditenv](https://i.imgur.com/iLAokPV.png)

In the Edit Environment Variable window, click "New.", enter the path to the folder where you extracted the SQLite3 binaries (e.g., `C:\sqlite3`) and then click "OK" to close all windows.

![addsqenv](https://i.imgur.com/E8sGTvP.png)

![finsqenv](https://i.imgur.com/Q297kMo.png)

## Verifying the installation

Open a command prompt, and type `sqlite3 --version` and press "Enter". If successful, you should see the version of SQLite3 displayed.

![succ](https://i.imgur.com/7dJvmqg.png)


