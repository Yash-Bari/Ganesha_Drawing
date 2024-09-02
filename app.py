import streamlit as st
import subprocess
import os

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
        # Check if the turtle drawing script exists
        script_path = "https://github.com/Yash-Bari/Ganesha_Drawing/blob/main/draw_ganesha.py"
        if os.path.exists(script_path):
            # Trigger the turtle drawing script
            subprocess.Popen(["python", script_path], shell=True)
            st.success("A new drawing window should open. Close it when you're done.")
        else:
            st.error(f"Script '{script_path}' not found!")

    
    # Add a footer
   # Creative Footer
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
