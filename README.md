# vertex

## intro to me and why i built it
Hi i am harshit and i am a teen who loves to code so recently i came across a problem the keyboard on my secondary laptop which i use to learn linux and more was not working and i had one external wired keyboard which i use with my main laptop so i wanted a solution where i can skip the hassle of connecting and disconnecting my keyboard  between the laptops so that's why i built vertex.

## about vertex
it is a program where you can use one keyboard between one to two laptops not simultaneously but one at a time without having to physically connect or disconnect anything . It works using sockets and pynput where every key you type gets transferred to the secondary laptop using a connection between the two laptops and then you can use the keyboard on the other laptop also

## how to download and run it(using .exe)(easy way)
* go to the releases page on this repo and download the both "for main laptop"and"for secondary laptop" .exe and run the **server.exe** first then the **main.exe**
* if the "windows protected your PC" page shows up then go to the more info button and click run anyway windows blocks random .exe file from running thats why
* enjoy the software


## how to use it(using code)(hard way)
* download the code from the github
* download all libraries mentioned in requirement either download it at once or individually by using  **`pip install pynput`** in the terminal, powershell, cmd etc 
* you can get the IP of your secondary laptop if it is linux by running **`hostname -I`** in the terminal and
* type your secondary laptop ip in the main.py dedicated slot (i have added a comment above it )
* run the server.py on secondary laptop and the main.py on the main laptop
* enjoy
## some error management
*if you see something like **`WinError 10013`** then do the steps mentioned on the next lines
* try disabling the windows firewall for private protection
* disconnect the VPN
* change the port number the number which looks like (7777) or anything like this

## IMPORTANT
* **dont use VPN**

* **dont share your IP**
## licence
MIT use it as you want but don't forget to give me credits
byee
