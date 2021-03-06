"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import lcmtypes.lidar_line_info_t

class road_boundary_t(object):
    __slots__ = ["utime", "leftRoadBoundary", "rightRoadBoundary"]

    def __init__(self):
        self.utime = 0
        self.leftRoadBoundary = lcmtypes.lidar_line_info_t()
        self.rightRoadBoundary = lcmtypes.lidar_line_info_t()

    def encode(self):
        buf = BytesIO()
        buf.write(road_boundary_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.utime))
        assert self.leftRoadBoundary._get_packed_fingerprint() == lcmtypes.lidar_line_info_t._get_packed_fingerprint()
        self.leftRoadBoundary._encode_one(buf)
        assert self.rightRoadBoundary._get_packed_fingerprint() == lcmtypes.lidar_line_info_t._get_packed_fingerprint()
        self.rightRoadBoundary._encode_one(buf)

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != road_boundary_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return road_boundary_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = road_boundary_t()
        self.utime = struct.unpack(">q", buf.read(8))[0]
        self.leftRoadBoundary = lcmtypes.lidar_line_info_t._decode_one(buf)
        self.rightRoadBoundary = lcmtypes.lidar_line_info_t._decode_one(buf)
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if road_boundary_t in parents: return 0
        newparents = parents + [road_boundary_t]
        tmphash = (0xcbb873f4385b80ef+ lcmtypes.lidar_line_info_t._get_hash_recursive(newparents)+ lcmtypes.lidar_line_info_t._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if road_boundary_t._packed_fingerprint is None:
            road_boundary_t._packed_fingerprint = struct.pack(">Q", road_boundary_t._get_hash_recursive([]))
        return road_boundary_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

