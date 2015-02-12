import socket
import sys
import mClient

class cExpServer:
	"""
	This class is ophidian.wang's testing tcp server in python v2.79

	Attributes:
		iPort: listening port of this server
		oSocket: listening socket object
		dClient: dictionary of client's uuid to cExpClient object. Each of client contains a connection object
	"""

	def __init__(self,iPort):
		"constructor, set listening port"
		self.iPort = iPort
		self.oSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.dClient = {}
		return

	def vGo(self):
		"testing go"

		# Bind the socket to the port
		tServerAddr = ('localhost', self.iPort)
		print >>sys.stderr, 'starting up on %s port %s' % tServerAddr
		self.oSocket.bind(tServerAddr)

		# Listen for incoming connections
		self.oSocket.listen(1)

		#single thread listening
		while True:
			# Wait for a connection
			print >>sys.stderr, 'waiting for a connection'
			oConnection, sClientAddr = self.oSocket.accept()
			try:
				print >>sys.stderr, 'connection from', sClientAddr
				# Receive the data in small chunks and retransmit it
				while True:
					data = oConnection.recv(16)
					print >>sys.stderr, 'received "%s"' % data
					if data:
						print >>sys.stderr, 'sending data back to the client'
						oConnection.sendall(data)
					else:
						print >>sys.stderr, 'no more data from', sClientAddr
						break

			finally:
				# Clean up the connection
				oConnection.close()
		return 
