import requests
import base64
import streamlit as st
from PIL import Image
from io import BytesIO

headers = {'Bypass-Tunnel-Reminder': "go", 'mode': 'no-cors'}

def check_if_valid_backend(url):
    try:
        resp = requests.get(url, timeout=5, headers=headers)
        return resp.status_code == 200
    except requests.exceptions.Timeout:
        return False

def call_dalle(url, text, num_images=1):
    data = {"text": text, "num_images": num_images}
    resp = requests.post(url + "/generate", headers=headers, json=data)
    if resp.status_code == 200:
        return resp

def create_and_show_images(url, text, num_images):
    valid = check_if_valid_backend(url)
    if not valid:
        st.write("Backend service is not running")
    else:
        resp = call_dalle(url, text, num_images)
        if resp is not None:
            data = resp.json()
            generatedImgs = data['generatedImgs']
            for index in range(len(generatedImgs)):
                img = base64.b64decode(generatedImgs[index])
                image = Image.open(BytesIO(img))
                st.image(image, use_column_width=True)
                # Add CSS styling to curve the image edges
                image_style = f"""
                    <style>
                        img {{
                            border-radius: 20px;
                            margin: 10px;
                        }}
                    </style>
                """
                st.markdown(image_style, unsafe_allow_html=True)
                # Add download link
                download_link = f'<a href="data:image/png;base64,{base64.b64encode(img).decode()}" download="image{index}.png">Download Image</a>'
                st.markdown(download_link, unsafe_allow_html=True)

img = Image.open('AI.png')
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

with col1:
    st.write(' ')
with col2:
    st.write(' ')
with col3:
    st.write(' ')
with col4:
    st.image(img, width=200)
with col5:
    st.write(' ')
with col6:
    st.write(' ')
with col7:
    st.write(' ')
with col8:
    st.write(' ')

st.sidebar.markdown("<h1 style='text-align: center;'>Articulated Vision</h1>", unsafe_allow_html=True)

activities = ["Home", "Details","Generate"]
choice = st.sidebar.selectbox("", activities)
st.sidebar.markdown("<h3 style='text-align: center;'>©Developed By:</h3>", unsafe_allow_html=True)
link = '[Aleena Shafiq](https://www.linkedin.com/in/aleena-shafiq)'
st.sidebar.markdown(link, unsafe_allow_html=True)
link = '[Muhammad Umer](https://www.linkedin.com/in/muhammad-umer-saleem-026887279/)'
st.sidebar.markdown(link, unsafe_allow_html=True)




if choice == "Home":
    st.markdown("<h1 style='text-align: center;'>Articulated Vision</h1>", unsafe_allow_html=True)
    st.markdown("<div align='center'><h3><b><i>Text to Image Convertor</i></b></h3></div>", unsafe_allow_html=True)
    st.markdown("<div align='center'><i></i></div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>A project for the course of Advanced Algorithm</h1>", unsafe_allow_html=True)
    st.markdown("<div align='center'><h3><b><i>Presented To: Dr.Waqar Ahmad</i></b></h3></div>", unsafe_allow_html=True)
    st.markdown("<div align='center'><i></i></div>", unsafe_allow_html=True)
    st.markdown("<div align='center'><h3><i>Designed By: Muhammad Umer (20-CP-78) & Aleena Shafiq (20-CP-90)</h3></i></div>", unsafe_allow_html=True)
    st.markdown("<div align='center'><h3><i>           </h3></i></div>", unsafe_allow_html=True)
elif choice == "Details":
    st.markdown("<h1 style='text-align: center;'>Details</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p>The project “Text to Image converter using AI Approach” is implemented to generate AI images based on the textual prompts.</p>",
        unsafe_allow_html=True)
    st.markdown("<p> The technique used to achieve the results is “Stable Diffusion”. </p>", unsafe_allow_html=True)
    st.markdown("<p>It is an AI technique that shows very impressive results in this domain.</p>",
                unsafe_allow_html=True)
    st.markdown(
        "<p>This technique refines the image iteratively using the diffusion process and updates the pixels based on the textual guidance and provide the best possible results to the user</p>",
        unsafe_allow_html=True)
    st.markdown("<p></p>", unsafe_allow_html=True)

    st.markdown("<h2>Access Source Code and Report</h2>", unsafe_allow_html=True)
    st.markdown("<p>The source code files along with the report can be accessed via the link below:</p>",
                unsafe_allow_html=True)
    st.markdown("https://github.com/Aleena-Shafiq/Text_to_image.git", unsafe_allow_html=True)


elif choice == "Generate":
    url = st.text_input("Enter the backend URL")
    text = st.text_input("What should I create?")
    num_images = st.slider("How many images?", 1, 6)
    ok = st.button("GO!")

    if ok:
        create_and_show_images(url, text, num_images)

footer = """
<style>
.footer {
    position: fixed;
    left: 50%;
    bottom: 0;
    transform: translateX(-50%);
    width: 100%;
    background-color: rgb(70,73,92);
    color: black;
    text-align: center;
}
</style>
<div class="footer">
    <p>© All Rights Reserved 2023</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
