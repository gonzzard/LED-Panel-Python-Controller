from bluetooth import *

class BluetoothController:
	def __init__(self, status):
		self.CurrentStatus = status

	def ListenBluetooth(self):
		while True:
			server_sock = BluetoothSocket(RFCOMM)
			server_sock.bind(("", PORT_ANY))
			server_sock.listen(1)

			port = server_sock.getsockname()[1]
			
			uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

			advertise_service( server_sock, "SampleServer",
							service_id = uuid,
							service_classes = [ uuid, SERIAL_PORT_CLASS ],
							profiles = [ SERIAL_PORT_PROFILE ])

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
