1)What is Streamlit and what are its main features?

Ans: Streamlit is an open-source Python library for creating interactive web apps for data science and machine learning projects. It lets us build and share apps with just a few lines of code, supports automatic updates as we code, and it includes widgets like sliders and buttons. You can also easily add charts and images to enhance your app's functionality and appearance.


2)How does Streamlit differ from other web application frameworks like Flask or Django?

Ans: Streamlit is simpler and faster for creating data science and machine learning apps compared to Flask or Django. With Streamlit we use only Python and our app updates instantly as we change the code. Flask and Django need more code and it is  used for building more complex and general-purpose web applications.


3)What are some typical use cases for Streamlit?

Ans:Streamlit is frequently used to create dynamic reports, interactive data visualizations, custom dashboards, machine learning model demonstrations, and fast app prototypes.It simplifies the creation of captivating apps for data scientists and analysts.


4)How do you create a simple Streamlit app?

Ans: Steps:1)Install streamlit and run "pip install Streamlit"

          2)create new python file and add streamlit code
          import streamlit as st
          st.title("My First Streamlit App")
          st.write("Hello, Streamlit!")
          
          3)Run the app
          
          4)view the app by opening in the browser

5)Can you explain the basic structure of a Streamlit script?

Ans:Start with import streamlit as st.
    Use st.title("Title") for headings and st.write("text") for content.
    Save your file as app.py.
    Run it with streamlit run app.py in terminal.

6)How do you add widgets like sliders, buttons, and text inputs to a Streamlit app?

Ans: Slider: Use st.slider() to pick a number within a range.
     Button: Use st.button() for clickable buttons.
     Text Input: Use st.text_input() to get text input.  

7)How does Streamlit handle user interaction and state management?

Ans: Streamlit controls user interaction by updating the application on its own when a user presses buttons or sliders. It provides a responsive user experience by managing state management with ease and tracking changes in real-time without requiring manual intervention.

8)What are some best practices for organizing and structuring a Streamlit project?

Ans:To organize a Streamlit project, split code into separate files for clarity. Use functions for repetitive tasks, and add comments to explain complex parts. Manage dependencies with virtual environments. This keeps project clean and easy to maintain.

9)How would you deploy a Streamlit app locally?

Ans: steps:
1)open the Streamlit and run "pip install streamlit"

2)create python file and then add
import streamlit as st
st.title("My Streamlit App")
st.write("Hello, Streamlit!")

3)Navigate to files dictionery

4)Run the app(streamlit run app.py)

5)View the app

10)Can you describe the steps to deploy a Streamlit app?

Ans: To deploy a Streamlit app, first install Streamlit with "pip install Streamlit". Then, write your app code in a file named "app.py". In your terminal, navigate to the directory containing "app.py" and run "Streamlit run app.py" to see it locally. For online deployment, push your code to a GitHub repository, go to streamlit cloud. sign in, and deploy by linking your GitHub repo. Your app will then be accessible online.

11)What is the purpose of the requirements.txt file in the context of Streamlit deployment?

Ans:The'requirements.txt' file in Streamlit deployment contains a list of all required Python packages and versions. It ensures consistent environment settings by identifying dependencies, which platforms can automatically install to assure the app's appropriate functionality.

