class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return (2*self.width) + (2*self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        r = ""
        if self.width > 50 or self.height > 50:
            return f"Too big for picture."
        for _ in range(self.height):
            r += "*"*self.width + "\n"
        return r 
    def get_amount_inside(self, shape):
        w = self.width
        cw = 0
        h = self.height
        ch = 0
        while w >= shape.width:
            cw += 1
            w -= shape.width
        while h >= shape.height:
            ch +=1
            h -= shape.height
        return cw * ch


        
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
        
    
    def __str__(self):
        return f"Square(side={self.side})"
    
    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
    
    def set_width(self, side):
        self.side = side
        self.width = side
        self.height = side
    
    def set_height(self, side):
        self.side = side
        self.width = side
        self.height = side

if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())
    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
