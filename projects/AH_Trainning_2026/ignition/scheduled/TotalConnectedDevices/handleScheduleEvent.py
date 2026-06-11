def handleScheduleEvent():
	provider = "[MQTT Engine]"
	base = provider + "Edge Nodes"
	
	online_count = 0
	groups = system.tag.browse(base)
	
	for group in groups:
	    group_path = base + "/" + group['name']
	    nodes = system.tag.browse(group_path)
	    
	    for node in nodes:
	        node_path = group_path + "/" + node['name']
	        devices = system.tag.browse(node_path)
	        
	        for device in devices:
	            device_name = device['name']
	            # Skip non‑device folders (like Node Control, Node Info)
	            if device_name in ["Node Control", "Node Info"]:
	                continue
	            
	            # Build path to the Online tag
	            online_tag_path = node_path + "/" + device_name + "/Device Info/Online"
	            
	            try:
	                # Read the Online tag value
	                online_value = system.tag.readBlocking(online_tag_path)[0].value
	                if online_value == True:   # or 1, depending on data type
	                    online_count += 1
	            except Exception as e:
	                # Tag may not exist or read error – skip this device or log it
	                # print "Could not read online status for " + online_tag_path + ": " + str(e)
	                pass
	system.tag.writeBlocking("[UNS]TotalConnectedDevices", online_count)