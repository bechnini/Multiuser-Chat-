# MultiUser-CHAT
This is a last project in the beej networking conecpts guide book wich is the book i completed reading
# Client
Its a normal client that connects to the local host with specifying the username and the port
# Server
A Server That uses select to handle multiple clients at once
# Stuff Learned From This Project
> MultiThreading
> select()
# Usage
If you are using this on the same device you dont have to change the code but if you are not you should change the ip addr
`python server.py 5555`
`python client.py user_x 5555`
