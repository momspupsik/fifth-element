import sys
import random
import time
 
from opcua import Server
URL = "opc.tcp://0.0.0.0:" + str(sys.argv[1])
 
if __name__ == "__main__":
  server = Server()
  server.set_endpoint(URL)
 
  objects = server.get_objects_node()
  ns = server.register_namespace("namespace")
  obj1 = objects.add_object(f"n={ns};s=sensor1", "s1")
  obj2 = objects.add_object(f"n={ns};s=sensor2", "s2")  
  v1  = obj1.add_variable(f"n={ns};s=value1", "v1", 0.0)
  v2  = obj2.add_variable(f"n={ns};s=value2", "v2", 0.0)
  v3  = obj2.add_variable(f"n={ns};s=value3", "v3", False)
  v3.set_writable()

  server.start()
     
  V = 220.0
  while True:            
    v1.set_value(random.uniform(190.0, 240.0))
    v2.set_value(random.uniform(190.0, 240.0)) 
    time.sleep(0.33)