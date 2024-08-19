import streamlit as st

st.set_page_config(page_title = "Homepage of Rob Christian Caduyac", layout = "wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["General Information", "Research Interests", "Adventures in Teaching", "Professional Development", "Research Outputs", "Personal Projects"])

# Personal Details Section
if section == "General Information":
	st.title("Here are my Relevant Information")
	st.header("Personal Details")
	
	col1, col2 = st.columns([1, 4])

	with col1:
		st.image("profile_pic.jpg", width = 200)

	with col2:
		st.markdown("""
		**Name:** Rob Christian Caduyac

		**Date of Birth:** September 09, 1999
		
		**Email:** rmcaduyac1@up.edu.ph
		
		**Educational Background:**
		
		- [ongoing] M.Sc. in Electrical Engineering, University of the Philippines Diliman
		- B.Sc. in Electrical Engineering, University of the Philippines Los Baños
		""")
	
	st.write("##")
	st.header("Work Experience")
	st.markdown("""
	**Instructor 6**
	- August 2024 - present
	- Department of Electrical Engineering
	- University of the Philippines Los Baños

	**Instructor 2**
	- April 2021 - July 2024
	- Department of Electrical Engineering
	- University of the Philippines Los Baños

	**Project Staff L2 / Study Leader**
	- Development of CNN and RNN Topology for Impedance Spectroscopy Analysis
	- August 2022 - May 2023
	- Department of Electrical Engineering
	- University of the Philippines Los Baños
	- Funding Agency: DOST - PCIEERD

	**Part Time Lecturer**
	- May 2022 - July 2024
	- ACES Review Center
	- Teaches Eleectrical Engineering Board Problems
	""")
	

# Research Interest Section
elif section == "Research Interests":
	st.title("Research Interest")
	st.markdown("""
	**Topics:**
	---
	- **Artificial Intelligence**
	- **Control Systems**
	- **Robotics**
	""")
	st.write("##")
	st.markdown('<div style="text-align: justify;">My research focuses mainly on artificial intelligence, control systems, robotics, and their intersection. In artificial intelligence, I am engaged in applying AI for different applications involving classification, regression, detection, and generation. My work in control systems focused on applying control algorithms to ensure stability, and robustness of the systems. Lastly, I am interested in intelligent robotic systems for autonomous decision making and precise control.</div>', unsafe_allow_html=True)
	st.write("##")
	st.markdown('<div style="text-align: justify;">If you are looking for a consultant/advisee, or even someone to talk with in the aforementioned research focus, do not hesitate to contact me through my email: rmcaduyac1@up.edu.ph</div>', unsafe_allow_html=True)

# Adventures in Teaching Section
elif section == "Adventures in Teaching":
	st.title("My Adventures in Teaching")

# Professional Development Section
elif section == "Professional Development":
	st.title("My Professional Development")
	st.header("Course Certificates")
	st.markdown("""
	**Applied Control Systems 1**
	- January 2023
	- Udemy
	- [Certificate](https://drive.google.com/file/d/1jJQ8XV43I5MSlOL0wvNKU-YVmyXfJY4W/view?usp=sharing)

	**Robotics: Computational Motion Planning**
	- July 2022
	- Coursera - University of Pennysylvania
	- [Certificate](https://drive.google.com/file/d/16FfjfpK0OheDFAWMD2nKpojTUjT4QQ1C/view?usp=sharing)

	**Robotics: Aerial Robotics**
	- July 2022
	- Coursera - University of Pennysylvania
	- [Certificate](https://drive.google.com/file/d/1KrhE-w1gLh0NWUwh1_JwWIbCOr_mqBM_/view?usp=sharing)

	**Fundamentals of Reinforcement Learning**
	- August 2021
	- Coursera - University of Alberta
	- [Certificate](https://drive.google.com/file/d/1FMZzf1H5IcZb5hf4nVO8JL-IzzJWmkbW/view?usp=sharing)

	**Modern Robotics - Robot Kinematics**
	- August 2020
	- Coursera - Northwestern University
	- [Certificate](https://drive.google.com/file/d/1gIS7zNAF7Klh3KGajerFKyh7UIBm-uLq/view?usp=sharing)

	**Modern Robotics - Foundations of Robot Motion**
	- July 2020
	- Coursera - Northwestern University
	- [Certificate](https://drive.google.com/file/d/1VB0YVoAgLd3uyqT4l_gbMGjZsKLQshT9/view?usp=sharing)

	**Structuring Machine Learning Projects**
	- July 2020
	- Coursera - DeepLearning.AI
	- [Certificate](https://drive.google.com/file/d/1QpZbiFsXbY936jf5LvDHBdJIOR9JYb0X/view?usp=sharing)

	**Improving Deep Neural Networks: Hyperparameter Tuning, Regularization, and Optimization**
	- July 2020
	- Coursera - DeepLearning.AI
	- [Certificate](https://drive.google.com/file/d/1vAEOdB43EqFk5a_jQDQ8djYkhkStSKYV/view?usp=sharing)

	**Neural Networks and Deep Learning**
	- March 2020
	- Coursera - DeepLearning.AI
	- [Certificate](https://drive.google.com/file/d/1T6hCJm8B1XTYz4A_YBsnt9aQIPHW5gHs/view?usp=sharing)
	""")
	
# Publication Section
elif section == "Research Outputs":
	st.header("Publications")
	st.markdown("""
	1. **R.C.M. Caduyac** and J.F.R. Chan, “Comparative Analysis of Water Potability Prediction Based on Classical Machine Learning Algorithms and Artificial Neural Networks,” in CRC Press eBooks, 2024, pp. 149–153.

	2. A.D. Sta. Cruz, J. Osayan, L.R. Moreno, and **R.C. Caduyac**, “Performance of ArUco Detector in ArUco Marker Detection Using Non-GPS Drone,” in CRC Press eBooks, 2024, pp. 63–67.
	""")
	st.header("Conference Presentations")
	st.markdown("""
	1. **R.C.M. Caduyac** and J.F.R. Chan, "Comparative Analysis of Water Potability Prediction Based on Classical Machine Learning Algorithms and Artificial Neural Networks," presented at the International Science, Technology, and Engineering Conference (ISTEC), 2022.

	2. A.D. Sta. Cruz, J. Osayan, L.R. Moreno, and **R.C. Caduyac**, “Performance of ArUco Detector in ArUco Marker Detection Using Non-GPS Drone,” presented at the International Science, Technology, and Engineering Conference (ISTEC), 2022.

	3. **R.C.M. Caduyac**, J.P.A. Ramoso, J.P. Arazas, and R.C.V. Tomas, "The Effects of Feature Selection on Material’s Equivalent Circuit Visualization through Principal Component Analyis," presented at the 2nd International Conference on Engineering and Agro-Industrial Technology (iCEAT), 2023.

	4. **R.C.M. Caduyac**, J.P.A. Ramoso, J.P. Arazas, and R.C.V. Tomas, "Machine Learning-based Discrimination of Materials through Electrochemical Impedance Spectroscopy," presented at the 3rd International Conference on Engineering and Agro-Industrial Technology (iCEAT), 2024.
	""")



	
	























	