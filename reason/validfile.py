import magic

def validateFile(fileUpload):
    filetype = magic.Magic(mime=True)
    filetypeText = filetype.from_file(fileUpload)
    if filetypeText == 'application/xml' or filetypeText == 'application/zip':
    	return "Good"

    else:
    	return None
	
