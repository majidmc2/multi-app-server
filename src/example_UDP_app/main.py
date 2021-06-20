import threading

from runserver.abstract import AbstractProtocol
from setting.setting import applications, logger
from example_UDP_app.socket_handler import ThreadedUDPServer, ThreadedSNMPRequestHandler


class UDPProtocol(AbstractProtocol):

    def __main(self):
        udp_port = applications["example_UDP_app"]["configurations"]["port"]
        local_ip = applications["example_UDP_app"]["configurations"]["local_address"]
        server = ThreadedUDPServer((local_ip, udp_port), ThreadedSNMPRequestHandler)
        try:
            '''Start a thread with the server -- that thread will then start one'''
            ip, port = server.server_address
            '''more thread for each request'''
            server_thread = threading.Thread(target=server.serve_forever)
            server_thread.daemon = True
            server_thread.start()
            logger.info(f"Server loop running on {ip}:{port}")
            server_thread.join()
        except KeyboardInterrupt:
            server.shutdown()
            logger.critical("Shutdown server")

    def protocol(self, *args, **kwargs):
        self.__main()
