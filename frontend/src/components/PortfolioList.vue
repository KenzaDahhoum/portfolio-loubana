<template>
  <div class="portfolio-list">
    <b-container>
      <h2 class="section-title">My Projects</h2>
      <b-row class="projects-container">
        <b-col
          v-for="project in projects"
          :key="project.id"
          cols="12"
          md="6"
          lg="4"
          class="project-card"
          data-aos="fade-up"
          @click="viewProject(project.id)"
        >
          <b-card no-body class="mb-4">
            <b-img :src="project.image" alt="Project Image" class="project-image" />
            <b-card-body>
              <h3 class="project-title">{{ project.title }}</h3>
              <p class="project-description">{{ project.description }}</p>
            </b-card-body>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import 'aos/dist/aos.css';
import AOS from 'aos'; 

export default {
  data() {
    return {
      projects: [
        {
          id: 1,
          title: 'Project One',
          description: 'A brief description of this project.',
          image: '/path/to/image1.jpg',
        },
        {
          id: 2,
          title: 'Project Two',
          description: 'A brief description of this project.',
          image: '/path/to/image2.jpg',
        },
     
      ],
    };
  },
  mounted() {
    AOS.init(); 
  },
  methods: {
    viewProject(id) {
      console.log(`Navigating to project ${id}`);
    },
  },
};
</script>

<style scoped>
.portfolio-list {
  text-align: center;
  margin: 40px auto;
}

.section-title {
  font-size: 2.5rem;
  margin-bottom: 30px;
  font-weight: bold;
}

.projects-container {
  display: flex;
  justify-content: space-between;
}

.project-card {
  cursor: pointer;
  transition: transform 0.3s ease-in-out;
}

.project-card:hover {
  transform: scale(1.05);
}

.project-image {
  width: 100%;
  height: auto;
  object-fit: cover;
  border-radius: 10px;
}

.project-title {
  font-size: 1.5rem;
  margin: 15px 0 10px;
  font-weight: 600;
}

.project-description {
  color: #666;
}
</style>
