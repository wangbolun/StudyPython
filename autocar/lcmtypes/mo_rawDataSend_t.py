"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class mo_rawDataSend_t(object):
    __slots__ = ["MO_RawData"]

    def __init__(self):
        self.MO_RawData = ""

    def encode(self):
        buf = BytesIO()
        buf.write(mo_rawDataSend_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(bytearray(self.MO_RawData[:13312]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != mo_rawDataSend_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return mo_rawDataSend_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = mo_rawDataSend_t()
        self.MO_RawData = buf.read(13312)
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if mo_rawDataSend_t in parents: return 0
        tmphash = (0x12e304aa6b1926cd) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if mo_rawDataSend_t._packed_fingerprint is None:
            mo_rawDataSend_t._packed_fingerprint = struct.pack(">Q", mo_rawDataSend_t._get_hash_recursive([]))
        return mo_rawDataSend_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

