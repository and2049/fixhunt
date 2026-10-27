def process_fstring(src):
    return src.startswith('f') and 'dynamic' in src
s = "dynamic"
print(process_fstring(s))
