from tornado import gen
from tornado import tcpserver


class TCPServer(tcpserver.TCPServer):
    """
        Base server for tcp server
    """

    protocol = None

    @gen.coroutine
    def handle_stream(self, stream, address):
        connection = self.protocol(stream)
        yield connection.on_connect()