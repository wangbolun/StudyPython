"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class speed_cmd_t(object):
    __slots__ = ["utime", "aim_spe", "mode", "t"]

    def __init__(self):
        self.utime = 0
        self.aim_spe = 0.0
        self.mode = 0
        self.t = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(speed_cmd_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qfif", self.utime, self.aim_spe, self.mode, self.t))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != speed_cmd_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return speed_cmd_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = speed_cmd_t()
        self.utime, self.aim_spe, self.mode, self.t = struct.unpack(">qfif", buf.read(20))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if speed_cmd_t in parents: return 0
        tmphash = (0x588bccc31c07b8dc) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if speed_cmd_t._packed_fingerprint is None:
            speed_cmd_t._packed_fingerprint = struct.pack(">Q", speed_cmd_t._get_hash_recursive([]))
        return speed_cmd_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

