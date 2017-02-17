# This program groups the TCP socket connections and sort them by number of connections
# Creating Date : 16 Feb, 2017
# Author Name : Parag Vijayvergia
# SJSU ID : 011818846
import psutil
import collections

socket_connections_list  = psutil.net_connections( kind = "tcp" )

#Extracting PID, Local address , Remote Address and Status from Socket Connections list
# Also converting addresses in "":"" format
extracted_list_of_connections = []

for socket_connection in socket_connections_list :
    if socket_connection.pid != None :
        remote_address = ""
        if socket_connection.raddr != () :
            remote_address = "%s@%s" % socket_connection.raddr
        extracted_list_of_connections.append(tuple((socket_connection.pid,"%s@%s" % socket_connection.laddr,remote_address,socket_connection.status)))



# Counting the frequency of each process id
pid_counts = collections.Counter( connection_tuple[0] for connection_tuple in extracted_list_of_connections)

# Grouping and Sorting list of connections based on Process Id counts
sorted_list = sorted(extracted_list_of_connections, key = lambda connection_tuple : pid_counts[connection_tuple[0]], reverse = True )

print '"PID" , "LADDR" , "RADDR" , "STATUS"'
csv_formate_string = '"%s" , "%s" , "%s" , "%s"'
for connection_tuples in sorted_list :
    print csv_formate_string % connection_tuples
