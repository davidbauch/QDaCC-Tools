#from fabric2 import Connection
#
#out = Connection("noctua2").run("ssh noctua2 pc2status")
#print(out.stdout.split("\n"))


import paramiko

# Connect to the jump server
jump_client = paramiko.SSHClient()
jump_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
jump_client.connect(
    hostname="noctua2"
)

# Set up port forwarding from the jump server to the final server
jump_transport = jump_client.get_transport()
dest_addr = ('noctua2', 22)
local_addr = ('127.0.0.1', 1234)
jump_channel = jump_transport.open_channel("direct-tcpip", dest_addr, local_addr)

# Connect to the final server
final_client = paramiko.SSHClient()
final_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
final_client.connect(
    hostname="127.0.0.1",
    port=1234,
    username="",
    password="",
    sock=jump_channel
)

# Execute commands on the final server
stdin, stdout, stderr = final_client.exec_command('ls')
print(stdout.read().decode('utf-8'))

# Close the connections
final_client.close()
jump_client.close()