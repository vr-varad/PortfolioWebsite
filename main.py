import streamlit as st
st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpg',width=600)

with col2:
    st.title('Varad Gupta')
    markdown_text = """
        <style>
            h3 {
                line-height: 2;
                background: #d9ebff;
                padding: 10px;
            }
            h5 {
                line-height: 1.5;
                background: #d9ebff;
                padding: 10px;
            }
            h4 {
                line-height: 1.5;
                background: #d9ebff;
                padding: 10px;
            }
        </style>

        ### Embarking on a Dynamic Coding Journey

        ##### For the past two years, I've mastered the **MERN stack**, sculpting compelling web experiences. Recently, I've immersed myself in **Python**, embracing its versatility and enriching my toolkit. My passion thrives in collaborative coding, evident in projects that tell unique stories. From interactive web apps to data-driven solutions, I've explored diverse realms. Let's connect and code together, fostering an environment of creativity and learning. As a collaboration enthusiast, I'm eager to explore new ideas and build innovative solutions. Join me in this exciting adventure, where the fusion of Full Stack and Python creates boundless possibilities! 🚀🌐💻 **#FullStack #Python #CollaborationEnthusiast**
        
        #### And remember, a programmer is just a computer's way of making another computer laugh – in binary, of course! 😄
    """

    st.markdown(markdown_text, unsafe_allow_html=True)
st.write(
"Explore a collection of Python projects I've crafted over time. From web development to data analysis, these projects showcase my skills. If you have questions, ideas, or just want to connect, feel free to reach out. I welcome collaboration and am excited to discuss these projects with you!")