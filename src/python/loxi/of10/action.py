# Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University
# Copyright (c) 2011, 2012 Open Networking Foundation
# Copyright (c) 2012, 2013 Big Switch Networks, Inc.

# Automatically generated by LOXI from template action.py
# Do not modify

import struct
import const
import util
import loxi.generic_util
import loxi

def unpack_list(reader):
    def deserializer(reader, typ):
        parser = parsers.get(typ)
        if not parser: raise loxi.ProtocolError("unknown action type %d" % typ)
        return parser(reader)
    return loxi.generic_util.unpack_list_tlv16(reader, deserializer)

class Action(object):
    type = None # override in subclass
    pass

class bsn_mirror(Action):
    type = const.OFPAT_VENDOR
    experimenter = 0x5c16c7
    subtype = 1

    def __init__(self, dest_port=None, vlan_tag=None, copy_stage=None):
        if dest_port != None:
            self.dest_port = dest_port
        else:
            self.dest_port = 0
        if vlan_tag != None:
            self.vlan_tag = vlan_tag
        else:
            self.vlan_tag = 0
        if copy_stage != None:
            self.copy_stage = copy_stage
        else:
            self.copy_stage = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        packed.append(struct.pack("!L", self.dest_port))
        packed.append(struct.pack("!L", self.vlan_tag))
        packed.append(struct.pack("!B", self.copy_stage))
        packed.append('\x00' * 3)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = bsn_mirror()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPAT_VENDOR)
        _len = reader.read('!H')[0]
        _experimenter = reader.read('!L')[0]
        assert(_experimenter == 0x5c16c7)
        _subtype = reader.read('!L')[0]
        assert(_subtype == 1)
        obj.dest_port = reader.read('!L')[0]
        obj.vlan_tag = reader.read('!L')[0]
        obj.copy_stage = reader.read('!B')[0]
        reader.skip(3)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.dest_port != other.dest_port: return False
        if self.vlan_tag != other.vlan_tag: return False
        if self.copy_stage != other.copy_stage: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("bsn_mirror {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("dest_port = ");
                q.text("%#x" % self.dest_port)
                q.text(","); q.breakable()
                q.text("vlan_tag = ");
                q.text("%#x" % self.vlan_tag)
                q.text(","); q.breakable()
                q.text("copy_stage = ");
                q.text("%#x" % self.copy_stage)
            q.breakable()
        q.text('}')

class bsn_set_tunnel_dst(Action):
    type = const.OFPAT_VENDOR
    experimenter = 0x5c16c7
    subtype = 2

    def __init__(self, dst=None):
        if dst != None:
            self.dst = dst
        else:
            self.dst = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        packed.append(struct.pack("!L", self.dst))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = bsn_set_tunnel_dst()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPAT_VENDOR)
        _len = reader.read('!H')[0]
        _experimenter = reader.read('!L')[0]
        assert(_experimenter == 0x5c16c7)
        _subtype = reader.read('!L')[0]
        assert(_subtype == 2)
        obj.dst = reader.read('!L')[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.dst != other.dst: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("bsn_set_tunnel_dst {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("dst = ");
                q.text("%#x" % self.dst)
            q.breakable()
        q.text('}')

class enqueue(Action):
    type = const.OFPAT_ENQUEUE

    def __init__(self, port=None, queue_id=None):
        if port != None:
            self.port = port
        else:
            self.port = 0
        if queue_id != None:
            self.queue_id = queue_id
        else:
            self.queue_id = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!H", self.port))
        packed.append('\x00' * 6)
        packed.append(struct.pack("!L", self.queue_id))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = enqueue()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPAT_ENQUEUE)
        _len = reader.read('!H')[0]
        obj.port = reader.read('!H')[0]
        reader.skip(6)
        obj.queue_id = reader.read('!L')[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.port != other.port: return False
        if self.queue_id != other.queue_id: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("enqueue {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("port = ");
                q.text(util.pretty_port(self.port))
                q.text(","); q.breakable()
                q.text("queue_id = ");
                q.text("%#x" % self.queue_id)
            q.breakable()
        q.text('}')

class nicira_dec_ttl(Action):
    type = const.OFPAT_VENDOR
    experimenter = 0x2320
    subtype = 18

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!H", self.subtype))
        packed.append('\x00' * 2)
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = nicira_dec_ttl()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPAT_VENDOR)
        _len = reader.read('!H')[0]
        _experimenter = reader.read('!L')[0]
        assert(_experimenter == 0x2320)
        _subtype = reader.read('!H')[0]
        assert(_subtype == 18)
        reader.skip(2)
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("nicira_dec_ttl {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

class output(Action):
    type = const.OFPAT_OUTPUT

    def __init__(self, port=None, max_len=None):
        if port != None:
            self.port = port
        else:
            self.port = 0
        if max_len != None:
            self.max_len = max_len
        else:
            self.max_len = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!H", self.port))
        packed.append(struct.pack("!H", self.max_len))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = output()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPAT_OUTPUT)
        _len = reader.read('!H')[0]
        obj.port = reader.read('!H')[0]
        obj.max_len = reader.read('!H')[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.port != other.port: return False
        if self.max_len != other.max_len: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("output {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("port = ");
                q.text(util.pretty_port(self.port))
                q.text(","); q.breakable()
                q.text("max_len = ");
                q.text("%#x" % self.max_len)
            q.breakable()
        q.text('}')

class set_dl_dst(Action):
    type = const.OFPAT_SET_DL_DST

    def __init__(self, dl_addr=None):
        if dl_addr != None:
            self.dl_addr = dl_addr
        else:
            self.dl_addr = [0,0,0,0,0,0]
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!6B", *self.dl_addr))
        packed.append('\x00' * 6)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = set_dl_dst()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPAT_SET_DL_DST)
        _len = reader.read('!H')[0]
        obj.dl_addr = list(reader.read('!6B'))
        reader.skip(6)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.dl_addr != other.dl_addr: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("set_dl_dst {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("dl_addr = ");
                q.text(util.pretty_mac(self.dl_addr))
            q.breakable()
        q.text('}')

class set_dl_src(Action):
    type = const.OFPAT_SET_DL_SRC

    def __init__(self, dl_addr=None):
        if dl_addr != None:
            self.dl_addr = dl_addr
        else:
            self.dl_addr = [0,0,0,0,0,0]
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!6B", *self.dl_addr))
        packed.append('\x00' * 6)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = set_dl_src()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPAT_SET_DL_SRC)
        _len = reader.read('!H')[0]
        obj.dl_addr = list(reader.read('!6B'))
        reader.skip(6)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.dl_addr != other.dl_addr: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("set_dl_src {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("dl_addr = ");
                q.text(util.pretty_mac(self.dl_addr))
            q.breakable()
        q.text('}')

class set_nw_dst(Action):
    type = const.OFPAT_SET_NW_DST

    def __init__(self, nw_addr=None):
        if nw_addr != None:
            self.nw_addr = nw_addr
        else:
            self.nw_addr = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.nw_addr))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = set_nw_dst()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPAT_SET_NW_DST)
        _len = reader.read('!H')[0]
        obj.nw_addr = reader.read('!L')[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.nw_addr != other.nw_addr: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("set_nw_dst {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("nw_addr = ");
                q.text("%#x" % self.nw_addr)
            q.breakable()
        q.text('}')

class set_nw_src(Action):
    type = const.OFPAT_SET_NW_SRC

    def __init__(self, nw_addr=None):
        if nw_addr != None:
            self.nw_addr = nw_addr
        else:
            self.nw_addr = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.nw_addr))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = set_nw_src()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPAT_SET_NW_SRC)
        _len = reader.read('!H')[0]
        obj.nw_addr = reader.read('!L')[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.nw_addr != other.nw_addr: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("set_nw_src {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("nw_addr = ");
                q.text("%#x" % self.nw_addr)
            q.breakable()
        q.text('}')

class set_nw_tos(Action):
    type = const.OFPAT_SET_NW_TOS

    def __init__(self, nw_tos=None):
        if nw_tos != None:
            self.nw_tos = nw_tos
        else:
            self.nw_tos = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!B", self.nw_tos))
        packed.append('\x00' * 3)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = set_nw_tos()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPAT_SET_NW_TOS)
        _len = reader.read('!H')[0]
        obj.nw_tos = reader.read('!B')[0]
        reader.skip(3)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.nw_tos != other.nw_tos: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("set_nw_tos {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("nw_tos = ");
                q.text("%#x" % self.nw_tos)
            q.breakable()
        q.text('}')

class set_tp_dst(Action):
    type = const.OFPAT_SET_TP_DST

    def __init__(self, tp_port=None):
        if tp_port != None:
            self.tp_port = tp_port
        else:
            self.tp_port = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!H", self.tp_port))
        packed.append('\x00' * 2)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = set_tp_dst()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPAT_SET_TP_DST)
        _len = reader.read('!H')[0]
        obj.tp_port = reader.read('!H')[0]
        reader.skip(2)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.tp_port != other.tp_port: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("set_tp_dst {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("tp_port = ");
                q.text("%#x" % self.tp_port)
            q.breakable()
        q.text('}')

class set_tp_src(Action):
    type = const.OFPAT_SET_TP_SRC

    def __init__(self, tp_port=None):
        if tp_port != None:
            self.tp_port = tp_port
        else:
            self.tp_port = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!H", self.tp_port))
        packed.append('\x00' * 2)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = set_tp_src()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPAT_SET_TP_SRC)
        _len = reader.read('!H')[0]
        obj.tp_port = reader.read('!H')[0]
        reader.skip(2)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.tp_port != other.tp_port: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("set_tp_src {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("tp_port = ");
                q.text("%#x" % self.tp_port)
            q.breakable()
        q.text('}')

class set_vlan_pcp(Action):
    type = const.OFPAT_SET_VLAN_PCP

    def __init__(self, vlan_pcp=None):
        if vlan_pcp != None:
            self.vlan_pcp = vlan_pcp
        else:
            self.vlan_pcp = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!B", self.vlan_pcp))
        packed.append('\x00' * 3)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = set_vlan_pcp()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPAT_SET_VLAN_PCP)
        _len = reader.read('!H')[0]
        obj.vlan_pcp = reader.read('!B')[0]
        reader.skip(3)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.vlan_pcp != other.vlan_pcp: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("set_vlan_pcp {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("vlan_pcp = ");
                q.text("%#x" % self.vlan_pcp)
            q.breakable()
        q.text('}')

class set_vlan_vid(Action):
    type = const.OFPAT_SET_VLAN_VID

    def __init__(self, vlan_vid=None):
        if vlan_vid != None:
            self.vlan_vid = vlan_vid
        else:
            self.vlan_vid = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!H", self.vlan_vid))
        packed.append('\x00' * 2)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = set_vlan_vid()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPAT_SET_VLAN_VID)
        _len = reader.read('!H')[0]
        obj.vlan_vid = reader.read('!H')[0]
        reader.skip(2)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.vlan_vid != other.vlan_vid: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("set_vlan_vid {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("vlan_vid = ");
                q.text("%#x" % self.vlan_vid)
            q.breakable()
        q.text('}')

class strip_vlan(Action):
    type = const.OFPAT_STRIP_VLAN

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = strip_vlan()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPAT_STRIP_VLAN)
        _len = reader.read('!H')[0]
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("strip_vlan {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')


def parse_vendor(reader):

    experimenter, = reader.peek("!4xL")
    if experimenter == 0x005c16c7: # Big Switch Networks
        subtype, = reader.peek("!8xL")
    elif experimenter == 0x00002320: # Nicira
        subtype, = reader.peek("!8xH")
    else:
        raise loxi.ProtocolError("unexpected experimenter id %#x" % experimenter)

    if subtype in experimenter_parsers[experimenter]:
        return experimenter_parsers[experimenter][subtype](reader)
    else:
        raise loxi.ProtocolError("unexpected BSN experimenter subtype %#x" % subtype)

parsers = {
    const.OFPAT_ENQUEUE : enqueue.unpack,
    const.OFPAT_OUTPUT : output.unpack,
    const.OFPAT_SET_DL_DST : set_dl_dst.unpack,
    const.OFPAT_SET_DL_SRC : set_dl_src.unpack,
    const.OFPAT_SET_NW_DST : set_nw_dst.unpack,
    const.OFPAT_SET_NW_SRC : set_nw_src.unpack,
    const.OFPAT_SET_NW_TOS : set_nw_tos.unpack,
    const.OFPAT_SET_TP_DST : set_tp_dst.unpack,
    const.OFPAT_SET_TP_SRC : set_tp_src.unpack,
    const.OFPAT_SET_VLAN_PCP : set_vlan_pcp.unpack,
    const.OFPAT_SET_VLAN_VID : set_vlan_vid.unpack,
    const.OFPAT_STRIP_VLAN : strip_vlan.unpack,
    const.OFPAT_VENDOR : parse_vendor,
}

experimenter_parsers = {
    0x2320 : {
        18: nicira_dec_ttl.unpack,
    },
    0x5c16c7 : {
        1: bsn_mirror.unpack,
        2: bsn_set_tunnel_dst.unpack,
    },
}
