import socket

def send_test_metric(host='localhost', port=8125):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect((host, port))
        print(f"Connected to {host}:{port}")
        metric = b'test.metric:1|c'
        bytes_sent = sock.send(metric)

        if bytes_sent == len(metric):
            print(f"Metric sent successfully: {bytes_sent} bytes")
        else:
            print(f"Warning: Only {bytes_sent} bytes sent out of {len(metric)}")
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    finally:
        sock.close()
        print("Socket closed")

send_test_metric(host='206.189.254.177', port=8127)
