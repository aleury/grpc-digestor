import grpc
from . import digestor_pb2
from . import digestor_pb2_grpc


class DigestorClient(object):
    """
    Client to access the Digestor Service.
    """
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 46001
        self.channel = grpc.insecure_channel(f'{self.host}:{self.server_port}')
        self.stub = digestor_pb2_grpc.DigestorStub(self.channel)

    def get_digest(self, message):
        return self.stub.GetDigest(
            digestor_pb2.DigestRequest(ToDigest=message),
        )
