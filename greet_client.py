import greet_pb2
import greet_pb2_grpc
import time
import grpc

def run():
    with grpc.insecure_channel("localhost:50066") as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. Say Hello - Unary")
        print("2. ParrotSaysHello - Server Side Streaming")
        print("3. ChattyClientSaysHello - Client Side Streaming")
        print("4. InteractingHello - Both Streaming")

        rpc_call = input("Which rpc would you like to make: ")
        if rpc_call == 1:
            hello_request = greet_pb2.HelloRequest(greeting="Hello", name="Youtube")
            hello_reply = stub.SayHello(hello_request)
            print("SayHello Response Received")
            print(hello_reply)
        elif rpc_call == 2:
            print("NA")
        elif rpc_call == 3:
            print("NA")
        elif rpc_call == 4:
            print("NA")
        else:
            print("Oops wrong option selected. Try again !!")


if __name__ == "main":
    run()
