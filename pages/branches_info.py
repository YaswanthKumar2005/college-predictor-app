import streamlit as st

# Set the page configuration for a wider layout and a title
st.set_page_config(page_title="Branch Information", layout="wide")

# --- Custom CSS for Colours and Styles (Consistent with Home.py) ---
st.markdown("""
<style>
/* Main title style with gradient background */
.big-font {
    font-size: 48px !important;
    font-weight: bold;
    color: white;
    background-image: linear-gradient(to right, #4CAF50, #2196F3); /* Green to Blue Gradient */
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 20px;
}

/* Box for displaying the selected branch information */
.info-box {
    background-color: #FFFFFF; /* White background to stand out */
    border: 2px solid #00A9E0; /* Blue border, matching theme */
    border-radius: 10px;
    padding: 25px;
    margin-top: 20px;
    box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
}

/* Header for the branch name inside the info box */
.branch-title {
    font-size: 26px !important;
    font-weight: bold;
    color: #1A5276; /* Dark Blue */
    border-bottom: 2px solid #4CAF50; /* Green accent line */
    padding-bottom: 10px;
    margin-bottom: 15px;
}

/* Style for the labels like 'Description' */
.info-label {
    font-size: 18px !important;
    font-weight: bold;
    color: #1A5276;
}
</style>
""", unsafe_allow_html=True)

# Use markdown for the styled title
st.markdown('<p class="big-font">⚙️ Engineering Branches Overview</p>', unsafe_allow_html=True)

st.markdown("Explore different engineering branches, their focus areas, and career growth opportunities. Select a branch from the dropdown below to learn more.")

# [cite_start]Comprehensive dictionary of engineering branch information [cite: 1]
branch_info = {
    "AGR": {"name": "Agricultural Engineering", "description": "Focuses on applying engineering principles to agriculture. It involves designing agricultural machinery, soil and water conservation, irrigation systems, and food processing.", "career": "Careers in agri-tech companies, food processing industries, farm equipment manufacturing, irrigation departments, and agricultural research."},
    "AI": {"name": "Artificial Intelligence", "description": "A dedicated program on the theory and development of computer systems that can perform tasks requiring human intelligence, such as visual perception, speech recognition, and decision-making.", "career": "Job roles as an AI Specialist, Machine Learning Engineer, Natural Language Processing (NLP) Engineer, Computer Vision Engineer, and AI Research Scientist."},
    "AID": {"name": "Artificial Intelligence and Data Science", "description": "An integrated discipline focusing on AI algorithms, machine learning models, and data science techniques to analyze and extract actionable insights from large datasets.", "career": "Opportunities as a Data Scientist, AI Engineer, Business Intelligence (BI) Analyst, Data Analyst, and Machine Learning Scientist."},
    "AIM": {"name": "Artificial Intelligence and Machine Learning", "description": "Focuses on the core concepts of creating intelligent systems. It covers algorithms, neural networks, deep learning, natural language processing, and computer vision in depth.", "career": "Career paths include AI/ML Engineer, Research Scientist, NLP Specialist, Robotics Engineer, and AI-driven product development."},
    "ASE": {"name": "Aerospace Engineering", "description": "Involves the design, development, testing, and production of aircraft, spacecraft, satellites, and missiles. It is split into aeronautical and astronautical engineering.", "career": "Careers in aerospace and defense companies (like ISRO, DRDO, HAL), airlines, and R&D organizations as a Design Engineer, Analyst, or Scientist."},
    "AUT": {"name": "Automobile Engineering", "description": "A branch of mechanical engineering that focuses on the design, manufacturing, and operation of automobiles, including cars, trucks, and motorcycles.", "career": "Opportunities in automotive manufacturing companies, design studios, and R&D centers as an Automotive Design Engineer, Production Engineer, or Vehicle Dynamics Engineer."},
    "BDT": {"name": "Big Data Analytics", "description": "A specialized field focusing on the tools, techniques, and algorithms required to process, analyze, and visualize extremely large and complex datasets (Big Data).", "career": "Job roles include Big Data Engineer, Data Architect, Data Scientist, and Analytics Consultant in tech, finance, and e-commerce sectors."},
    "BIO": {"name": "Bio-Technology", "description": "Uses biological systems and living organisms to develop or create products. It involves genetic engineering, bioprocess engineering, and immunology.", "career": "Careers as a Research Scientist, Biotechnologist, or Quality Control Officer in pharmaceutical, agricultural, healthcare, and food industries."},
    "CAD": {"name": "Computer Aided Design", "description": "Focuses on the use of computer systems to assist in the creation, modification, analysis, or optimization of a design, often as a specialization in Mechanical or Civil engineering.", "career": "Opportunities as a CAD Designer, Design Engineer, Product Design Engineer, and Architectural Drafter across various engineering domains."},
    "CAI" : {"name": "Computer Science and Engineering (Artificial Intelligence)", "description": "Integrates core Computer Science principles with a specialization in AI models, neural networks, expert systems, and intelligent applications.", "career": "Careers as an AI Specialist, Machine Learning Engineer, NLP Engineer, and Software Developer for AI-based products."},
    "CBA" : {"name": "Computer Science and Business Analytics", "description": "A hybrid program that combines computer science fundamentals with business principles, data analysis, and statistical methods to drive strategic business decisions.", "career": "Roles like Business Analyst, Data Analyst, BI Consultant, and Technical Product Manager in corporate and tech sectors."},
    "CBC": {"name": "Computer Science and Engineering (Block Chain Technology)", "description": "A CSE specialization centered on decentralized systems, cryptography, and the architecture of blockchain platforms like Bitcoin and Ethereum.", "career": "Opportunities as a Blockchain Developer, Smart Contract Developer, Cryptocurrency Analyst, and Security Specialist."},
    "CCC": {"name": "Computer and Communication Engineering", "description": "A blend of computer science and communication engineering, focusing on the design and management of computer networks, telecommunication systems, and mobile computing.", "career": "Job roles as a Network Architect, Telecommunication Specialist, Systems Engineer, and Network Security Engineer."},
    "CDA": {"name": "Computer Science and Engineering (Data Analytics)", "description": "A CSE specialization that emphasizes statistical analysis, data mining, and data visualization techniques to extract actionable insights from business data.", "career": "Careers as a Data Analyst, Business Intelligence Analyst, Data Scientist, and Data Engineer."},
    "CHE": {"name": "Chemical Engineering", "description": "Applies principles of chemistry, physics, and biology to design and operate processes for converting raw materials into valuable products like fuels, medicines, and plastics.", "career": "Careers as a Process Engineer, Chemical Plant Manager, or Product Development Scientist in industries like pharma, energy, and FMCG."},
    "CIA": {"name": "Computer Science and Engineering (Artificial Intelligence)", "description": "A CSE specialization that provides a deep dive into AI concepts, covering machine learning, knowledge representation, problem-solving, and expert systems.", "career": "Careers as an AI Developer, Machine Learning Engineer, Data Scientist, and R&D Engineer in artificial intelligence."},
    "CIC": {"name": "Computer Science and Engineering (Cyber Security)", "description": "Combines core CS principles with a specialization in protecting computer systems and networks. It covers cryptography, ethical hacking, and digital forensics.", "career": "Job roles like Cybersecurity Analyst, Security Engineer, Penetration Tester, and Information Security Manager."},
    "CIT": {"name": "Computer and Information Technology", "description": "A broad field covering computer systems, networking, and software applications, often with a more practical, hands-on approach than theoretical computer science.", "career": "Careers as a Systems Analyst, IT Support Specialist, Network Engineer, and Web Developer."},
    "CIV": {"name": "Civil Engineering", "description": "Focused on planning, designing, constructing, and maintaining infrastructure like buildings, roads, bridges, canals, and dams.", "career": "Career opportunities in construction management, urban planning, structural engineering, government services (like PWD), and environmental consulting."},
    "CN": {"name": "Computer Networking", "description": "A specialization focusing on the design, implementation, and management of computer networks, including Local Area Networks (LAN), Wide Area Networks (WAN), and the Internet.", "career": "Jobs as a Network Engineer, Network Administrator, Cloud Networking Specialist, and Network Security Analyst."},
    "CS": {"name": "Computer Science", "description": "Focuses on the theoretical foundations of information and computation. It covers algorithms, data structures, programming languages, and the theory of computation.", "career": "Prime roles in software development, research and development (R&D), algorithm design, and system architecture."},
    "CSB": {"name": "Computer Science and Biosciences", "description": "An interdisciplinary branch combining computation with biological sciences to solve problems in genomics, bioinformatics, and computational biology.", "career": "Careers as a Bioinformatician, Computational Biologist, and Research Scientist in biotech firms and pharmaceutical labs."},
    "CSBS": {"name": "Computer Science and Business Systems", "description": "A unique curriculum blending computer science with management, business fundamentals, and humanities to prepare students for strategic IT roles.", "career": "Jobs as a Business Analyst, IT Consultant, Systems Analyst, and Product Manager who can bridge the gap between tech and business."},
    "CSC": {"name": "Computer Science and Communication Engineering", "description": "Integrates computer science with communication principles, focusing on computer networks, mobile communication protocols, and distributed computing systems.", "career": "Opportunities as a Network Architect, Telecommunications Engineer, Systems Engineer, and Cloud Communication Specialist."},
    "CSD": {"name": "Computer Science and Design", "description": "Blends computer science principles with design thinking, focusing on User Interface (UI), User Experience (UX), Human-Computer Interaction (HCI), and product design.", "career": "Careers as a UI/UX Designer, Product Manager, Front-end Developer, and Interaction Designer."},
    "CSE": {"name": "Computer Science and Engineering", "description": "Focuses on programming, algorithms, data structures, and software development. Core to all technology and IT industries.", "career": "Careers in software development, data science, AI, machine learning, cybersecurity, and cloud computing."},
    "CSEB": {"name": "Computer Science and Engineering (Big Data Analytics)", "description": "A CSE specialization that provides expertise in the architecture, tools, and algorithms required to process and analyze massive datasets for valuable insights.", "career": "Job roles include Big Data Engineer, Data Architect, Data Scientist, and Analytics Engineer."},
    "CSER": {"name": "Computer Science Engineering (Regional Language)", "description": "Delivers the standard CSE curriculum in a regional language to improve accessibility and understanding for students from diverse linguistic backgrounds.", "career": "Same career paths as CSE, with additional opportunities in localization, regional tech content development, and government digital initiatives."},
    "CSG": {"name": "Computer Science and Engineering (Gaming and Graphics)", "description": "Combines core CS with specialized skills in computer graphics, game design, physics engines, virtual reality (VR), and augmented reality (AR).", "career": "Careers as a Game Developer, Graphics Programmer, AR/VR Developer, and Game Designer in the entertainment and simulation industries."},
    "CSM": {"name": "Computer Science and Engineering (AI & Machine Learning)", "description": "A specialization within CSE that deeply covers AI concepts, neural networks, deep learning, and the application of ML in solving complex problems.", "career": "Jobs as a Machine Learning Engineer, AI Research Scientist, Computer Vision Engineer, and Data Scientist."},
    "CSO": {"name": "Computer Science and Engineering (IoT and Cyber Security with Blockchain)", "description": "A highly specialized field combining IoT device programming, network security for connected devices, and decentralized security using blockchain technology.", "career": "Roles like IoT Security Specialist, Blockchain Developer, Embedded Security Engineer, and Secure Systems Architect."},
    "CSS": {"name": "Computer Science and Systems Engineering", "description": "Integrates computer science with systems engineering principles to design, develop, and manage the lifecycle of large-scale, complex software and hardware systems.", "career": "Careers as a Systems Engineer, Systems Architect, Integration Engineer, and Technical Program Manager."},
    "CST": {"name": "Computer Science and Technology", "description": "A broad, application-oriented branch covering software development, computer networking, database management, and IT infrastructure.", "career": "Careers as a Software Developer, Systems Analyst, IT Manager, and Database Administrator."},
    "CSW": {"name": "Computer Science and Engineering (Software Engineering)", "description": "A specialization within CSE that emphasizes the systematic design, development, testing, and maintenance of robust and scalable software systems.", "career": "Job roles like Software Engineer, DevOps Engineer, Quality Assurance Engineer, and Application Developer."},
    "DS": {"name": "Data Science", "description": "An interdisciplinary field that uses scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data.", "career": "Careers as a Data Scientist, Data Analyst, Machine Learning Engineer, and Business Intelligence Developer."},
    "EBM": {"name": "Electronics and Biomedical Engineering", "description": "Applies electronic engineering principles and design concepts to medicine and biology for healthcare purposes, such as designing medical devices and diagnostic tools.", "career": "Careers as a Biomedical Engineer, Medical Device Designer, Clinical Engineer, and R&D Scientist in healthcare technology."},
    "ECA": {"name": "Electronics and Computer Engineering", "description": "A hybrid field merging electronics engineering with computer science, covering hardware design, microprocessors, embedded systems, and software development.", "career": "Careers as an Embedded Systems Engineer, Hardware Engineer, Firmware Developer, and IoT device specialist."},
    "ECE": {"name": "Electronics and Communication Engineering", "description": "Deals with the design and development of electronic circuits, communication equipment like transmitters, receivers, and integrated circuits (ICs).", "career": "Job roles in embedded systems, telecommunications, Very Large Scale Integration (VLSI), Internet of Things (IoT), and signal processing."},
    "ECES": {"name": "Electronics and Communication Engineering (Embedded Systems)", "description": "An ECE specialization focusing on the design of computer hardware and software systems that are embedded within larger mechanical or electrical systems.", "career": "Job opportunities as an Embedded Software Engineer, Firmware Engineer, and IoT Device Engineer."},
    "ECM": {"name": "Electronics and Computer Engineering", "description": "An integrated discipline that covers electronic devices, circuits, computer architecture, and software, bridging the gap between hardware and software.", "career": "Jobs as a Hardware Engineer, Firmware Developer, and Systems-on-Chip (SoC) Designer."},
    "ECT": {"name": "Electronics and Computer Technology", "description": "A practical, technology-oriented program covering digital electronics, microprocessors, computer hardware assembly, and networking fundamentals.", "career": "Job roles as a Hardware Technician, Network Support Specialist, and Test Engineer."},
    "ECV": {"name": "Electronics and Communication Engineering (VLSI Design)", "description": "An ECE specialization focused on Very Large Scale Integration (VLSI), which is the process of creating integrated circuits (chips) by combining thousands of transistors.", "career": "Careers as a VLSI Design Engineer, Verification Engineer, and Chip Designer in the semiconductor industry."},
    "EEE": {"name": "Electrical and Electronics Engineering", "description": "Covers the generation, transmission, and distribution of electrical power, as well as the fundamentals of electronic devices and circuits.", "career": "Career paths in power systems, automation, electric vehicles (EVs), renewable energy, and control systems."},
    "EIE": {"name": "Electronics and Instrumentation Engineering", "description": "Focuses on the design and application of measurement instruments, sensors, and control systems, bridging the gap between electronics and instrumentation.", "career": "Jobs as an Instrumentation Engineer, Control Systems Engineer, or Automation Engineer in manufacturing and process industries."},
    "EII": {"name": "Electronics Instrumentation & Control Engineering", "description": "An integrated course covering the principles of electronics, measurement instrumentation, and control systems for industrial automation and process control.", "career": "Careers as a Control and Instrumentation Engineer, Automation Engineer, and Process Control Specialist."},
    "EVT": {"name": "Environmental Engineering", "description": "Applies science and engineering principles to improve and maintain the environment. It includes water and air pollution control, recycling, and waste disposal.", "career": "Careers as an Environmental Consultant, Water Treatment Specialist, and Sustainability Officer for corporations and government agencies."},
    "FDE": {"name": "Food Engineering", "description": "A multidisciplinary field combining microbiology, applied physical sciences, chemistry, and engineering for food processing and related industries.", "career": "Opportunities as a Food Process Engineer, Packaging Engineer, and R&D Scientist in the food and beverage sector."},
    "FDT": {"name": "Food Technology", "description": "Applies food science to the selection, preservation, processing, packaging, and distribution of safe and nutritious food products.", "career": "Jobs as a Food Technologist, Quality Control Manager, or Product Development Scientist in the food manufacturing industry."},
    "GDT": {"name": "Graphics and Digital Technology", "description": "Focuses on computer graphics, digital image processing, and visualization technologies used in gaming, digital media, and scientific simulations.", "career": "Careers as a Graphics Programmer, Digital Artist, and AR/VR Developer."},
    "GIN": {"name": "Geoinformatics Engineering", "description": "Deals with the science and technology of geographically referenced information. It includes Geographic Information Systems (GIS), remote sensing, and cartography.", "career": "Job opportunities as a GIS Analyst, Remote Sensing Specialist, and Geospatial Data Scientist."},
    "INF": {"name": "Information Technology", "description": "Focuses on the application of computers and telecommunications to store, retrieve, transmit, and manipulate data, emphasizing networking, system administration, and IT infrastructure.", "career": "Careers as an IT Consultant, Network Administrator, Cloud Engineer, and Database Administrator."},
    "IOT": {"name": "Internet of Things", "description": "Focuses on the design and development of interconnected smart devices. It covers sensors, networking protocols, cloud computing, and data analytics for IoT applications.", "career": "Job roles include IoT Developer, Embedded Systems Engineer, and IoT Solutions Architect."},
    "IST": {"name": "Information Science and Technology", "description": "A broad field concerned with the analysis, collection, classification, storage, and retrieval of information, blending aspects of IT and computer science.", "career": "Careers as an Information Architect, Systems Analyst, Database Administrator, and UX Researcher."},
    "MAD": {"name": "Machine Learning and Data Analytics", "description": "An integrated program focusing on machine learning algorithms and their practical application in data analytics to build predictive models and solve business problems.", "career": "Careers as a Machine Learning Engineer, Data Analyst, and Data Scientist."},
    "MAU": {"name": "Mechatronics and Automation Engineering", "description": "A synergetic field combining mechanical engineering, electronics, computer science, and control engineering for designing advanced automated systems.", "career": "Jobs as a Mechatronics Engineer, Automation Engineer, and Robotics Engineer."},
    "MEC": {"name": "Mechanical Engineering", "description": "Involves mechanics, kinematics, thermodynamics, and material science for designing and analyzing mechanical systems.", "career": "Opportunities in manufacturing, automotive, aerospace, and robotics industries."},
    "MET": {"name": "Metallurgical Engineering", "description": "Focuses on the study of the physical and chemical behavior of metallic elements, their inter-metallic compounds, and their mixtures (alloys).", "career": "Careers as a Metallurgist, Materials Engineer, or Process Engineer in the steel and metal fabrication industries."},
    "MII": {"name": "Manufacturing Engineering", "description": "Focuses on the design and optimization of manufacturing processes, systems, and equipment to produce high-quality goods efficiently.", "career": "Careers as a Manufacturing Engineer, Process Engineer, and Industrial Engineer."},
    "MIN": {"name": "Mining Engineering", "description": "Deals with the extraction of minerals from the earth. It involves mine design, safety protocols, and environmental management.", "career": "Jobs as a Mining Engineer, Operations Manager in mining companies, and Geotechnical Engineer."},
    "MMM": {"name": "Materials and Metallurgical Engineering", "description": "Focuses on the study of the structure, properties, and processing of various materials, including metals, ceramics, polymers, and composites.", "career": "Careers as a Materials Scientist, Metallurgist, and Process Engineer."},
    "MMT": {"name": "Multimedia Technology", "description": "Deals with creating and processing interactive content, including graphics, audio, video, and animation for web, mobile, and entertainment industries.", "career": "Careers as a Multimedia Developer, Animator, UI/UX Designer, and VFX Artist."},
    "MRB": {"name": "Mechatronics and Robotics", "description": "A specialized field combining mechanical, electrical, and computer engineering to design, build, and operate robots and other automated systems.", "career": "Jobs as a Robotics Engineer, Automation Engineer, and Control Systems Engineer."},
    "NAM": {"name": "Naval Architecture and Marine Engineering", "description": "Involves the design, construction, and maintenance of ships, boats, and other marine vessels and offshore structures.", "career": "Careers as a Naval Architect, Marine Engineer, and Shipyard Project Manager."},
    "PEE": {"name": "Power Electronics Engineering", "description": "Focuses on the application of solid-state electronics for the control and conversion of electric power. It is key for electric vehicles, renewable energy, and power supplies.", "career": "Jobs as a Power Electronics Engineer and Design Engineer for EVs, solar inverters, and power control systems."},
    "PET": {"name": "Petroleum Engineering", "description": "Concerns the production of hydrocarbons, such as crude oil and natural gas. It involves drilling, reservoir engineering, and production operations.", "career": "Careers as a Reservoir Engineer, Drilling Engineer, or Production Engineer in oil and gas companies."},
    "PHM": {"name": "Pharmaceutical Engineering", "description": "Focuses on the design, construction, and operation of manufacturing facilities for pharmaceuticals, combining chemical engineering with pharmaceutical sciences.", "career": "Jobs as a Process Engineer (Pharma), Quality Assurance Manager, and Validation Engineer."},
    "RBT": {"name": "Robotics", "description": "A dedicated branch for the design, construction, operation, and application of robots, as well as the computer systems for their control and sensory feedback.", "career": "Careers as a Robotics Engineer, Automation Engineer, and AI/ML Engineer for robotic systems."},
    "SWE": {"name": "Software Engineering", "description": "A dedicated branch focusing on the principles and practices of designing, developing, testing, deploying, and maintaining large-scale software systems.", "career": "Job roles like Software Engineer, DevOps Engineer, Full-Stack Developer, and QA Engineer."}
}

# Create a list of branches for the dropdown, including a placeholder
branch_options = ['--Select--'] + sorted(branch_info.keys())

# Create a dropdown (select box) for the user to choose a branch.
selected_branch_key = st.selectbox(
    "Select a Branch to View Details",
    branch_options
)

# Display the information for the selected branch inside the styled box
if selected_branch_key and selected_branch_key != '--Select--':
    info = branch_info[selected_branch_key]
    st.markdown(f"""
    <div class="info-box">
        <p class="branch-title">{info['name']} ({selected_branch_key})</p>
        <p class="info-label">Description</p>
        <p>{info['description']}</p>
        <br>
        <p class="info-label">Career Growth</p>
        <p>{info['career']}</p>
    </div>
    """, unsafe_allow_html=True)


# Add a footer
st.markdown("---")
st.markdown("This information is for general guidance. Course curricula and career outcomes may vary by university.")
