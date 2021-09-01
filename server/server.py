import socketserver

# Note to self: 
#           probably threading should be a thing to use 
#           because the server needs to continuously send the posistion of the ball to the clients without interupting 

# https://docs.python.org/3/library/socketserver.html

# A class for a TCP socket server
class socketTCPhandler(socketserver.BaseRequestHandler):
    """
        When a client does any type of input the server should 
    """    
    def handler(self):
        pass


# A class for a UDP socket server
class socketUDPhandler(socketserver.BaseRequestHandler):
    
    def handler(self):
        pass

def server():
    HOST, PORT = 0, 0
    with socketserver.TCPServer((HOST, PORT), socketTCPhandler) as socketServer:
        
        socketServer.serve_forever()


if __name__ == "__main__":
    server()
