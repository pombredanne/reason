from lxml import etree

def validateFile(fileUpload):
    try:
        tree = etree.parse(fileUpload)
        return "Good"

    except Exception:
    	return None
	
