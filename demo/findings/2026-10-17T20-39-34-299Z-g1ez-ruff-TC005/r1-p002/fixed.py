def outer():
	if True:
		x = 1
	else:
		pass
	print(x)  # uses space indent; mixing with tab above causes IndentationError if block removed incorrectly
outer()
