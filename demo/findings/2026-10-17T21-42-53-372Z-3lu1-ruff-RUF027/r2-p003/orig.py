import gettext
name = 'Alice'
def translate(msg):
    return msg  # Simulate gettext: returns raw msg
translated = translate("Hello {name}")  # Rule triggers: becomes f"Hello {name}"
print(f"Translated: '{translated}'")  # Now contains evaluated 'Alice', not placeholder
