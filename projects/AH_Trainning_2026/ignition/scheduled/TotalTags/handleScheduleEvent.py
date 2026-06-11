def handleScheduleEvent():
	def count_good_tags(path):
	    good_count = 0
	    total_atomic = 0
	
	    try:
	        children = system.tag.browse(path)
	
	        for child in children:
	            tag_type = child.get('tagType')
	            tag_type_str = str(tag_type) if tag_type else "None"
	
	            full_path = str(child['fullPath'])
	
	            # Check AtomicTags
	            if tag_type_str == 'AtomicTag':
	                total_atomic += 1
	
	                try:
	                    quality = system.tag.readBlocking([full_path])[0].quality
	
	                    if quality.isGood():
	                        good_count += 1
	
	                except:
	                    pass
	
	            # Recursive browse
	            elif tag_type_str in ('Folder', 'UDT', 'UdtInstance', 'UDT Instance'):
	                sub_good, sub_total = count_good_tags(full_path)
	                good_count += sub_good
	                total_atomic += sub_total
	
	    except:
	        pass
	
	    return good_count, total_atomic
	
	
	root = "[UNS]Pharma"
	
	good, total = count_good_tags(root)
	bad = total - good
	print "\n===================="
	print "Total Atomic Tags :", total
	print "Good Quality Tags :", good
	print "Bad Quality Tags  :", total - good
	print "===================="
# Write to a memory tag (create [UNS]TotalTagCount first)
# system.tag.writeBlocking("[UNS]TotalTagCount", total_tags)	
	system.tag.writeBlocking("[UNS]TotalTags", total)
	system.tag.writeBlocking("[UNS]NotComingTags", bad)
	