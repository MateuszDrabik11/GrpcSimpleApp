# Simple GRPC app with Python

# service.proto

It describes the gRPC service and messages that are used to communicate between server and client.

`service Simple {
    rpc Hello(HelloRequest) returns (HelloReply) {}
}
`
Service consists of methods that accept a message or stream of messages and returns another message or stream of messages.

Message is an objects that stores data that are being sent. 
Because gRPC is staticly typed you have to specify type of every field and also each field has a number that is used for serialization.
Features of Protocol buffers used in gRPC:
- messages can be nested in other messages
- field can be repeated to send an array of values
- optional fields
- enums
- there's no inheritance

https://protobuf.dev/programming-guides/proto3/

# server.py

`class HelloService(service_pb2_grpc.SimpleServicer):
    def Hello(self, request, context):
        return service_pb2.HelloReply(reply=f"Hello, {request.name}")
`
This is the implementation of service that was declared in .proto file, rest of the code is to start and configure server.
Server can use things like encryption and authorization what makes gRPC very secure.
