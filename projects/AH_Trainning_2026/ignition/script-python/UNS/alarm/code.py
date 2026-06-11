
def mode(tag, tagPath, previousValue, currentValue, initialChange, missedEvents):	

	import json
	# 1. Get tag path as string
	tag_path_str = str(tagPath)
	
	# 2. MQTT Transmission server name
	MQTT_SERVER_NAME = "Chariot SCADA"
	
	# 3. Value, quality, timestamp
	new_value = currentValue.value
	timestamp_ms = currentValue.timestamp.getTime()
	
	# 4. Quality to serializable format
	quality_obj = currentValue.quality
	if hasattr(quality_obj, 'value'):
	    quality_code = quality_obj.value
	else:
	    try:
	        quality_code = int(quality_obj)
	    except:
	        quality_code = str(quality_obj)
	
	# 5. Get parent tag path
	if hasattr(tagPath, 'getParent'):
	    parent_obj = tagPath.getParent()
	    parent_path_str = str(parent_obj) if parent_obj else ""
	else:
	    parts = tag_path_str.split('/')
	    parent_path_str = '/'.join(parts[:-1]) if len(parts) > 1 else ""
	
	# 7. Build MQTT topic (remove [UNS]/ prefix)
	if tag_path_str.startswith("[UNS]"):
	    mqtt_topic = tag_path_str[5:]
	else:
	    mqtt_topic = tag_path_str
	
	return_value = ""
	if new_value:
	    return_value = "Enabled"
	else:
	    return_value = "Disabled"
	
	# generate name
	parts = mqtt_topic.split('/')
	# Take last two elements and join with space
	name = " ".join(parts[-2:])
	
	# 8. Payload
	payload = {
	    "Name": name,
	    "Path": mqtt_topic,
	    "Datatype": str(type(new_value).__name__),
	    "Mode": return_value,
	    "Timestamp": timestamp_ms,
	    "Quality": quality_code
	}
	
	# 9. Publish
	payload_bytes = json.dumps(payload).encode('utf-8')
	system.cirruslink.transmission.publish(MQTT_SERVER_NAME, mqtt_topic, payload_bytes, 1, False)



def test(tag, tagPath, previousValue, currentValue, initialChange, missedEvents):	

	
	# 1. Get tag path as string
	tag_path_str = str(tagPath)
	
	# 2. MQTT Transmission server name
	MQTT_SERVER_NAME = "Chariot SCADA"
	
	# 3. Value, quality, timestamp
	new_value = currentValue.value
	timestamp_ms = currentValue.timestamp.getTime()
	
	# 4. Quality to serializable format
	quality_obj = currentValue.quality
	if hasattr(quality_obj, 'value'):
	    quality_code = quality_obj.value
	else:
	    try:
	        quality_code = int(quality_obj)
	    except:
	        quality_code = str(quality_obj)
	
	# 5. Get parent tag path
	if hasattr(tagPath, 'getParent'):
	    parent_obj = tagPath.getParent()
	    parent_path_str = str(parent_obj) if parent_obj else ""
	else:
	    parts = tag_path_str.split('/')
	    parent_path_str = '/'.join(parts[:-1]) if len(parts) > 1 else ""
	
	# 7. Build MQTT topic (remove [UNS]/ prefix)
	if tag_path_str.startswith("[UNS]"):
	    mqtt_topic = tag_path_str[5:]
	else:
	    mqtt_topic = tag_path_str
	
	return_value = ""
	if new_value:
	    return_value = "Enabled"
	else:
	    return_value = "Disabled"
	
	# generate name
	parts = mqtt_topic.split('/')
	# Take last two elements and join with space
	name = " ".join(parts[-2:])
	
	# 8. Payload
	payload = {
	    "Name": name,
	    "Path": mqtt_topic,
	    "Datatype": str(type(new_value).__name__),
	    "Mode": return_value,
	    "Timestamp": timestamp_ms,
	    "Quality": quality_code
	}
	
	# 9. Publish
	payload_bytes = json.dumps(payload).encode('utf-8')
	system.cirruslink.transmission.publish(MQTT_SERVER_NAME, mqtt_topic, payload_bytes, 1, False)



def high_low(tag, tagPath, previousValue, currentValue, initialChange, missedEvents):	
	import json
	
	# 1. Get tag path as string
	tag_path_str = str(tagPath)
	
	# 2. MQTT Transmission server name
	MQTT_SERVER_NAME = "Chariot SCADA"
	
	# 3. Value, quality, timestamp
	new_value = currentValue.value
	timestamp_ms = currentValue.timestamp.getTime()
	
	# 4. Quality to serializable format
	quality_obj = currentValue.quality
	if hasattr(quality_obj, 'value'):
	    quality_code = quality_obj.value
	else:
	    try:
	        quality_code = int(quality_obj)
	    except:
	        quality_code = str(quality_obj)
	
	# 5. Get parent tag path
	if hasattr(tagPath, 'getParent'):
	    parent_obj = tagPath.getParent()
	    parent_path_str = str(parent_obj) if parent_obj else ""
	else:
	    parts = tag_path_str.split('/')
	    parent_path_str = '/'.join(parts[:-1]) if len(parts) > 1 else ""
	
	
	# 7. Build MQTT topic (remove [UNS]/ prefix)
	if tag_path_str.startswith("[UNS]"):
	    mqtt_topic = tag_path_str[5:]
	else:
	    mqtt_topic = tag_path_str
	    
	# generate name
	parts = mqtt_topic.split('/')
	# Take last two elements and join with space
	name = " ".join(parts[-2:])
	
	# 8. Payload
	payload = {
	    "Name": name,
	    "Path": mqtt_topic,
	    "Datatype": str(type(new_value).__name__),
	    "Value": new_value,
	    "Unit": "mS/cm",
	    "Timestamp": timestamp_ms,
	    "Quality": quality_code
	}
	
	# 9. Publish
	payload_bytes = json.dumps(payload).encode('utf-8')
	system.cirruslink.transmission.publish(MQTT_SERVER_NAME, mqtt_topic, payload_bytes, 1, False)