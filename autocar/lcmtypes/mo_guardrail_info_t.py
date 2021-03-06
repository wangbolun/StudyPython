"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class mo_guardrail_info_t(object):
    __slots__ = ["bValid0", "RealPointXZ0", "Height0", "bValid1", "RealPointXZ1", "Height1"]

    def __init__(self):
        self.bValid0 = 0
        self.RealPointXZ0 = [ [ 0 for dim1 in range(2) ] for dim0 in range(2) ]
        self.Height0 = 0
        self.bValid1 = 0
        self.RealPointXZ1 = [ [ 0 for dim1 in range(2) ] for dim0 in range(2) ]
        self.Height1 = 0

    def encode(self):
        buf = BytesIO()
        buf.write(mo_guardrail_info_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">b", self.bValid0))
        for i0 in range(2):
            buf.write(struct.pack('>2h', *self.RealPointXZ0[i0][:2]))
        buf.write(struct.pack(">hb", self.Height0, self.bValid1))
        for i0 in range(2):
            buf.write(struct.pack('>2h', *self.RealPointXZ1[i0][:2]))
        buf.write(struct.pack(">h", self.Height1))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != mo_guardrail_info_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return mo_guardrail_info_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = mo_guardrail_info_t()
        self.bValid0 = struct.unpack(">b", buf.read(1))[0]
        self.RealPointXZ0 = []
        for i0 in range(2):
            self.RealPointXZ0.append(struct.unpack('>2h', buf.read(4)))
        self.Height0, self.bValid1 = struct.unpack(">hb", buf.read(3))
        self.RealPointXZ1 = []
        for i0 in range(2):
            self.RealPointXZ1.append(struct.unpack('>2h', buf.read(4)))
        self.Height1 = struct.unpack(">h", buf.read(2))[0]
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if mo_guardrail_info_t in parents: return 0
        tmphash = (0xb87dddc0f1d931e3) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if mo_guardrail_info_t._packed_fingerprint is None:
            mo_guardrail_info_t._packed_fingerprint = struct.pack(">Q", mo_guardrail_info_t._get_hash_recursive([]))
        return mo_guardrail_info_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

