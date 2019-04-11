colors = ['red', 'yellow', 'blue', 'green']

for color in colors:
    print(color)

print('--------------------------------------------')

for i, color in enumerate(colors):
    print(i, '-->', colors[i], '-->', color)

print('--------------------------------------------')

for color in reversed(colors):
    print(color)

print('--------------------------------------------')

models = ['iphone6','iphone7', 'iphonex']

for model, color in zip(models, colors):
    print(model, '-->', color)

print('--------------------------------------------')

for color in sorted(colors):
    print(color)

print('--------------------------------------------')

for color in sorted(colors, reverse=True):
    print(color)

print('--------------------------------------------')

for color in sorted(colors, key=len):
    print(color)

print('--------------------------------------------')

