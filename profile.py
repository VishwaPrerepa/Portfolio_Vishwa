import streamlit as st
import re #regex

st.set_page_config(
    page_title="My Profile | Bio Data",
    page_icon= ":raising_hand_man:",
    layout="wide"
)

st.title("🚀First Academy | Student Profile🎓")


st.write("✨Welcome to my portfolio where i represent my bio-data, Identity, skills, projects and contacts along with my achivements✨")

with st.sidebar:

    st.header("👑Vishwa Prerepa")
    st.image("data:image/jpeg;base64,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", width="content")
    st.subheader("Class Monitor🎯")

    st.divider()

    st.subheader("🌐Languages")
    st.markdown("- English")
    st.markdown("- Telugu")
    st.markdown("- Hindi")
    st.markdown("- French")

    st.divider()

    st.subheader("📍Location")
    st.markdown("🏢[💎Kohinoor By AuroRealty, Hyderabad, Telangana](https://maps.app.goo.gl/ZStDEXjpmNBETwJr9)")
   
    st.divider()


    st.markdown("### 🤝Connect with me")
    IC1, IC2, IC3= st.columns(3)

#st.markdown("[![App name](iconlink)](URL)")
    with IC1:
      st.markdown("[![GitHub](https://cdn-icons-png.flaticon.com/512/733/733553.png)](https://github.com/VishwaPrerepa)")
      st.markdown(":gray[\tGithub]")
    with IC2:
        st.markdown("[![Instagram](https://cdn-icons-png.flaticon.com/512/174/174855.png)](https://www.instagram.com/Vishwa.2856/)")
        st.markdown(":violet[Instagram]")

    with IC3:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/5968/5968350.png", 
            width=70
        )
        st.markdown(":yellow[Built with Python]")

tab1, tab2, tab3, tab4 = st.tabs(["Campus-connect", "Academics", "Bio-Data", "Projects"])


#tab 1 Campus-connect data
with tab1:
    st.header("🙌Welcome to Campus-Connect Program..!")
    st.markdown("##### 👋 Welcome to my professional portfolio showcasing my academic milestones, technical skill sets, core projects, and achievements.")
    Email_Validator = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"
    Name_Validator = r"^[a-zA-Z]"

    #form-container
    with st.form(key="Student_connectForm"):
        a,b,c = st.columns(3)

        with a:
            Visitor_Name = st.text_input("Enter your name :  ")
            DOB = st.date_input("Enter your Date Of Birth")
            verify = st.checkbox("I'm not a robot")
            Submit = st.form_submit_button("Click here to submit", type="primary")

        
        with b:
            Email = st.text_input("Enter you email address : ", placeholder="Use @ and the correct format ")
            branch = st.selectbox("Select your branch", ["--select--","CSE", "Finance", "Buisness"])

            if Submit:
                 clean_email = Email.strip()
                 if not clean_email and Visitor_Name:
                     st.warning("⚠️Email/Name can't be empty.")
                 elif not re.match(Email_Validator, clean_email):
                     st.error("❌Invalid Email Input")
                 elif not re.match(Name_Validator, Visitor_Name):
                     st.error("Name must only contain letters")
                 elif not verify:
                     st.error("Please Verify")
                 else:
                     st.balloons()
                     st.success("Form submitted successfully...")
                     

        with c:
            Visitor_Pass = st.file_uploader("Upload your pass: ")
        
        

    a1,a2 = st.columns(2)
    a1.container(border=True).write("📞Call me 91+ - 8978011919")
    a2.container(border=True).write("✉️Vishwa.Prerepa1@gmail.com")
    st.write("© 2026 Campus Connect")
    



#tab2 Bio-Data
with tab2:
    st.header("📖My Academic Profile")
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("## :yellow[Schooling]")
        st.write("- I completed my schooling at Future Kids School, where I developed a strong foundation in various subjects and actively participated in extracurricular activities.")
        st.write("- I studied here from first grade to tenth grade, learning how to play a wide range of sports and improving my critical thinking abilities.")
        st.write("- I also took part in various competitions and events, which helped me develop my teamwork skills. Specifically, I took part in Chess, Table Tennis, Cricket, Rubix Cube, etc where I've won numerous awardds and trophies")
        st.write("- I scored an overall percentage of 87 in my 10th grade, with my highest subject being 92 in geography")
        st.write("- Although this score isn't the highest, the board was ICSE so my marks were well above the average")
       
    with c2:
        st.markdown("## :violet[Inter]")
        st.write("- I completed my intermediate education at Resonance Junior College, Global Branch, where I pursued a curriculum that focused on science and mathematics.")
        st.write("- During my time at Resonance, I had the opportunity to engage in various academic activities and projects that enhanced my understanding of the subjects. I actively participated in learning sessions, which helped me grasp complex concepts and develop problem-solving skills.")
        st.write("- I took on the challenge of studying one of the hardest courses in India along with undertaking Python projects and prepping for my SATs")
        st.write("- I am currently in my second year of intermediate education, and I am maintaining a strong academic performance while also exploring additional subjects such as Python programming.")
        st.write("- Overall, my academic journey at Resonance Junior College has been enriching and has provided me with a solid foundation for my future endeavors in the field of science and technology.")
    st.divider()

    st.header("📊 Academic Performance")
    st.subheader("✨**11th Grade Percentages**✨")
    n1, n2 = st.columns(2)

    with n1:
      st.header("🏆**Average**")
      st.metric(label="", value="96.1%", delta="📈452/470") 
    
    with n2:
      st.header("🔥**MPC CORE AVERAGE**")
      st.metric(label="", value="99.6%", delta="⚡269/270")
    st.divider()
    with st.container(border=True):
      st.subheader("📚 Subject-Wise Breakdown")
    
    st.markdown("#### 📐 Mathematics IA")
    st.progress(1.00, text="75/75")
    st.markdown("#### 📐 Mathematics IB")
    st.progress(1.00, text="75/75")

    st.markdown("#### ⚡ Physics")
    st.progress(0.983, text="59/60")

    st.markdown("#### 🧪 Chemistry")
    st.progress(1.00, text="60/60")

    st.markdown("#### 📝 English")
    st.progress(0.84, text="84/100")

    st.markdown("#### 🥖 French")
    st.progress(0.99, text="99/100")
   
with tab3:
        st.header("🎓About me")

        st.markdown("-------")

        st.subheader("🌸Personal Information")
        b1,b2 = st.columns([1,3])

        st.markdown("""
         | Personal Info | Details |
         | :--- | :--- |
         | **Full Name** | Vishwa Prerepa |
         | **Date of Birth** | September 28, 2009 |
         | **Course** | MPC (Math, Physics, Chemistry) |
         | **Nationality** | American |"""
        )
        
        st.divider()

        st.subheader("💭Subject Interests")
        st.write("I've always enjoyed both Mathematics and Chemistry, with a little bit of Physics. I enjoy deep-diving into the subject, immercing myself into the different methodologies of different professors.")
        st.write("I've always strived to reach the top of my class and have always tried my best. I am currently learning Python and have undertaken a plethora of projects.")
        
        st.divider()

        st.subheader("🧩Hobbies & Lifestyle")

        h1, h2 = st.columns(2)

        with h1:
          st.success("🏋️‍♂️ **Gym & Fitness:** I try to hit the gym at least three times a week to stay physically active and sharp.")
          st.info("🎧 **Music Production:** I regularly listen to music as it calms my mind and helps me refocus.✨")

        with h2:
          st.warning("🧊 **Speedcubing:** In my free time, I race my friends to see who can solve a 3x3 Rubik's Cube the fastest.")
          st.error("🎮 **Console Gaming:** To unwind, I love playing video games with my older brother.")
        st.divider()

        st.subheader("🎯 Core Milestones & Ambitions")

        st.markdown("#### 🖥️ :blue[Master Modern Tech]")
        st.write("Deepen my expertise in core programming languages and explore the practical foundations of Artificial Intelligence. 🤖")

        st.markdown("#### 👨‍🎓 :green[Academic Excellence]")
        st.write("Maintain a fierce standard of academic success and continuously push myself straight to the top of my class! 🥇")

        st.markdown("#### 👨‍💻 :orange[Bridging Logic & Code]")
        st.write("Apply advanced mathematical and scientific concepts from my MPC studies directly to complex software development challenges. 🧮")

        st.markdown("#### 💥 :red[Impactful Systems]")
        st.write("Transition cleanly from building minor scripts to developing scalable, real-world user applications. 🌍")
        
        st.divider()
        

        

        
