"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import lcmtypes.key_point_t

import lcmtypes.object_outline_t

class moving_object_t(object):
    __slots__ = ["objectCenterPosition", "objectCenterSpeed", "objectOutline"]

    def __init__(self):
        self.objectCenterPosition = lcmtypes.key_point_t()
        self.objectCenterSpeed = lcmtypes.key_point_t()
        self.objectOutline = lcmtypes.object_outline_t()

    def encode(self):
        buf = BytesIO()
        buf.write(moving_object_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.objectCenterPosition._get_packed_fingerprint() == lcmtypes.key_point_t._get_packed_fingerprint()
        self.objectCenterPosition._encode_one(buf)
        assert self.objectCenterSpeed._get_packed_fingerprint() == lcmtypes.key_point_t._get_packed_fingerprint()
        self.objectCenterSpeed._encode_one(buf)
        assert self.objectOutline._get_packed_fingerprint() == lcmtypes.object_outline_t._get_packed_fingerprint()
        self.objectOutline._encode_one(buf)

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != moving_object_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return moving_object_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = moving_object_t()
        self.objectCenterPosition = lcmtypes.key_point_t._decode_one(buf)
        self.objectCenterSpeed = lcmtypes.key_point_t._decode_one(buf)
        self.objectOutline = lcmtypes.object_outline_t._decode_one(buf)
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if moving_object_t in parents: return 0
        newparents = parents + [moving_object_t]
        tmphash = (0x41b4e84902986fab+ lcmtypes.key_point_t._get_hash_recursive(newparents)+ lcmtypes.key_point_t._get_hash_recursive(newparents)+ lcmtypes.object_outline_t._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if moving_object_t._packed_fingerprint is None:
            moving_object_t._packed_fingerprint = struct.pack(">Q", moving_object_t._get_hash_recursive([]))
        return moving_object_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

