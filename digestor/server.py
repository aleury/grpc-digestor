import time
from concurrent import futures

import grpc

from . import digestor
from . import digestor_pb2
from . import digestor_pb2_grpc


class DigestorServicer(digestor_pb2_grpc.DigestorServicer):
    """
    gRPC server for the Digestor Service
    """
    def __init__(self, *args, **kwargs):
        self.server_port = 46001

    def GetDigest(self, request, context):
        """
        Implementation of the rpc GetDigest declared in the
        the proto file above.
        """
        digest = digestor.digest(request.ToDigest)
        return digestor_pb2.DigestResponse(Digest=digest)

    def start(self):
        """
        Function which actually starts th gRPC server, and preps
        it for serving incoming connections.
        """
        digestor_server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=10),
        )

        digestor_pb2_grpc.add_DigestorServicer_to_server(
            DigestorServicer(),
            digestor_server,
        )

        digestor_server.add_insecure_port(f'[::]:{self.server_port}')
        digestor_server.start()
        print('Digestor Server running...')

        try:
            while True:
                time.sleep(60*60*60)
        except KeyboardInterrupt:
            digestor_server.stop(0)
            print('Digestor Server Stopped...')


if __name__ == '__main__':
    server = DigestorServicer()
    server.start()
