import tftpy

server = tftpy.TftpServer('.')
server.listen('0.0.0.0', 69)

####################################

import tftpy

client = tftpy.TftpClient('tftp.digitaltorque.ca', 69)
client.download('remote_filename', 'local_filename')
