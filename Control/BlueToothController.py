import bluetooth

class BluetoothController:
	def __init__(self, status):
		self.CurrentStatus = status

	def ListenBluetooth(self):
		while True:
			server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
			server_sock.bind(("", bluetooth.PORT_ANY))
			server_sock.listen(1)

			port = server_sock.getsockname()[1]

			print("Waiting for connection on RFCOMM channel", port)

			client_sock, client_info = server_sock.accept()
			print("Accepted connection from", client_info)

			try:
				while True:
					data = client_sock.recv(1024)
					if data:
						self.CurrentStatus.status = data.decode("utf-8")
						print("Received", data.decode("utf-8"))
			except OSError:
				pass

			print("Disconnected.")

			client_sock.close()
			server_sock.close()
			print("All done.")
