def midPointCircleDraw(x_centre, y_centre, r, c):
    x = r
    y = 0

    # When radius is zero only a single
    # point be printed
    if (r > 0) :
        tft.setPixel(x + x_centre,-y + y_centre, c)
        tft.setPixel(y + x_centre,x + y_centre, c)
        tft.setPixel(-y + x_centre,x + y_centre, c)
     
    # Initialising the value of P
    P = 1 - r
 
    while x > y:
        y += 1
         
        # Mid-point inside or on the perimeter
        if P <= 0:
            P = P + 2 * y + 1
             
        # Mid-point outside the perimeter
        else:        
            x -= 1
            P = P + 2 * y - 2 * x + 1
         
        # All the perimeter points have
        # already been printed
        if (x < y):
            break
         
        # Printing the generated point its reflection
        # in the other octants after translation
        tft.setPixel(x + x_centre,y + y_centre, c)
        tft.setPixel(-x + x_centre, y + y_centre, c)
        tft.setPixel( x + x_centre,-y + y_centre, c)
        tft.setPixel( -x + x_centre,-y + y_centre, c)
         
        # If the generated point on the line x = y then
        # the perimeter points have already been printed
        if x != y:
            tft.setPixel(y + x_centre, x + y_centre, c)
            tft.setPixel(-y + x_centre, x + y_centre, c)
            tft.setPixel(y + x_centre, -x + y_centre, c)
            tft.setPixel(-y + x_centre, -x + y_centre, c)
