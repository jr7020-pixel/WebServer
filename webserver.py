# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))

    # Fill in start
    serverSocket.listen(1)  # Tell the socket to start listening for requests
    # Fill in end

    while True:
        # Establish the connection
        # print('Ready to serve...') # Commented out for Gradescope submission

        # Fill in start - are you accepting connections?
        connectionSocket, addr = serverSocket.accept()
        # Fill in end

        try:
            # Fill in start - a client is sending you a message
            message = connectionSocket.recv(1024).decode()
            # Fill in end

            filename = message.split()[1]

            # opens the client requested file.
            # We read as 'rb' (read bytes) to make sending easier.
            # Fill in start
            f = open(filename[1:], "rb")
            # Fill in end

            # Fill in start
            # The first line must be the HTTP Status line
            header = b"HTTP/1.1 200 OK\r\n"
            header += b"Server: MyPythonServer\r\n"
            header += b"Content-Type: text/html; charset=UTF-8\r\n"
            header += b"Connection: close\r\n"
            header += b"\r\n"  # Blank line to separate headers from body

            outputdata = header
            # Fill in end

            # Fill in start - append your html file contents
            outputdata += f.read()
            # Fill in end

            # Send everything as one send command
            # Fill in start
            connectionSocket.sendall(outputdata)
            # Fill in end

            connectionSocket.close()  # closing the connection socket

        except Exception as e:
            # Send response message for invalid request due to the file not being found (404)
            # Fill in start
            error_header = b"HTTP/1.1 404 Not Found\r\n"
            error_header += b"Content-Type: text/html; charset=UTF-8\r\n"
            error_header += b"Connection: close\r\n"
            error_header += b"\r\n"
            error_body = b"<html><body><h1>404 Not Found</h1></body></html>"

            connectionSocket.sendall(error_header + error_body)
            # Fill in end

            # Close client socket
            # Fill in start
            connectionSocket.close()
            # Fill in end


if __name__ == "__main__":
    webServer(13331)