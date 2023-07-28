from __future__ import print_function

import logging

import grpc
import time
import image_server_pb2
import image_server_pb2_grpc
from io import BytesIO
import csv

def iter_return_file(byt: bytes):
    yield image_server_pb2.ImageRequest(image=byt)
    return

def run():
    with open("tree.jpg", "rb") as f:
        byt = f.read()
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = image_server_pb2_grpc.ProcessorStub(channel)
        time_ls = []
        for i in range(1000):
            start_g = time.time()
            iter = stub.GrayscaleImage(iter_return_file(byt))
            end_g = time.time()
            
            start_i = time.time()
            iter = stub.InvertImage(iter_return_file(byt))
            end_i = time.time()
            
            start_ic = time.time()
            iter = stub.IconImage(iter_return_file(byt))
            end_ic = time.time()

            time_ls.append([str(i), end_g - start_g, end_i - start_i, end_ic - start_ic])
        
        with open("grpc_data.csv", "w") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerows(time_ls)





if __name__ == '__main__':
    logging.basicConfig()
    run()