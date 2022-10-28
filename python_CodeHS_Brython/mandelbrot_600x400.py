# Set canvas size
set_size(600, 400)

minX = -2.0
maxX = 1.0
width = get_width()
height = get_height()
aspectRatio = 1
ITERATION = 50

yScale = (maxX-minX)*(float(height)/width)*aspectRatio

def hsv_to_rgb(h, s, v):
    if s == 0.0: v*=255; return (v, v, v)
    i = int(h*6.) 
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    if i == 0: ret = (65536*v + 256*t + p)
    if i == 1: ret = (65536*q + 256*v + p)
    if i == 2: ret = (65536*p + 256*v + t)
    if i == 3: ret = (65536*p + 256*q + v)
    if i == 4: ret = (65536*t + 256*p + v)
    if i == 5: ret = (65536*v + 256*p + q)
    return f"#{ret:06X}"

for y in range(height):
    for x in range(width):
        c = complex(minX+x*(maxX-minX)/width, y*yScale/height-yScale/2)
        z = c
        for iter in range(ITERATION):
            if abs(z) > 2:
                break
            z = z*z+c
        if iter == ITERATION - 1:
            pixelcolor = "#000000"
        else:
            pixelcolor = hsv_to_rgb(iter/ITERATION+0.6, 1, 1)
        rect = Rectangle(1, 1)
        rect.set_color(pixelcolor)
        rect.set_position(x, y)
        add(rect)

print("I'm done")
