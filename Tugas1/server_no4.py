import sys
import socket
import logging
import time

logging.basicConfig(level=logging.INFO)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)

    # Bind the socket to the port
    server_address = ('0.0.0.0', 32444)

    logging.info(f"starting up on {server_address}")
    sock.bind(server_address)
    sock.listen(1)
    while True:
        logging.info("waiting for a connection")
        connection, client_address = sock.accept()
        logging.info(f"connection from {client_address}")
        while True:
            data = connection.recv(1024)
            logging.info(f"received {data}")
            if data:
                logging.info("sending back data")
                connection.sendall(data)
            else:
                break
            
        connection.close()
except Exception as ee:
    logging.log(logging.INFO, f"ERROR: {str(ee)}")
finally:
    logging.log(logging.INFO, 'closing')
    sock.close()