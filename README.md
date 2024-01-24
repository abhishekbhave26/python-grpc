# Introduction:
gRPC client and server in Python using a proto file
This project defines a gRPC Greet Service using Protocol Buffers (proto3). Key features include:

# Project Overview: gRPC Greet Service

Unary RPC (SayHello): Single request, single response.
Server Streaming (ParrotSaysHello): Server sends a stream of responses.
Client Streaming (ChattyClientSaysHello): Client sends a stream of requests, receives a delayed response.
Bidirectional Streaming (InteractingHello): Both client and server exchange streams of messages.
Message Structure:

HelloRequest: User's name and an optional greeting.
HelloReply: Server's response message.
DelayedReply: Delayed server message with an array of client requests.

# Setup:

# pip install grpcio-tools
# python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. .\protos\greet.proto

# Start server:

# python greet_server.py

# Start Client:

# python greet_client.py
