"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import lcmtypes.map_point_t

class map_line_info_t(object):
    __slots__ = ["index", "pointCount", "points", "pointsProperty"]

    def __init__(self):
        self.index = 0
        self.pointCount = 0
        self.points = []
        self.pointsProperty = []

    def encode(self):
        buf = BytesIO()
        buf.write(map_line_info_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">bh", self.index, self.pointCount))
        for i0 in range(self.pointCount):
            assert self.points[i0]._get_packed_fingerprint() == lcmtypes.map_point_t._get_packed_fingerprint()
            self.points[i0]._encode_one(buf)
        buf.write(struct.pack('>%db' % self.pointCount, *self.pointsProperty[:self.pointCount]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != map_line_info_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return map_line_info_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = map_line_info_t()
        self.index, self.pointCount = struct.unpack(">bh", buf.read(3))
        self.points = []
        for i0 in range(self.pointCount):
            self.points.append(lcmtypes.map_point_t._decode_one(buf))
        self.pointsProperty = struct.unpack('>%db' % self.pointCount, buf.read(self.pointCount))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if map_line_info_t in parents: return 0
        newparents = parents + [map_line_info_t]
        tmphash = (0x342213a20fffebda+ lcmtypes.map_point_t._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if map_line_info_t._packed_fingerprint is None:
            map_line_info_t._packed_fingerprint = struct.pack(">Q", map_line_info_t._get_hash_recursive([]))
        return map_line_info_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
