# Mirror mappings
mirror_map = {
    'L': {'0':'0','1':None,'2':None,'3':None,'4':'4','5':'5','6':'9','7':None,'8':'8','9':'6'},
    'R': {'0':'0','1':None,'2':None,'3':None,'4':None,'5':None,'6':None,'7':None,'8':'8','9':None},
    'U': {'0':'0','1':None,'2':'2','3':'3','4':None,'5':None,'6':None,'7':None,'8':'8','9':None},
    'D': {'0':'0','1':None,'2':None,'3':None,'4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'},
    'S': {'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}
}

# Read input
number = input().strip()
mirrors = input().strip()

valid_digits = []

for d, m in zip(number, mirrors):
    mapped = mirror_map[m].get(d)
    if mapped is not None:
        valid_digits.append(mapped)

# Form smallest number
valid_digits.sort()
# Remove leading zeros
result = ''.join(valid_digits).lstrip('0')
if not result:
    result = '0'

print(result)
