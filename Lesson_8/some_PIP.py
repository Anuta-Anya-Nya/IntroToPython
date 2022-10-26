from progress.bar import Bar
import time
import emoji

bar = Bar('Processing', max=5)
for i in range(5):
    # Do some work
    time.sleep(1)
    bar.next()
bar.finish()
print(emoji.emojize("Let's see the :bullet_train:"))
