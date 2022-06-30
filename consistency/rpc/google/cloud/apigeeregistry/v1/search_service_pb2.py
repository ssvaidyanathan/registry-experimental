# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/apigeeregistry/v1/search_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/apigeeregistry/v1/search_service.proto\x12\x1egoogle.cloud.apigeeregistry.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a#google/longrunning/operations.proto\"%\n\x0cIndexRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"0\n\rIndexResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x0f\n\rIndexMetadata\"E\n\x0cQueryRequest\x12\x0e\n\x01q\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"\xa8\x01\n\rQueryResponse\x12\x45\n\x07results\x18\x01 \x03(\x0b\x32\x34.google.cloud.apigeeregistry.v1.QueryResponse.Result\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x1a&\n\x06Result\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0f\n\x07\x65xcerpt\x18\x02 \x01(\t2\xaf\x02\n\x06Search\x12\x88\x01\n\x05Index\x12,.google.cloud.apigeeregistry.v1.IndexRequest\x1a\x1d.google.longrunning.Operation\"2\x82\xd3\xe4\x93\x02\x0b\"\t/v1/index\xca\x41\x1e\n\rIndexResponse\x12\rIndexMetadata\x12x\n\x05Query\x12,.google.cloud.apigeeregistry.v1.QueryRequest\x1a-.google.cloud.apigeeregistry.v1.QueryResponse\"\x12\x82\xd3\xe4\x93\x02\x0c\x12\n/v1/search\x1a \xca\x41\x1d\x61pigeeregistry.googleapis.comBk\n\"com.google.cloud.apigeeregistry.v1B\x12SearchServiceProtoP\x01Z/github.com/apigee/registry-experimental/rpc;rpcb\x06proto3')



_INDEXREQUEST = DESCRIPTOR.message_types_by_name['IndexRequest']
_INDEXRESPONSE = DESCRIPTOR.message_types_by_name['IndexResponse']
_INDEXMETADATA = DESCRIPTOR.message_types_by_name['IndexMetadata']
_QUERYREQUEST = DESCRIPTOR.message_types_by_name['QueryRequest']
_QUERYRESPONSE = DESCRIPTOR.message_types_by_name['QueryResponse']
_QUERYRESPONSE_RESULT = _QUERYRESPONSE.nested_types_by_name['Result']
IndexRequest = _reflection.GeneratedProtocolMessageType('IndexRequest', (_message.Message,), {
  'DESCRIPTOR' : _INDEXREQUEST,
  '__module__' : 'google.cloud.apigeeregistry.v1.search_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.apigeeregistry.v1.IndexRequest)
  })
_sym_db.RegisterMessage(IndexRequest)

IndexResponse = _reflection.GeneratedProtocolMessageType('IndexResponse', (_message.Message,), {
  'DESCRIPTOR' : _INDEXRESPONSE,
  '__module__' : 'google.cloud.apigeeregistry.v1.search_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.apigeeregistry.v1.IndexResponse)
  })
_sym_db.RegisterMessage(IndexResponse)

IndexMetadata = _reflection.GeneratedProtocolMessageType('IndexMetadata', (_message.Message,), {
  'DESCRIPTOR' : _INDEXMETADATA,
  '__module__' : 'google.cloud.apigeeregistry.v1.search_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.apigeeregistry.v1.IndexMetadata)
  })
_sym_db.RegisterMessage(IndexMetadata)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREQUEST,
  '__module__' : 'google.cloud.apigeeregistry.v1.search_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.apigeeregistry.v1.QueryRequest)
  })
_sym_db.RegisterMessage(QueryRequest)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), {

  'Result' : _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
    'DESCRIPTOR' : _QUERYRESPONSE_RESULT,
    '__module__' : 'google.cloud.apigeeregistry.v1.search_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.apigeeregistry.v1.QueryResponse.Result)
    })
  ,
  'DESCRIPTOR' : _QUERYRESPONSE,
  '__module__' : 'google.cloud.apigeeregistry.v1.search_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.apigeeregistry.v1.QueryResponse)
  })
_sym_db.RegisterMessage(QueryResponse)
_sym_db.RegisterMessage(QueryResponse.Result)

_SEARCH = DESCRIPTOR.services_by_name['Search']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.cloud.apigeeregistry.v1B\022SearchServiceProtoP\001Z/github.com/apigee/registry-experimental/rpc;rpc'
  _QUERYREQUEST.fields_by_name['q']._options = None
  _QUERYREQUEST.fields_by_name['q']._serialized_options = b'\340A\002'
  _SEARCH._options = None
  _SEARCH._serialized_options = b'\312A\035apigeeregistry.googleapis.com'
  _SEARCH.methods_by_name['Index']._options = None
  _SEARCH.methods_by_name['Index']._serialized_options = b'\202\323\344\223\002\013\"\t/v1/index\312A\036\n\rIndexResponse\022\rIndexMetadata'
  _SEARCH.methods_by_name['Query']._options = None
  _SEARCH.methods_by_name['Query']._serialized_options = b'\202\323\344\223\002\014\022\n/v1/search'
  _INDEXREQUEST._serialized_start=212
  _INDEXREQUEST._serialized_end=249
  _INDEXRESPONSE._serialized_start=251
  _INDEXRESPONSE._serialized_end=299
  _INDEXMETADATA._serialized_start=301
  _INDEXMETADATA._serialized_end=316
  _QUERYREQUEST._serialized_start=318
  _QUERYREQUEST._serialized_end=387
  _QUERYRESPONSE._serialized_start=390
  _QUERYRESPONSE._serialized_end=558
  _QUERYRESPONSE_RESULT._serialized_start=520
  _QUERYRESPONSE_RESULT._serialized_end=558
  _SEARCH._serialized_start=561
  _SEARCH._serialized_end=864
# @@protoc_insertion_point(module_scope)
