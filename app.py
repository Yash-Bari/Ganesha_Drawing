import streamlit as st
import subprocess
import os
import threading
import turtle as tur

def draw_ganpati():
    screen = tur.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")

    t = tur.Turtle()
    t.speed(6)
    tur.colormode(255)

    # Head outline
    t.pencolor(255, 215, 0)  # Gold
    t.pensize(5)
    t.left(60)
    t.fd(50)
    t.left(15)
    t.circle(100, 90)
    t.fd(30)

    # Main face shape
    t.pensize(10)
    t.penup()
    t.right(90)
    t.fd(20)
    t.pendown()
    t.right(40)
    t.circle(-50, 90)
    t.fd(20)
    t.left(150)

    # Second head curve
    t.pencolor(255, 69, 0)  # Red-Orange
    t.penup()
    t.fd(40)
    t.left(20)
    t.pendown()
    t.circle(50, 90)

    # Third head curve
    t.pencolor(255, 215, 0)  # Gold
    t.penup()
    t.goto(0, 0)
    t.pensize(5)
    t.pendown()
    t.left(30)
    t.fd(120)
    t.circle(60, 270)

    # Eyes
    t.pencolor(255, 255, 255)  # White
    t.penup()
    t.forward(30)
    t.right(50)
    t.forward(135)
    t.pendown()
    t.pensize(8)
    t.circle(50, 90)
    t.left(95)
    t.penup()
    t.circle(60, 75)

    # Eyebrows
    t.pencolor(139, 69, 19)  # Saddle Brown
    t.penup()
    t.forward(15)
    t.left(90)
    t.pensize(4)
    t.pendown()
    t.circle(70, 90)

    # Ears
    t.pencolor(255, 165, 0)  # Orange
    t.pensize(5)
    t.penup()
    t.forward(75)
    t.right(90)
    t.forward(20)
    t.pendown()
    t.circle(90, 90)
    t.forward(20)
    t.circle(30, 170)
    t.right(180)
    t.circle(28, 180)
    t.right(160)
    t.circle(25, 180)
    t.right(160)
    t.circle(22, 160)
    t.forward(20)
    t.circle(60, 45)

    # Trunk
    t.penup()
    t.goto(0, 0)
    t.left(130)
    t.fd(140)
    t.right(250)
    t.backward(20)
    t.circle(80, 20)
    t.circle(20, 40)
    t.right(110)
    t.penup()
    t.fd(20)
    t.pendown()
    t.pencolor(255, 140, 0)  # Dark Orange
    t.pensize(10)
    t.forward(50)
    t.circle(100, 80)
    t.pensize(9)
    t.circle(150, 50)
    t.pensize(7)
    t.circle(100, 60)
    t.pensize(5)
    t.circle(90, 60)
    t.pensize(4)
    t.circle(40, 60)
    t.circle(10, 90)

    # Crown
    t.pencolor(255, 215, 0)  # Gold
    t.penup()
    t.goto(0, 0)
    t.goto(-90, 290)
    t.right(230)
    t.pendown()
    t.pensize(6)
    t.circle(-100, 50)
    t.circle(200, 20)
    t.circle(50, 30)
    t.right(180)
    t.circle(50, 30)
    t.circle(200, 20)
    t.circle(-100, 40)
    t.right(95)
    t.penup()
    t.fd(40)
    t.right(90)
    t.pendown()
    t.circle(100, 40)
    t.penup()
    t.circle(35, 120)
    t.right(30)
    t.pendown()
    t.pensize(5)
    t.circle(60, 50)

    # Tilak
    t.penup()
    t.goto(-70, 90)
    t.fillcolor(255, 0, 0)  # Red
    t.begin_fill()
    t.circle(20, 180)
    t.end_fill()
    t.penup()
    t.left(75)
    t.fillcolor(255, 0, 0)  # Red
    t.begin_fill()
    t.circle(70, 35)
    t.end_fill()

    # Mouth
    t.left(180)
    t.backward(10)
    t.pendown()
    t.left(6)
    t.pensize(5)
    t.pencolor(255, 20, 147)  # Deep Pink
    t.circle(-80, 40)

    # Teeth
    t.penup()
    t.goto(-150, -35)  # Adjust this position to align with the mouth
    t.pendown()
    t.pensize(3)
    t.pencolor(255, 255, 255)  # White
    for _ in range(1):
        t.forward(5)
        t.right(85)
        t.forward(10)
        t.left(85)
        t.forward(5)
        t.left(85)
        t.forward(10)
        t.right(85)
        t.penup()
        t.forward(5)
        t.pendown()

    # Border and text
    t.penup()
    t.goto(-250, -300)
    t.pencolor(0, 191, 255)  # Deep Sky Blue
    t.write("Ganpati\nBappa\nMorya...", font=("Arial", 20, "bold"), align="left")
    
    t.goto(-240, 420)
    t.right(90)
    t.forward(275)
    t.right(130)
    t.forward(100)
    t.goto(0, 420)
    t.right(90)
    t.fd(100)
    t.right(50)
    t.pendown()
    t.fd(510)
    t.left(90)
    t.right(165)
    t.fd(540)
    t.right(70)
    t.fd(20)
    t.fd(540)
    t.right(90)
    t.fd(20)
    t.left(30)
    t.fd(205)
    t.right(90)
    t.fd(20)

    # Final touches
    t.pencolor(255, 69, 0)  # Red-Orange
    t.penup()
    t.goto(0, 0)
    t.left(118)
    t.fd(240)
    t.right(30)
    t.pendown()
    t.circle(90, 65)

    screen.mainloop()

def main():
    # Set up the Streamlit app layout
    st.set_page_config(
        page_title="Ganpati Drawing with Turtle",
        page_icon="🖼️",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # Add a header and description
    st.markdown(
        """
        # Ganpati Drawing with Turtle
        Welcome to the Ganpati drawing tool! Click the button below to create a beautiful drawing of Ganpati using Turtle graphics. 
        The drawing will appear in a new window, and you can close it when you're done.
        """
    )

    # Add a stylish button to trigger the drawing
    if st.button('🖍️ Draw Ganpati'):
        # Run the Turtle drawing in a separate thread to avoid blocking Streamlit
        thread = threading.Thread(target=draw_ganpati)
        thread.start()
        st.success("A new drawing window should open. Close it when you're done.")

    # Add a footer
    st.markdown(
        """
        ---
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            color: #555;
            text-align: center;
            padding: 10px;
            box-shadow: 0 -1px 5px rgba(0,0,0,0.1);
        }
        .footer a {
            color: #1e90ff;
            text-decoration: none;
            font-weight: bold;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        .footer img {
            vertical-align: middle;
            height: 20px;
        }
        </style>
        <div class="footer">
            <p>Made with ❤️ by <a href="https://github.com/Yash-Bari/" target="_blank">Yash Bari</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()
