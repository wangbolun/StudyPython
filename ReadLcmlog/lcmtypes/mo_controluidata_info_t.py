"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class mo_controluidata_info_t(object):
    __slots__ = ["FrontObjectDistance", "TTC", "LeftLaneDistance", "RightLaneDistance", "FrontObjectDistanceVisionSignal", "FrontObjectType", "FrontObjectDistanceAudioSignal", "TTCSignal", "LeftLaneDepartSignal", "RightLaneDepartSignal", "FrontObjectIdx", "LeftLaneIdx", "RightLaneIdx"]

    def __init__(self):
        self.FrontObjectDistance = 0
        self.TTC = 0
        self.LeftLaneDistance = 0
        self.RightLaneDistance = 0
        self.FrontObjectDistanceVisionSignal = 0
        self.FrontObjectType = 0
        self.FrontObjectDistanceAudioSignal = 0
        self.TTCSignal = 0
        self.LeftLaneDepartSignal = 0
        self.RightLaneDepartSignal = 0
        self.FrontObjectIdx = 0
        self.LeftLaneIdx = 0
        self.RightLaneIdx = 0

    def encode(self):
        buf = BytesIO()
        buf.write(mo_controluidata_info_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">iiiiiiiiiiiii", self.FrontObjectDistance, self.TTC, self.LeftLaneDistance, self.RightLaneDistance, self.FrontObjectDistanceVisionSignal, self.FrontObjectType, self.FrontObjectDistanceAudioSignal, self.TTCSignal, self.LeftLaneDepartSignal, self.RightLaneDepartSignal, self.FrontObjectIdx, self.LeftLaneIdx, self.RightLaneIdx))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != mo_controluidata_info_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return mo_controluidata_info_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = mo_controluidata_info_t()
        self.FrontObjectDistance, self.TTC, self.LeftLaneDistance, self.RightLaneDistance, self.FrontObjectDistanceVisionSignal, self.FrontObjectType, self.FrontObjectDistanceAudioSignal, self.TTCSignal, self.LeftLaneDepartSignal, self.RightLaneDepartSignal, self.FrontObjectIdx, self.LeftLaneIdx, self.RightLaneIdx = struct.unpack(">iiiiiiiiiiiii", buf.read(52))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if mo_controluidata_info_t in parents: return 0
        tmphash = (0x5b24934159e0b926) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if mo_controluidata_info_t._packed_fingerprint is None:
            mo_controluidata_info_t._packed_fingerprint = struct.pack(">Q", mo_controluidata_info_t._get_hash_recursive([]))
        return mo_controluidata_info_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

