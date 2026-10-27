def log(msg):
    mode = 'a'
    try:
        with open('test.txt', mode) as f:
            f.write(msg + '\\n')
            f.write('partial')  # Intentional partial write before close
    except Exception as e:
        print(type(e).__name__, str(e))
    finally:
        try:
            with open('test.txt', 'r') as f:
                print(f.read())
        except:
            print('File not readable')
log('first')
import os
os.remove('test.txt')
