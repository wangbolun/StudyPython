"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class mo_radarpoint_info_t(object):
    __slots__ = ["Distance", "Height", "Type"]

    def __init__(self):
        self.Distance = 0
        self.Height = 0
        self.Type = 0

    def encode(self):
        buf = BytesIO()
        buf.write(mo_radarpoint_info_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">hhb", self.Distance, self.Height, self.Type))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != mo_radarpoint_info_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return mo_radarpoint_info_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = mo_radarpoint_info_t()
        self.Distance, self.Height, self.Type = struct.unpack(">hhb", buf.read(5))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if mo_radarpoint_info_t in parents: return 0
        tmphash = (0x98e28a5d73b0a3b5) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if mo_radarpoint_info_t._packed_fingerprint is None:
            mo_radarpoint_info_t._packed_fingerprint = struct.pack(">Q", mo_radarpoint_info_t._get_hash_recursive([]))
        return mo_radarpoint_info_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
