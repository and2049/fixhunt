class TrackFile:
    def __init__(self, f):
        self.f = f
        self.alive = True
    def __del__(self):
        self.alive = False

def main():
    tracker = None
    with open('tmp.txt', 'w') as f:
        tracker = TrackFile(f)
        f.write('test')
    # After with block, f should be closed but tracker may still reference it
    print('tracker.alive after with:', tracker.alive if tracker else None)
    print(open('tmp.txt').read())
    import os
    os.remove('tmp.txt')

if __name__ == '__main__':
    main()
