"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import lcmtypes.float_point_3d_t

class map_special_point_t(object):
    __slots__ = ["point", "index", "distance", "property"]

    def __init__(self):
        self.point = lcmtypes.float_point_3d_t()
        self.index = 0
        self.distance = 0.0
        self.property = 0

    def encode(self):
        buf = BytesIO()
        buf.write(map_special_point_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.point._get_packed_fingerprint() == lcmtypes.float_point_3d_t._get_packed_fingerprint()
        self.point._encode_one(buf)
        buf.write(struct.pack(">hfb", self.index, self.distance, self.property))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != map_special_point_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return map_special_point_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = map_special_point_t()
        self.point = lcmtypes.float_point_3d_t._decode_one(buf)
        self.index, self.distance, self.property = struct.unpack(">hfb", buf.read(7))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if map_special_point_t in parents: return 0
        newparents = parents + [map_special_point_t]
        tmphash = (0xa0f27f6b121c7393+ lcmtypes.float_point_3d_t._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if map_special_point_t._packed_fingerprint is None:
            map_special_point_t._packed_fingerprint = struct.pack(">Q", map_special_point_t._get_hash_recursive([]))
        return map_special_point_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

