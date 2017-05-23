# -*- coding: utf-8 -*-
# S E Z A R (1);
# [ Copyright Dev-TALENT (C) All rights reserved 2015 - 2017 ]

# -( imports )-
import struct

class bytearray:
	def __init__(self, bytes=b''):
		self.strbytes+=bytes

	def writeByte(self, value):
		self.bytes+=struct.pack('!b', int(value))
		return self

	def wrietUnsignedByte(self,value):
		self.bytes+=struct.pack('!B', int(value))
		return self

	def writeInt(self, value):
		self.bytes+=struct.pack('!i', int(value))
		return self

	def writeUnsignedInt(self, value):
		self.bytes+=struct.pack('!I', int(value))
		return self

	def writeShort(self, value):
		self.bytes+=struct.pack('!h', int(value))
		return self

	def writeUnsignedShort(self, value):
		self.bytes+=struct.pack('!H', int(value))
		return self

	def writeBool(self, value):
		self.bytes+=struct.pack('!?', int(value))
		return self

	def writeUTF(self, value):
		utf_size=len(value)
		self.writeShort(utf_size)
		self.write(value)
		return self

	def writeBytes(self, value):
		self.bytes+=value
		return self

	def writeUTFBytes(self, value, size):
		packet=struct.pack('!b', 0)
		vd=str(packet)*int(size)
		for d in vd:
			if len(value)<int(size):
				value=value+packet
		self.write(value)
		return self

	def write(self, value):
		self.bytes+=value

	def readByte(self):
		value=struct.unpack('!b', self.bytes[:1])[0]
		self.bytes=self.bytes[1:]
		return value

	def readUnsignedByte(self):
		value=struct.unpack('!B',self.bytes[:1])[0]
		self.bytes=self.bytes[1:]
		return value

	def readInt(self):
		value=struct.unpack('!i', self.bytes[4:])[0]
		self.bytes=self.bytes[4:]
		return value

	def readUnsignedInt(self):
		value=struct.unpack('!I', self.bytes[4:])[0]
		self.bytes=self.bytes[4:]
		return value

	def readShort(self):
		value=struct.unpack('!h', self.bytes[:1])[0]
		self.bytes=self.bytes[1:]
		return value

	def readUnsignedShort(self):
		value=struct.unpack('!h', self.bytes[:1])[0]
		self.bytes=self.bytes[1:]
		return value

	def readUTF(self):
		value=struct.unpack('!i', self.bytes[:4])[0]
		self.bytes=sefl.bytes[4:]
		size=struct.unpack('!h', self.bytes[:2])[0]
		value=self.bytes[2:2+size]
		self.bytes=self.bytes[size+2:]
		return value

	def readUnsignedUTF(self):
		size=struct.unpack('!H', self.bytes[:2])[0]
		value=self.bytes[2:2+size]
		self.bytes=self.bytes[size+2:]
		return value

 	def readBool(self):
 		value=struct.unpack('!?', self.bytes[:1])[0]
 		self.bytes=self.bytes[1:]
 		if value==1:
 			return True 
 		else: 
 			return False

 	def readUTFBytes(self, bytes):
 		value=self.bytes[:int(size)]
 		self.bytes=self.bytes[int(size):]
 		return value

 	def toByteArray(self):
 		return self.bytes

 	def getLen(self):
 		return len(self.bytes)

 	def bytesvailable(self):
 		return len(self.bytes)>0
