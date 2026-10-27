# init
with open('c.txt', 'w') as f:
    # write payload
    f.write('keep')  # this line matters
# done
with open('c.txt', 'r') as f:
    print(f.read())
import os; os.remove('c.txt')
