import grpc
import image_server_pb2_grpc
from concurrent import futures
import logging
from PIL import Image, ImageOps
import image_server_pb2
from io import BytesIO

class ImageServicer(image_server_pb2_grpc.ProcessorServicer):
    def __init__(self) -> None:
        super().__init__()

    def GrayscaleImage(self, request_iterator, context):
        """Sends a greeting
        """
        data = bytearray()
        for req in request_iterator:
            data.extend(req.image)
        bio = BytesIO(data)
        im = Image.open(bio)
        newim = ImageOps.grayscale(im)
        new_io = BytesIO()
        newim.save(new_io, "png")    
        yield image_server_pb2.ImageResponse(image=new_io.getvalue()) 
        return


    def InvertImage(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        data = bytearray()
        for req in request_iterator:
            data.extend(req.image)
        bio = BytesIO(data)
        im = Image.open(bio)
        newim = ImageOps.invert(im)
        new_io = BytesIO()
        newim.save(new_io, "png")    
        yield image_server_pb2.ImageResponse(image=new_io.getvalue()) 
        return

    def IconImage(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        data = bytearray()
        for req in request_iterator:
            data.extend(req.image)
        bio = BytesIO(data)
        im = Image.open(bio)
        newim = im.resize((32,32), Image.LANCZOS)
        new_io = BytesIO()
        newim.save(new_io, "png")    
        yield image_server_pb2.ImageResponse(image=new_io.getvalue()) 
        return
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_server_pb2_grpc.add_ProcessorServicer_to_server(
        ImageServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()