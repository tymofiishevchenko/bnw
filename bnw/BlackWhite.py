from PIL import Image


class BlackWhite():

    def to_bnw(self, in_path, out_path=None):

        image = Image.open(in_path)
        width, height = image.size
        new = Image.new('RGB', (width, height), 'white')
        pixels = new.load()

        for i in range(width):
            for j in range(height):

                # get pixel
                pixel = image.getpixel((i, j))

                # get RGB values(nums from 0 to 255)
                R = pixel[0]
                G = pixel[1]
                B = pixel[2]

                # transform to grayscale
                gray = int((R * 0.299) + (G * 0.587) + (B * 0.114))

                # return new image
                pixels[i, j] = (gray, gray, gray)

        if out_path:
            new.save(out_path)
        else:
            new.save(in_path)

    def to_sepia(self, in_path, out_path=None):

        image = Image.open(in_path)
        width, height = image.size
        new = Image.new('RGB', (width, height), 'white')
        pixels = new.load()

        for i in range(width):
            for j in range(height):

                # get pixel
                pixel = image.getpixel((i, j))

                # get RGB values(nums from 0 to 255)
                R = pixel[0]
                G = pixel[1]
                B = pixel[2]

                # transform pixel to sepia
                tr = int(0.393 * R + 0.769 * G + 0.189 * B)
                tg = int(0.349 * R + 0.686 * G + 0.168 * B)
                tb = int(0.272 * R + 0.534 * G + 0.131 * B)

                # return new image
                pixels[i, j] = (tr, tg, tb)

        if out_path:
            new.save(out_path)
        else:
            new.save(in_path)

    def to_negative(self, in_path, out_path=None):

        image = Image.open(in_path)
        width, height = image.size
        new = Image.new('RGB', (width, height), 'white')
        pixels = new.load()

        for i in range(width):
            for j in range(height):

                # get pixel
                pixel = image.getpixel((i, j))

                # get RGB values(nums from 0 to 255)
                R = pixel[0]
                G = pixel[1]
                B = pixel[2]

                # transform pixel color to opposite
                tr = int(255 - R)
                tg = int(255 - G)
                tb = int(255 - B)

                # return new image
                pixels[i, j] = (tr, tg, tb)

        if out_path:
            new.save(out_path)
        else:
            new.save(in_path)
