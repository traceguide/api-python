#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class KeyValue:
  """
  Attributes:
   - Key
   - Value
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'Key', None, None, ), # 1
    (2, TType.STRING, 'Value', None, None, ), # 2
  )

  def __init__(self, Key=None, Value=None,):
    self.Key = Key
    self.Value = Value

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.Key = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.Value = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('KeyValue')
    if self.Key is not None:
      oprot.writeFieldBegin('Key', TType.STRING, 1)
      oprot.writeString(self.Key)
      oprot.writeFieldEnd()
    if self.Value is not None:
      oprot.writeFieldBegin('Value', TType.STRING, 2)
      oprot.writeString(self.Value)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.Key is None:
      raise TProtocol.TProtocolException(message='Required field Key is unset!')
    if self.Value is None:
      raise TProtocol.TProtocolException(message='Required field Value is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.Key)
    value = (value * 31) ^ hash(self.Value)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Runtime:
  """
  Attributes:
   - guid
   - start_micros
   - group_name
   - attrs
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'guid', None, None, ), # 1
    (2, TType.I64, 'start_micros', None, None, ), # 2
    (3, TType.STRING, 'group_name', None, None, ), # 3
    (4, TType.LIST, 'attrs', (TType.STRUCT,(KeyValue, KeyValue.thrift_spec)), None, ), # 4
  )

  def __init__(self, guid=None, start_micros=None, group_name=None, attrs=None,):
    self.guid = guid
    self.start_micros = start_micros
    self.group_name = group_name
    self.attrs = attrs

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.guid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.start_micros = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.group_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.attrs = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = KeyValue()
            _elem5.read(iprot)
            self.attrs.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Runtime')
    if self.guid is not None:
      oprot.writeFieldBegin('guid', TType.STRING, 1)
      oprot.writeString(self.guid)
      oprot.writeFieldEnd()
    if self.start_micros is not None:
      oprot.writeFieldBegin('start_micros', TType.I64, 2)
      oprot.writeI64(self.start_micros)
      oprot.writeFieldEnd()
    if self.group_name is not None:
      oprot.writeFieldBegin('group_name', TType.STRING, 3)
      oprot.writeString(self.group_name)
      oprot.writeFieldEnd()
    if self.attrs is not None:
      oprot.writeFieldBegin('attrs', TType.LIST, 4)
      oprot.writeListBegin(TType.STRUCT, len(self.attrs))
      for iter6 in self.attrs:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.guid)
    value = (value * 31) ^ hash(self.start_micros)
    value = (value * 31) ^ hash(self.group_name)
    value = (value * 31) ^ hash(self.attrs)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class LogRecord:
  """
  Attributes:
   - timestamp_micros
   - runtime_guid
   - span_guid
   - stable_name
   - message
   - level
   - thread_id
   - filename
   - line_number
   - stack_frames
   - payload_json
   - error_flag
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'timestamp_micros', None, None, ), # 1
    (2, TType.STRING, 'runtime_guid', None, None, ), # 2
    (3, TType.STRING, 'span_guid', None, None, ), # 3
    (4, TType.STRING, 'stable_name', None, None, ), # 4
    (5, TType.STRING, 'message', None, None, ), # 5
    (6, TType.STRING, 'level', None, None, ), # 6
    (7, TType.I64, 'thread_id', None, None, ), # 7
    (8, TType.STRING, 'filename', None, None, ), # 8
    (9, TType.I64, 'line_number', None, None, ), # 9
    (10, TType.LIST, 'stack_frames', (TType.STRING,None), None, ), # 10
    (11, TType.STRING, 'payload_json', None, None, ), # 11
    (12, TType.BOOL, 'error_flag', None, None, ), # 12
  )

  def __init__(self, timestamp_micros=None, runtime_guid=None, span_guid=None, stable_name=None, message=None, level=None, thread_id=None, filename=None, line_number=None, stack_frames=None, payload_json=None, error_flag=None,):
    self.timestamp_micros = timestamp_micros
    self.runtime_guid = runtime_guid
    self.span_guid = span_guid
    self.stable_name = stable_name
    self.message = message
    self.level = level
    self.thread_id = thread_id
    self.filename = filename
    self.line_number = line_number
    self.stack_frames = stack_frames
    self.payload_json = payload_json
    self.error_flag = error_flag

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.timestamp_micros = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.runtime_guid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.span_guid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.stable_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.level = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.thread_id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.filename = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I64:
          self.line_number = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.LIST:
          self.stack_frames = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = iprot.readString();
            self.stack_frames.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.STRING:
          self.payload_json = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.BOOL:
          self.error_flag = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('LogRecord')
    if self.timestamp_micros is not None:
      oprot.writeFieldBegin('timestamp_micros', TType.I64, 1)
      oprot.writeI64(self.timestamp_micros)
      oprot.writeFieldEnd()
    if self.runtime_guid is not None:
      oprot.writeFieldBegin('runtime_guid', TType.STRING, 2)
      oprot.writeString(self.runtime_guid)
      oprot.writeFieldEnd()
    if self.span_guid is not None:
      oprot.writeFieldBegin('span_guid', TType.STRING, 3)
      oprot.writeString(self.span_guid)
      oprot.writeFieldEnd()
    if self.stable_name is not None:
      oprot.writeFieldBegin('stable_name', TType.STRING, 4)
      oprot.writeString(self.stable_name)
      oprot.writeFieldEnd()
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 5)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    if self.level is not None:
      oprot.writeFieldBegin('level', TType.STRING, 6)
      oprot.writeString(self.level)
      oprot.writeFieldEnd()
    if self.thread_id is not None:
      oprot.writeFieldBegin('thread_id', TType.I64, 7)
      oprot.writeI64(self.thread_id)
      oprot.writeFieldEnd()
    if self.filename is not None:
      oprot.writeFieldBegin('filename', TType.STRING, 8)
      oprot.writeString(self.filename)
      oprot.writeFieldEnd()
    if self.line_number is not None:
      oprot.writeFieldBegin('line_number', TType.I64, 9)
      oprot.writeI64(self.line_number)
      oprot.writeFieldEnd()
    if self.stack_frames is not None:
      oprot.writeFieldBegin('stack_frames', TType.LIST, 10)
      oprot.writeListBegin(TType.STRING, len(self.stack_frames))
      for iter13 in self.stack_frames:
        oprot.writeString(iter13)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.payload_json is not None:
      oprot.writeFieldBegin('payload_json', TType.STRING, 11)
      oprot.writeString(self.payload_json)
      oprot.writeFieldEnd()
    if self.error_flag is not None:
      oprot.writeFieldBegin('error_flag', TType.BOOL, 12)
      oprot.writeBool(self.error_flag)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.timestamp_micros)
    value = (value * 31) ^ hash(self.runtime_guid)
    value = (value * 31) ^ hash(self.span_guid)
    value = (value * 31) ^ hash(self.stable_name)
    value = (value * 31) ^ hash(self.message)
    value = (value * 31) ^ hash(self.level)
    value = (value * 31) ^ hash(self.thread_id)
    value = (value * 31) ^ hash(self.filename)
    value = (value * 31) ^ hash(self.line_number)
    value = (value * 31) ^ hash(self.stack_frames)
    value = (value * 31) ^ hash(self.payload_json)
    value = (value * 31) ^ hash(self.error_flag)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TraceJoinId:
  """
  Attributes:
   - TraceKey
   - Value
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'TraceKey', None, None, ), # 1
    (2, TType.STRING, 'Value', None, None, ), # 2
  )

  def __init__(self, TraceKey=None, Value=None,):
    self.TraceKey = TraceKey
    self.Value = Value

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.TraceKey = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.Value = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TraceJoinId')
    if self.TraceKey is not None:
      oprot.writeFieldBegin('TraceKey', TType.STRING, 1)
      oprot.writeString(self.TraceKey)
      oprot.writeFieldEnd()
    if self.Value is not None:
      oprot.writeFieldBegin('Value', TType.STRING, 2)
      oprot.writeString(self.Value)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.TraceKey is None:
      raise TProtocol.TProtocolException(message='Required field TraceKey is unset!')
    if self.Value is None:
      raise TProtocol.TProtocolException(message='Required field Value is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.TraceKey)
    value = (value * 31) ^ hash(self.Value)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class SpanRecord:
  """
  Attributes:
   - span_guid
   - runtime_guid
   - span_name
   - join_ids
   - oldest_micros
   - youngest_micros
   - attributes
   - deprecated_error_text
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'span_guid', None, None, ), # 1
    (2, TType.STRING, 'runtime_guid', None, None, ), # 2
    (3, TType.STRING, 'span_name', None, None, ), # 3
    (4, TType.LIST, 'join_ids', (TType.STRUCT,(TraceJoinId, TraceJoinId.thrift_spec)), None, ), # 4
    (5, TType.I64, 'oldest_micros', None, None, ), # 5
    (6, TType.I64, 'youngest_micros', None, None, ), # 6
    (7, TType.STRING, 'deprecated_error_text', None, None, ), # 7
    (8, TType.LIST, 'attributes', (TType.STRUCT,(KeyValue, KeyValue.thrift_spec)), None, ), # 8
  )

  def __init__(self, span_guid=None, runtime_guid=None, span_name=None, join_ids=None, oldest_micros=None, youngest_micros=None, attributes=None, deprecated_error_text=None,):
    self.span_guid = span_guid
    self.runtime_guid = runtime_guid
    self.span_name = span_name
    self.join_ids = join_ids
    self.oldest_micros = oldest_micros
    self.youngest_micros = youngest_micros
    self.attributes = attributes
    self.deprecated_error_text = deprecated_error_text

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.span_guid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.runtime_guid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.span_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.join_ids = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = TraceJoinId()
            _elem19.read(iprot)
            self.join_ids.append(_elem19)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.oldest_micros = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I64:
          self.youngest_micros = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.LIST:
          self.attributes = []
          (_etype23, _size20) = iprot.readListBegin()
          for _i24 in xrange(_size20):
            _elem25 = KeyValue()
            _elem25.read(iprot)
            self.attributes.append(_elem25)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.deprecated_error_text = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SpanRecord')
    if self.span_guid is not None:
      oprot.writeFieldBegin('span_guid', TType.STRING, 1)
      oprot.writeString(self.span_guid)
      oprot.writeFieldEnd()
    if self.runtime_guid is not None:
      oprot.writeFieldBegin('runtime_guid', TType.STRING, 2)
      oprot.writeString(self.runtime_guid)
      oprot.writeFieldEnd()
    if self.span_name is not None:
      oprot.writeFieldBegin('span_name', TType.STRING, 3)
      oprot.writeString(self.span_name)
      oprot.writeFieldEnd()
    if self.join_ids is not None:
      oprot.writeFieldBegin('join_ids', TType.LIST, 4)
      oprot.writeListBegin(TType.STRUCT, len(self.join_ids))
      for iter26 in self.join_ids:
        iter26.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.oldest_micros is not None:
      oprot.writeFieldBegin('oldest_micros', TType.I64, 5)
      oprot.writeI64(self.oldest_micros)
      oprot.writeFieldEnd()
    if self.youngest_micros is not None:
      oprot.writeFieldBegin('youngest_micros', TType.I64, 6)
      oprot.writeI64(self.youngest_micros)
      oprot.writeFieldEnd()
    if self.deprecated_error_text is not None:
      oprot.writeFieldBegin('deprecated_error_text', TType.STRING, 7)
      oprot.writeString(self.deprecated_error_text)
      oprot.writeFieldEnd()
    if self.attributes is not None:
      oprot.writeFieldBegin('attributes', TType.LIST, 8)
      oprot.writeListBegin(TType.STRUCT, len(self.attributes))
      for iter27 in self.attributes:
        iter27.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.span_guid)
    value = (value * 31) ^ hash(self.runtime_guid)
    value = (value * 31) ^ hash(self.span_name)
    value = (value * 31) ^ hash(self.join_ids)
    value = (value * 31) ^ hash(self.oldest_micros)
    value = (value * 31) ^ hash(self.youngest_micros)
    value = (value * 31) ^ hash(self.attributes)
    value = (value * 31) ^ hash(self.deprecated_error_text)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Auth:
  """
  Attributes:
   - access_token
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'access_token', None, None, ), # 1
  )

  def __init__(self, access_token=None,):
    self.access_token = access_token

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.access_token = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Auth')
    if self.access_token is not None:
      oprot.writeFieldBegin('access_token', TType.STRING, 1)
      oprot.writeString(self.access_token)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.access_token)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Timing:
  """
  Attributes:
   - receive_micros
   - transmit_micros
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'receive_micros', None, None, ), # 1
    (2, TType.I64, 'transmit_micros', None, None, ), # 2
  )

  def __init__(self, receive_micros=None, transmit_micros=None,):
    self.receive_micros = receive_micros
    self.transmit_micros = transmit_micros

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.receive_micros = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.transmit_micros = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Timing')
    if self.receive_micros is not None:
      oprot.writeFieldBegin('receive_micros', TType.I64, 1)
      oprot.writeI64(self.receive_micros)
      oprot.writeFieldEnd()
    if self.transmit_micros is not None:
      oprot.writeFieldBegin('transmit_micros', TType.I64, 2)
      oprot.writeI64(self.transmit_micros)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.receive_micros)
    value = (value * 31) ^ hash(self.transmit_micros)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class SampleCount:
  """
  Attributes:
   - oldest_micros
   - youngest_micros
   - count
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'oldest_micros', None, None, ), # 1
    (2, TType.I64, 'youngest_micros', None, None, ), # 2
    (3, TType.I64, 'count', None, None, ), # 3
  )

  def __init__(self, oldest_micros=None, youngest_micros=None, count=None,):
    self.oldest_micros = oldest_micros
    self.youngest_micros = youngest_micros
    self.count = count

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.oldest_micros = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.youngest_micros = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.count = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SampleCount')
    if self.oldest_micros is not None:
      oprot.writeFieldBegin('oldest_micros', TType.I64, 1)
      oprot.writeI64(self.oldest_micros)
      oprot.writeFieldEnd()
    if self.youngest_micros is not None:
      oprot.writeFieldBegin('youngest_micros', TType.I64, 2)
      oprot.writeI64(self.youngest_micros)
      oprot.writeFieldEnd()
    if self.count is not None:
      oprot.writeFieldBegin('count', TType.I64, 3)
      oprot.writeI64(self.count)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.oldest_micros)
    value = (value * 31) ^ hash(self.youngest_micros)
    value = (value * 31) ^ hash(self.count)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ReportRequest:
  """
  Attributes:
   - runtime
   - span_records
   - log_records
   - timestamp_offset_micros
   - discarded_log_record_samples
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'runtime', (Runtime, Runtime.thrift_spec), None, ), # 1
    None, # 2
    (3, TType.LIST, 'span_records', (TType.STRUCT,(SpanRecord, SpanRecord.thrift_spec)), None, ), # 3
    (4, TType.LIST, 'log_records', (TType.STRUCT,(LogRecord, LogRecord.thrift_spec)), None, ), # 4
    (5, TType.I64, 'timestamp_offset_micros', None, None, ), # 5
    (6, TType.LIST, 'discarded_log_record_samples', (TType.STRUCT,(SampleCount, SampleCount.thrift_spec)), None, ), # 6
  )

  def __init__(self, runtime=None, span_records=None, log_records=None, timestamp_offset_micros=None, discarded_log_record_samples=None,):
    self.runtime = runtime
    self.span_records = span_records
    self.log_records = log_records
    self.timestamp_offset_micros = timestamp_offset_micros
    self.discarded_log_record_samples = discarded_log_record_samples

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.runtime = Runtime()
          self.runtime.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.span_records = []
          (_etype31, _size28) = iprot.readListBegin()
          for _i32 in xrange(_size28):
            _elem33 = SpanRecord()
            _elem33.read(iprot)
            self.span_records.append(_elem33)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.log_records = []
          (_etype37, _size34) = iprot.readListBegin()
          for _i38 in xrange(_size34):
            _elem39 = LogRecord()
            _elem39.read(iprot)
            self.log_records.append(_elem39)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.timestamp_offset_micros = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.discarded_log_record_samples = []
          (_etype43, _size40) = iprot.readListBegin()
          for _i44 in xrange(_size40):
            _elem45 = SampleCount()
            _elem45.read(iprot)
            self.discarded_log_record_samples.append(_elem45)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ReportRequest')
    if self.runtime is not None:
      oprot.writeFieldBegin('runtime', TType.STRUCT, 1)
      self.runtime.write(oprot)
      oprot.writeFieldEnd()
    if self.span_records is not None:
      oprot.writeFieldBegin('span_records', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.span_records))
      for iter46 in self.span_records:
        iter46.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.log_records is not None:
      oprot.writeFieldBegin('log_records', TType.LIST, 4)
      oprot.writeListBegin(TType.STRUCT, len(self.log_records))
      for iter47 in self.log_records:
        iter47.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.timestamp_offset_micros is not None:
      oprot.writeFieldBegin('timestamp_offset_micros', TType.I64, 5)
      oprot.writeI64(self.timestamp_offset_micros)
      oprot.writeFieldEnd()
    if self.discarded_log_record_samples is not None:
      oprot.writeFieldBegin('discarded_log_record_samples', TType.LIST, 6)
      oprot.writeListBegin(TType.STRUCT, len(self.discarded_log_record_samples))
      for iter48 in self.discarded_log_record_samples:
        iter48.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.runtime)
    value = (value * 31) ^ hash(self.span_records)
    value = (value * 31) ^ hash(self.log_records)
    value = (value * 31) ^ hash(self.timestamp_offset_micros)
    value = (value * 31) ^ hash(self.discarded_log_record_samples)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Command:
  """
  Attributes:
   - disable
  """

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'disable', None, None, ), # 1
  )

  def __init__(self, disable=None,):
    self.disable = disable

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.BOOL:
          self.disable = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Command')
    if self.disable is not None:
      oprot.writeFieldBegin('disable', TType.BOOL, 1)
      oprot.writeBool(self.disable)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.disable)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ReportResponse:
  """
  Attributes:
   - commands
   - timing
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'commands', (TType.STRUCT,(Command, Command.thrift_spec)), None, ), # 1
    (2, TType.STRUCT, 'timing', (Timing, Timing.thrift_spec), None, ), # 2
  )

  def __init__(self, commands=None, timing=None,):
    self.commands = commands
    self.timing = timing

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.commands = []
          (_etype52, _size49) = iprot.readListBegin()
          for _i53 in xrange(_size49):
            _elem54 = Command()
            _elem54.read(iprot)
            self.commands.append(_elem54)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.timing = Timing()
          self.timing.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ReportResponse')
    if self.commands is not None:
      oprot.writeFieldBegin('commands', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.commands))
      for iter55 in self.commands:
        iter55.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.timing is not None:
      oprot.writeFieldBegin('timing', TType.STRUCT, 2)
      self.timing.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.commands)
    value = (value * 31) ^ hash(self.timing)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
