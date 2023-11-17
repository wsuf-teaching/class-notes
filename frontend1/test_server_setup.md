# Simple form test environment setup

There are two bigger pieces required.

1. Live Server in Visual Studio Code to run the HTML page with the form in such a fashion that you are able to submit it and be able to receive answers properly.

2. Python as well as the included small python web "server".

## 1. Installing Live server in VS Code

Click on the "Extension" tab in the left side of VS Code, and then Search for "Live Server".

![liveserver](https://i.imgur.com/tEK077P.png)

Click on it, then click on Install on the left.

![liveserver2](https://i.imgur.com/iTac7eQ.png)

Once installed, a new button titled "Go Live" should appear on the lower right corner of your VS Code window.

![liveserver3](https://i.imgur.com/uYOR8xC.png)

From now on, if you click on the "Go Live" button, it should start a live server instance (by default on port 5500) serving your current folder. If it finds a file called `index.html` it will launch that as default, if not, it will launch your currently selected file. No matter, you can easily change the file to be run in the URL of your browsers.

> Clicking it again will stop the live server.

## 2. Installing Python

If not installed, you can download Python from the [official python website](https://www.python.org/).

> You can check whether you have it installed by typing "python" in your windows command line.

TODO IMAGE

In the top menu click on Downloads then in the dropdown there should be a button titled "Python x.y.z" (3.12.0 as of 2023.11.17). Download it and start the installation.

In the installer, what matters is that you put the checkmark in before "Add python.exe to PATH".

![python1](https://i.imgur.com/hytsmtw.png)

After doing that, you can click on "Install Now".

> After the installation, you may have to reopen your active terminal windows in order to be able to run python in them.

## 2.5 Installing flask with pip

Having installed python, there is one more thing we need to download. That is "flask", a micro web framework written in python that the little test web server of ours is running on.

Python automatically installs its own package manager called pip that we can use to get flask and other plugins or useful libraries.

Open your terminal window and type `pip install flask`.

## 3. Running the test server

Now all you need to do is download the [script](./server_script/server.py), and run it with python by navigating your terminal to the folder where you have downloaded it and then entering the following command:

```
python .\server.py
```

This small server by default will run on port 5000. Therefore its full address will be either `localhost:5000` or `127.0.0.1:5000`. Finally, as the endpoint defined in the server is `/test`, the actual endpoint you will have to send a request from your own form running through the Live server will be `http://127.0.0.1:5000/test`

> You can stop the small server by pressing CTRL+C on your keyboard while in the terminal or simply by closing the terminal window.