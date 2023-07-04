import sys
import socket
import logging

logging.basicConfig(level=logging.INFO)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the port
    server_address = ('0.0.0.0', 10000)

    logging.info(f"starting up on {server_address}")
    sock.bind(server_address)
    sock.listen(1)

    while True:
        logging.info("waiting for a connection")
        connection, client_address = sock.accept()
        logging.info(f"connection from {client_address}")

        while True:
            data = connection.recv(32)
            logging.info(f"received {data}")
            if data:
                logging.info("sending back data")
                connection.sendall(data)
            else:
                break

        connection.close()

except Exception as ee:
    logging.log(logging.ERROR, f"ERROR: {str(ee)}")

finally:
    logging.log(logging.INFO, 'closing')
    sock.close()
