# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ibc.core.connection.v1 import tx_pb2 as ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the ibc/connection Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ConnectionOpenInit = channel.unary_unary(
                '/ibc.core.connection.v1.Msg/ConnectionOpenInit',
                request_serializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenInit.SerializeToString,
                response_deserializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenInitResponse.FromString,
                )
        self.ConnectionOpenTry = channel.unary_unary(
                '/ibc.core.connection.v1.Msg/ConnectionOpenTry',
                request_serializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenTry.SerializeToString,
                response_deserializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenTryResponse.FromString,
                )
        self.ConnectionOpenAck = channel.unary_unary(
                '/ibc.core.connection.v1.Msg/ConnectionOpenAck',
                request_serializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenAck.SerializeToString,
                response_deserializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenAckResponse.FromString,
                )
        self.ConnectionOpenConfirm = channel.unary_unary(
                '/ibc.core.connection.v1.Msg/ConnectionOpenConfirm',
                request_serializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenConfirm.SerializeToString,
                response_deserializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenConfirmResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the ibc/connection Msg service.
    """

    def ConnectionOpenInit(self, request, context):
        """ConnectionOpenInit defines a rpc handler method for MsgConnectionOpenInit.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConnectionOpenTry(self, request, context):
        """ConnectionOpenTry defines a rpc handler method for MsgConnectionOpenTry.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConnectionOpenAck(self, request, context):
        """ConnectionOpenAck defines a rpc handler method for MsgConnectionOpenAck.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConnectionOpenConfirm(self, request, context):
        """ConnectionOpenConfirm defines a rpc handler method for MsgConnectionOpenConfirm.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ConnectionOpenInit': grpc.unary_unary_rpc_method_handler(
                    servicer.ConnectionOpenInit,
                    request_deserializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenInit.FromString,
                    response_serializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenInitResponse.SerializeToString,
            ),
            'ConnectionOpenTry': grpc.unary_unary_rpc_method_handler(
                    servicer.ConnectionOpenTry,
                    request_deserializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenTry.FromString,
                    response_serializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenTryResponse.SerializeToString,
            ),
            'ConnectionOpenAck': grpc.unary_unary_rpc_method_handler(
                    servicer.ConnectionOpenAck,
                    request_deserializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenAck.FromString,
                    response_serializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenAckResponse.SerializeToString,
            ),
            'ConnectionOpenConfirm': grpc.unary_unary_rpc_method_handler(
                    servicer.ConnectionOpenConfirm,
                    request_deserializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenConfirm.FromString,
                    response_serializer=ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenConfirmResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ibc.core.connection.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the ibc/connection Msg service.
    """

    @staticmethod
    def ConnectionOpenInit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.connection.v1.Msg/ConnectionOpenInit',
            ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenInit.SerializeToString,
            ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenInitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConnectionOpenTry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.connection.v1.Msg/ConnectionOpenTry',
            ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenTry.SerializeToString,
            ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenTryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConnectionOpenAck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.connection.v1.Msg/ConnectionOpenAck',
            ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenAck.SerializeToString,
            ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenAckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConnectionOpenConfirm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.connection.v1.Msg/ConnectionOpenConfirm',
            ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenConfirm.SerializeToString,
            ibc_dot_core_dot_connection_dot_v1_dot_tx__pb2.MsgConnectionOpenConfirmResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
