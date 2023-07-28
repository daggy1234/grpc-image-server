# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import image_server_pb2 as image__server__pb2


class ProcessorStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GrayscaleImage = channel.stream_stream(
                '/image_server.Processor/GrayscaleImage',
                request_serializer=image__server__pb2.ImageRequest.SerializeToString,
                response_deserializer=image__server__pb2.ImageResponse.FromString,
                )
        self.InvertImage = channel.stream_stream(
                '/image_server.Processor/InvertImage',
                request_serializer=image__server__pb2.ImageRequest.SerializeToString,
                response_deserializer=image__server__pb2.ImageResponse.FromString,
                )
        self.IconImage = channel.stream_stream(
                '/image_server.Processor/IconImage',
                request_serializer=image__server__pb2.ImageRequest.SerializeToString,
                response_deserializer=image__server__pb2.ImageResponse.FromString,
                )


class ProcessorServicer(object):
    """The greeting service definition.
    """

    def GrayscaleImage(self, request_iterator, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InvertImage(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IconImage(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProcessorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GrayscaleImage': grpc.stream_stream_rpc_method_handler(
                    servicer.GrayscaleImage,
                    request_deserializer=image__server__pb2.ImageRequest.FromString,
                    response_serializer=image__server__pb2.ImageResponse.SerializeToString,
            ),
            'InvertImage': grpc.stream_stream_rpc_method_handler(
                    servicer.InvertImage,
                    request_deserializer=image__server__pb2.ImageRequest.FromString,
                    response_serializer=image__server__pb2.ImageResponse.SerializeToString,
            ),
            'IconImage': grpc.stream_stream_rpc_method_handler(
                    servicer.IconImage,
                    request_deserializer=image__server__pb2.ImageRequest.FromString,
                    response_serializer=image__server__pb2.ImageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'image_server.Processor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Processor(object):
    """The greeting service definition.
    """

    @staticmethod
    def GrayscaleImage(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/image_server.Processor/GrayscaleImage',
            image__server__pb2.ImageRequest.SerializeToString,
            image__server__pb2.ImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InvertImage(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/image_server.Processor/InvertImage',
            image__server__pb2.ImageRequest.SerializeToString,
            image__server__pb2.ImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IconImage(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/image_server.Processor/IconImage',
            image__server__pb2.ImageRequest.SerializeToString,
            image__server__pb2.ImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
