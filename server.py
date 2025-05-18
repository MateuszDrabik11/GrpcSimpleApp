from concurrent import futures
import logging
import grpc

import service_pb2_grpc
import service_pb2

# inheritance
class HelloService(service_pb2_grpc.SimpleServicer):
    def Hello(self, request, context):
        return service_pb2.HelloReply(reply=f"Hello, {request.name}")

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_SimpleServicer_to_server(HelloService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()