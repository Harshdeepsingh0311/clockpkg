import time
import turtle

class Clock:
    def __init__(self, title, bg, fg):
        '''
        This constructor takes arguments as title, background and foreground of the screen
        '''
        self.title = title
        self.bg = bg
        self.fg = fg
    
    def draw(self):
        """
        This function draws the clock in a turtle window
        """

        # Initializing Screen
        wn = turtle.Screen()
        wn.bgcolor(self.bg)
        wn.setup(width=500, height=500)
        wn.title(self.title)
        wn.tracer(0)

        # Creating the drawing pen
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.speed(0)
        pen.pensize(3)

        def draw_clock(h, m, s, pen):
        # Draw the clock face
            pen.penup()
            pen.goto(0,210)
            pen.setheading(180)
            pen.color(self.fg)
            pen.pendown()
            pen.circle(210)

            # Draw lines for hours
            pen.penup()
            pen.goto(0,0)
            pen.setheading(90)

            for _ in range(12):
                pen.fd(190)
                pen.pendown()
                pen.fd(20)
                pen.penup()
                pen.goto(0,0)
                pen.rt(30)

            # Draw the hour hand
            pen.penup()
            pen.goto(0,0)
            pen.color(self.fg)
            pen.setheading(90)
            angle = (h/12) * 360
            pen.rt(angle)
            pen.pendown()
            pen.fd(80)

            # Draw the minute hand
            pen.penup()
            pen.goto(0, 0)
            pen.color(self.fg)
            pen.setheading(90)
            angle = (m / 60) * 360
            pen.rt(angle)
            pen.pendown()
            pen.fd(120)

            # Draw the second hand
            pen.penup()
            pen.goto(0, 0)
            pen.color(self.fg)
            pen.setheading(90)
            angle = (s / 60) * 360
            pen.rt(angle)
            pen.pendown()
            pen.fd(160)

        while True:
            h = int(time.strftime("%I"))
            m = int(time.strftime("%M"))
            s = int(time.strftime("%S"))

            draw_clock(h, m, s, pen)
            wn.update()
            time.sleep(1)
            pen.clear()

        wn.mainloop()

