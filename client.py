import grpc
import service_pb2_grpc
import service_pb2

import logging
def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = service_pb2_grpc.SimpleStub(channel)
        response = stub.Hello(service_pb2.HelloRequest(name="world"))
        print(response.reply)

if __name__ == "__main__":
    logging.basicConfig()
    run()