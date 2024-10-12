from flask import Flask, jsonify
from flask_cors import CORS
from models import db, Education, Experience, Project, Skill

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()

# Pre-populating education, experience, skills, and projects

with app.app_context():
    # Clear the database before adding
    db.session.query(Education).delete()
    db.session.query(Experience).delete()
    db.session.query(Project).delete()
    db.session.query(Skill).delete()

    # Adding education records
    education1 = Education(
        institution="ALX Africa",
        degree="Software Engineer",
        field_of_study="Informatique",
        start_date="April 2023",
        end_date="November 2024"
    )
    education2 = Education(
        institution="ISGI Marrakech",
        degree="Technicien spécialisé",
        field_of_study="Développement informatique",
        start_date="2018",
        end_date="2020"
    )
    education3 = Education(
        institution="Ibn el Arabi",
        degree="Baccalauréat",
        field_of_study="Sciences expérimentales",
        start_date="2017",
        end_date="2018"
    )

    db.session.add_all([education1, education2, education3])

    # Adding experience records
    experience1 = Experience(
        company="DIGISBAI",
        position="Web Developer",
        start_date="March 2022",
        end_date="Present",
        location="Remote",
        description="Full-time web developer working remotely."
    )
    experience2 = Experience(
        company="Haku Expertise",
        position="Frontend Developer",
        start_date="May 2021",
        end_date="February 2022",
        location="Rabat, Morocco",
        description="Internship as a frontend developer."
    )
    experience3 = Experience(
        company="Province Chichaoua",
        position="Web Developer",
        start_date="February 2020",
        end_date="July 2020",
        location="Morocco",
        description="Internship focusing on web development."
    )
    # Adding call center experiences
    experience4 = Experience(
        company="Digisell",
        position="Téléconseillère francophone",
        start_date="May 2022",
        end_date="October 2022",
        location="Kénitra, Morocco",
        description="Effectuer des appels sortants aux clients potentiels, communiquer sur les nouvelles offres, fidélisation des clients, et atteindre les objectifs quantitatifs et qualitatifs."
    )
    experience5 = Experience(
        company="MH Groupe",
        position="Téléconseillère francophone",
        start_date="October 2020",
        end_date="January 2021",
        location="Marrakech, Morocco",
        description="Effectuer des appels sortants aux clients potentiels, communiquer sur les nouvelles offres, fidélisation des clients, et atteindre les objectifs quantitatifs et qualitatifs."
    )

    db.session.add_all([experience1, experience2, experience3, experience4, experience5])

    # Adding skills records (Tools, Programming Languages, Soft Skills, Design Skills)
    skills = [
        Skill(name="JavaScript", category="Tools and Technology"),
        Skill(name="Vue.js", category="Tools and Technology"),
        Skill(name="HTML5", category="Tools and Technology"),
        Skill(name="CSS", category="Tools and Technology"),
        Skill(name="Git", category="Tools and Technology"),
        Skill(name="GitHub", category="Tools and Technology"),
        Skill(name="GitLab", category="Tools and Technology"),
        Skill(name="Vuex", category="Tools and Technology"),
        Skill(name="Nuxt.js", category="Tools and Technology"),
        Skill(name="Figma", category="Tools and Technology"),
        Skill(name="JavaScript", category="Programming Languages"),
        Skill(name="HTML5", category="Programming Languages"),
        Skill(name="CSS", category="Programming Languages"),
        Skill(name="PHP", category="Programming Languages"),
        Skill(name="Problem Solving", category="Soft Skills"),
        Skill(name="Debugging", category="Soft Skills"),
        Skill(name="Organization Skills", category="Soft Skills"),
        Skill(name="Teamwork", category="Soft Skills"),
        Skill(name="Remote Work", category="Soft Skills"),
        Skill(name="Responsive Web Design", category="Design Skills"),
        Skill(name="UX Design", category="Design Skills"),
        Skill(name="Agile Development", category="Design Skills"),
        Skill(name="Front-End Design", category="Design Skills"),
        Skill(name="Linux Terminal", category="Tools and Technology"),
        Skill(name="Powershell", category="Tools and Technology"),
    ]

    db.session.add_all(skills)

    # Adding project records
    project1 = Project(
        title="HRZen Management System",
        description="An HR management system developed during my ALX Africa journey. It helps to manage employee records, attendance, and events.",
        technologies="Python (Flask), Vue.js, PostgreSQL",
        link="https://github.com/KenzaDahhoum/portfolio-project"
    )
    project2 = Project(
        title="Frontend for Real Estate Platform",
        description="Developed the frontend of a real estate management platform during my internship at Haku Expertise.",
        technologies="Vue.js, HTML, CSS",
        link=""
    )
    project3 = Project(
        title="Chichaoua Web Development Project",
        description="Worked on a web application for the local government during my internship at Province Chichaoua.",
        technologies="HTML, CSS, JavaScript, GitLab",
        link=""
    )
    project4 = Project(
        title="DIGISBAI Web Development",
        description="Ongoing web development projects at DIGISBAI, focusing on full-stack development.",
        technologies="JavaScript, Vue.js, PHP",
        link=""
    )

    db.session.add_all([project1, project2, project3, project4])

    db.session.commit()

# API Endpoints
@app.route('/api/education', methods=['GET'])
def get_education():
    education_records = Education.query.all()
    return jsonify([{
        'institution': record.institution,
        'degree': record.degree,
        'field_of_study': record.field_of_study,
        'start_date': record.start_date,
        'end_date': record.end_date
    } for record in education_records])

@app.route('/api/experience', methods=['GET'])
def get_experience():
    experience_records = Experience.query.all()
    return jsonify([{
        'company': record.company,
        'position': record.position,
        'start_date': record.start_date,
        'end_date': record.end_date,
        'location': record.location,
        'description': record.description
    } for record in experience_records])

@app.route('/api/projects', methods=['GET'])
def get_projects():
    project_records = Project.query.all()
    return jsonify([{
        'title': record.title,
        'description': record.description,
        'technologies': record.technologies,
        'link': record.link
    } for record in project_records])

@app.route('/api/skills', methods=['GET'])
def get_skills():
    skill_records = Skill.query.all()
    return jsonify([{
        'name': record.name,
        'category': record.category
    } for record in skill_records])

if __name__ == '__main__':
    app.run(debug=True)
