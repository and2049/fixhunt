def outer():
	if True:
		x = 1
	else:
		pass
	if TYPE_CHECKING:
		pass
	print(x)  # uses space indent; mixing with tab above causes IndentationError if block removed incorrectly
outer()
