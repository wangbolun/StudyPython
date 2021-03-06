"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class mo_object_info_t(object):
    __slots__ = ["Id", "XOffset", "ZDistance", "Width", "Height", "SpeedX", "SpeedZ", "Type", "ControlPoints", "TTCtime"]

    def __init__(self):
        self.Id = 0
        self.XOffset = 0
        self.ZDistance = 0
        self.Width = 0
        self.Height = 0
        self.SpeedX = 0
        self.SpeedZ = 0
        self.Type = 0
        self.ControlPoints = [ [ 0 for dim1 in range(2) ] for dim0 in range(3) ]
        self.TTCtime = 0

    def encode(self):
        buf = BytesIO()
        buf.write(mo_object_info_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">ihhhhbbh", self.Id, self.XOffset, self.ZDistance, self.Width, self.Height, self.SpeedX, self.SpeedZ, self.Type))
        for i0 in range(3):
            buf.write(struct.pack('>2h', *self.ControlPoints[i0][:2]))
        buf.write(struct.pack(">b", self.TTCtime))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != mo_object_info_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return mo_object_info_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = mo_object_info_t()
        self.Id, self.XOffset, self.ZDistance, self.Width, self.Height, self.SpeedX, self.SpeedZ, self.Type = struct.unpack(">ihhhhbbh", buf.read(16))
        self.ControlPoints = []
        for i0 in range(3):
            self.ControlPoints.append(struct.unpack('>2h', buf.read(4)))
        self.TTCtime = struct.unpack(">b", buf.read(1))[0]
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if mo_object_info_t in parents: return 0
        tmphash = (0xf049e0bc337f5b39) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if mo_object_info_t._packed_fingerprint is None:
            mo_object_info_t._packed_fingerprint = struct.pack(">Q", mo_object_info_t._get_hash_recursive([]))
        return mo_object_info_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

