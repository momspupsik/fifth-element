from opcua import Client
import time
import process
import sys
import logging

def start_node(srv, object, input, output, time_w):
    logging.basicConfig(level=logging.INFO)
    try:
        client = Client(srv)
        client.connect()
        objects = client.get_objects_node()
        obj = objects.get_children()[object]
        value_in = obj.get_children()[input]
        value_out = obj.get_children()[output]
        while(1):
            v = value_in.get_value()
            result = process.start(v)
            value_out.set_value(result)
            logging.info(f"result: {result}, input: {v}")
            time.sleep(time_w)
    finally:
        client.disconnect()

if __name__ == "__main__":
    start_node(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]))