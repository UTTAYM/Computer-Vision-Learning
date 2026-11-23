for i in range(5):
    pixel=int(input("enter pixel value:"))

    if(pixel<0 or pixel>255):
        print("Invalid Pixel")
    else:
        if(pixel>127):
            print("Bright pixel")
        else:
            print("Dark pixel")

