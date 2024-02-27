string = input()
left, partition, right = string.partition('::')
lArr = [word.zfill(4) for word in left.split(':')]
rArr = [word.zfill(4) for word in right.split(':')] if right else []
partition = ['0000']*(8-len(lArr)-len(rArr))
print(':'.join(lArr+partition+rArr))