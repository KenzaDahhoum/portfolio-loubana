from flask import Flask, jsonify
from flask_cors import CORS
from models import db, Education, Experience, Project, Skill, Product, Ingredient, ProductImage

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()

    # Pre-populate products in the database
    db.session.query(Product).delete()
    db.session.query(Ingredient).delete()

    # Masque Oliban Miel
    masque = Product(
        title="Masque Oliban Miel",
        description="A revitalizing masque enriched with oliban and honey.",
        benefits="Hydrates, revitalizes, reduces acne scars, firms the skin.",
        how_to_use="Apply 2-3 times a week on clean skin. Leave for 15 minutes, then rinse thoroughly.",
        whatsapp_link="https://wa.me/1234567890",
        instagram_link="https://www.instagram.com/oliban_loubana/"
    )

    ingredients_masque = [
        Ingredient(name="Oliban extract", benefits="Antibacterial, anti-inflammatory, firms the skin", product=masque),
        Ingredient(name="Honey", benefits="Moisturizing, antibacterial, antioxidant", product=masque),
        Ingredient(name="Jojoba Oil", benefits="Deep hydration, balances oil production", product=masque),
        Ingredient(name="Sweet Almond Oil", benefits="Softens skin, reduces irritation", product=masque),
        Ingredient(name="Rose Oil", benefits="Soothes and rejuvenates skin", product=masque),
        Ingredient(name="Vitamin E", benefits="Protects skin, prevents aging", product=masque)
    ]

    masque_images = [
        ProductImage(image_url="/assets/images/masque-1.jpg", product=masque),
        ProductImage(image_url="/assets/images/masque-2.jpg", product=masque),
        ProductImage(image_url="/assets/images/masque-3.jpg", product=masque)
    ]
    
    # Crème Oliban
    creme = Product(
        title="Crème Oliban",
        description="A deeply hydrating night cream with oliban and precious oils.",
        benefits="Deep hydration, reduces wrinkles, brightens complexion.",
        how_to_use="Apply daily as a night cream to deeply moisturize your skin.",
        whatsapp_link="https://wa.me/1234567890",
        instagram_link="https://www.instagram.com/oliban_loubana/"
    )

    ingredients_creme = [
        Ingredient(name="Oliban extract", benefits="Antibacterial, anti-inflammatory", product=creme),
        Ingredient(name="Prickly Pear Oil", benefits="Rich in antioxidants, reduces wrinkles", product=creme),
        Ingredient(name="Jojoba Oil", benefits="Deep hydration", product=creme),
        Ingredient(name="Sweet Almond Oil", benefits="Softens skin", product=creme),
        Ingredient(name="Rose Water", benefits="Soothes and refreshes skin", product=creme),
        Ingredient(name="Vitamin E", benefits="Prevents aging", product=creme)
    ]

    creme_images = [
        ProductImage(image_url="/assets/images/creme-1.jpg", product=creme),
        ProductImage(image_url="/assets/images/creme-2.jpg", product=creme),
        ProductImage(image_url="/assets/images/creme-3.jpg", product=creme)
    ]

    # Tabrima
    tabrima = Product(
        title="Tabrima",
        description="A brightening oliban-based treatment to enhance skin radiance.",
        benefits="Unifies skin tone, smooths, and brightens.",
        how_to_use="Apply during your hammam ritual to exfoliate and rejuvenate the skin.",
        whatsapp_link="https://wa.me/1234567890",
        instagram_link="https://www.instagram.com/oliban_loubana/"
    )

    ingredients_tabrima = [
        Ingredient(name="Basil", benefits="Antibacterial, reduces acne", product=tabrima),
        Ingredient(name="Rose", benefits="Tones and softens skin", product=tabrima),
        Ingredient(name="Lavender", benefits="Calms and soothes skin", product=tabrima),
        Ingredient(name="Clove", benefits="Fights bacteria and acne", product=tabrima),
        Ingredient(name="Nila", benefits="Brightens skin", product=tabrima),
        Ingredient(name="Aker el Fassi", benefits="Brightens and evens skin tone", product=tabrima)
    ]

    tabrima_images = [
        ProductImage(image_url="/assets/images/tabrima-1.jpg", product=tabrima),
        ProductImage(image_url="/assets/images/tabrima-2.jpg", product=tabrima),
        ProductImage(image_url="/assets/images/tabrima-3.jpg", product=tabrima)
    ]

    db.session.add_all([masque, creme, tabrima])
    db.session.add_all(ingredients_masque + ingredients_creme + ingredients_tabrima)
    db.session.add_all(masque_images + creme_images + tabrima_images)
    db.session.commit()

# Endpoints for each product type
@app.route('/api/loubana/masque', methods=['GET'])
def get_masque():
    masque = Product.query.filter_by(title='Masque Oliban Miel').first()
    if masque:
        return jsonify({
            'title': masque.title,
            'description': masque.description,
            'benefits': masque.benefits,
            'how_to_use': masque.how_to_use,
            'whatsapp_link': masque.whatsapp_link,
            'instagram_link': masque.instagram_link,
            'ingredients': [{'name': i.name, 'benefits': i.benefits} for i in masque.ingredients],
            'images': ['/assets/images/IMG_masque-1.jpeg', '/assets/images/IMG_masque-2.jpeg', '/assets/images/IMG_masque-3.jpeg']
        })
    return jsonify({'message': 'Masque not found'}), 404

@app.route('/api/loubana/creme', methods=['GET'])
def get_creme():
    creme = Product.query.filter_by(title='Crème Oliban').first()
    if creme:
        return jsonify({
            'title': creme.title,
            'description': creme.description,
            'benefits': creme.benefits,
            'how_to_use': creme.how_to_use,
            'whatsapp_link': creme.whatsapp_link,
            'instagram_link': creme.instagram_link,
            'ingredients': [{'name': i.name, 'benefits': i.benefits} for i in creme.ingredients],
            'images': ['/assets/images/IMG_creme-1.jpeg', '/assets/images/IMG_creme-2.jpeg', '/assets/images/IMG_creme-3.jpeg']
        })
    return jsonify({'message': 'Crème not found'}), 404

@app.route('/api/loubana/tabrima', methods=['GET'])
def get_tabrima():
    tabrima = Product.query.filter_by(title='Tabrima').first()
    if tabrima:
        return jsonify({
            'title': tabrima.title,
            'description': tabrima.description,
            'benefits': tabrima.benefits,
            'how_to_use': tabrima.how_to_use,
            'whatsapp_link': tabrima.whatsapp_link,
            'instagram_link': tabrima.instagram_link,
            'ingredients': [{'name': i.name, 'benefits': i.benefits} for i in tabrima.ingredients],
            'images': ['/assets/images/tabrima.jpeg', '/assets/images/tabrima.jpeg', '/assets/images/tabrima.jpeg']
        })
    return jsonify({'message': 'Tabrima not found'}), 404



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
        location="Chichaoua",
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
