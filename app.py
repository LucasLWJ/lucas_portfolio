from flask import Flask, render_template, url_for, jsonify
from dataclasses import dataclass
from typing import List, Dict

app = Flask(__name__)

@dataclass
class ProjectImage:
    url: str
    caption: str

@dataclass
class Project:
    title: str
    description: str
    image_url: str
    technologies: List[str]
    project_images: List[ProjectImage]
    github_url: str = None
    live_url: str = None

@dataclass
class Experience:
    company: str
    position: str
    date: str
    responsibilities: List[str]
    technologies: List[str]

# Example project with multiple images
projects = [
    Project(
        title="Healthcare Product Design: Clean Cue",
        description="An ESP32-based solution designed to improve hand-hygiene compliance rates in hospital wards",
        image_url="static/images/project1.png",
        technologies=["ESP32 Programming", "Fusion360", "Circuit Design", "FDM 3D printing", "MedTech"],
        project_images=[
            ProjectImage("static/images/cleancue1.png", "First feature: Login screen"),
            ProjectImage("static/images/cleancue2.png", "Second feature: Dashboard"),
            ProjectImage("static/images/cleancue3.png", "Third feature: Settings page"),
            ProjectImage("static/images/cleancue4.png", "Third feature: Settings page"),
        ],
        live_url="https://www.youtube.com/watch?v=GjOuKQfj_LY"
    ),
    Project(
        title="Intelligent Robotics: Autonomous Navigation and Object Recognition ",
        description="Simultaneous mapping and exploring mazes with frontier-based navigation and YOLOv8",
        image_url="static/images/project2.jpg",
        technologies=["ROS2", "Python", "Yolov8"],
        project_images=[
            ProjectImage("static/images/IR1.png", "First feature: Login screen"),
            ProjectImage("static/images/IR2.png", "Second feature: Dashboard"),
            ProjectImage("static/images/IR3.png", "Third feature: Settings page"),
            ProjectImage("static/images/IR4.png", "Third feature: Settings page"),
        ],
        #github_url="https://github.com/yourusername/project1"
    ),
    Project(
        title="EEG-Based Drowsiness Detection System",
        description="An EEG-based system to detect driver fatigue on long-haul journeys",
        image_url="static/images/project3.png",
        technologies=["LabVIEW", "Circuit Design", "MedTech"],
        project_images=[
            ProjectImage("static/images/nycu1.png", "First feature: Login screen"),
            ProjectImage("static/images/nycu2.png", "Second feature: Dashboard"),
            ProjectImage("static/images/nycu3.png", "Third feature: Settings page"),
            ProjectImage("static/images/nycu4.png", "Third feature: Settings page"),
        ],
        github_url="https://docs.google.com/document/d/1OZo14LgqF7d9JaB9Fbqc9qf92bZmHndHs69aX7sxdps/edit?usp=sharing"
    ),
    Project(
        title="Machine Learning - Predicting Candidemia In Patients ",
        description="Building a classifier that uses patient health data to predict Candidemia, a type of bloodstream infection",
        image_url="static/images/project4.png",
        technologies=["Python"],
        project_images=[
            ProjectImage("static/images/ml1.png", "First feature: Login screen"),
            ProjectImage("static/images/ml2.png", "Second feature: Dashboard"),
            ProjectImage("static/images/ml3.png", "Third feature: Settings page"),
            ProjectImage("static/images/ml4.png", "First feature: Login screen"),
            ProjectImage("static/images/ml5.png", "Second feature: Dashboard"),
            ProjectImage("static/images/ml6.png", "Third feature: Settings page"),
        ],
        github_url="https://docs.google.com/document/d/1NYy9BGAL-Q2CWr24sKECaAB5gTUkb_T8_a77jNrJ93Y/edit?tab=t.0"
    ),
    Project(
        title="L-ILY - Interactive Robotic Desktop Flower",
        description="Bridging distances with grace—hand gestures that bring flowers to life, keeping love in motion",
        image_url="static/images/project5.png",
        technologies=["Jetson Nano", "Firebase Server", "Arduino"],
        project_images=[
            ProjectImage("static/images/lily1.png", "First feature: Login screen"),
        ],
        live_url="https://www.canva.com/design/DAGd3QqtUMs/FmYnIaS4k7GgInswFFYDEA/edit?utm_content=DAGd3QqtUMs&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton"
    ),
]

@app.route('/')
def home():
    return render_template('home.html', projects=projects)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)


experiences = [
    Experience(
        company="Changi General Hospital Office of Innovation (OOI)",
        position="Product Design Intern",
        date="Feb 2024 - Aug 2024",
        responsibilities=[
                'Worked with a senior consultant anesthetist to prototype a novel medical device using Solidworks to facilitate anesthesia application and endotracheal intubation, simplifying the intubation process and improving procedural efficiency',
                'Worked with the OOI R&D team to design and prototype a tendon-operated grasping mechanism using SLA 3D printing, streamlining the design for a Pharyngeal Imaging Forceps prototype for airway foreign object retrieval',
                'Conducted market scans for four medical device projects, evaluating their value and viability in the local market, and providing strategic recommendations to the OOI team that guided product development decisions'
        ],
        technologies=["Solidworks", "SLA Printing", "3D Bioprinting", "Medical Device R&D", "Market Analysis & Product Strategy"],
    ), 
    Experience(
        company="Defence Science Organisation (DSO)",
        position="Intern",
        date="Apr 2019 - Jun 2019",
        responsibilities=[
                'Designed and developed a smartphone application to seamlessly interface with an existing defense platform, enhancing field status and health monitoring capabilities',
                'Delivered a fully functional demonstration of the smartphone application to stakeholders within just two months, showcasing rapid adaptability and efficiency in an R&D setting',
        ],
        technologies=["Mobile App Development", "USB and UART Interfacing"],
    )     
]

@app.route('/experience')
def experience():
        return render_template('experience.html', experiences=experiences)


@app.route('/contact')
def contact():
    return render_template('contact.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)