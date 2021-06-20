import socket
import threading

from sqlalchemy import or_, and_
from runserver.db_base import Session
from setting.setting import applications, logger



class ThreadedSNMPRequestHandler(BaseRequestHandler):
    """
    Threaded SNMP request handler.
    Document: https://docs.python.org/3/library/socketserver.html#socketserver-udpserver-example
    """

    def __init__(self, request, client_address, server):
        self.socket = None
        self.thread = threading.current_thread()
        self.iv = applications["snmp"]["configurations"]["text"]
        super(ThreadedSNMPRequestHandler, self).__init__(request, client_address, server)

    def handle(self):

        request_data = self.request[0].strip()
        self.socket = self.request[1]

        # TODO: Write Your Codes
        # Example:
        # db_session = Session()
        # user = db_session.query(User).filter(User.user_id).first()
        # db_session.close()


class ThreadedUDPServer(ThreadingMixIn, UDPServer):
    """
    Nothing to add here, inherited everything necessary from parents.
    """
    pass
