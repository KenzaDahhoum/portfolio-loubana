<template>
  <div class="portfolio-list">
    <b-container>
      <h2 class="section-title">My Recent Projects</h2>
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
            <b-img
              :src="project.image"
              alt="Project Image"
              class="project-image"
            />
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
import "aos/dist/aos.css";
import AOS from "aos";

export default {
  data() {
    return {
      projects: [
        {
          id: 1,
          title: "Personal Portfolio",
          description: "A web portfolio showcasing my work and journey.",
          images: [require("@/assets/images/screenshot_2024.png")],
        },
        {
          id: 2,
          title: "HRZen System",
          description:
            "An HR management system to manage employee records and events.",
          images: [
            require("@/assets/images/home-hrzen.png"),
            require("@/assets/images/add-emp.42d70c6a.png"),
            require("@/assets/images/add-event.527507b3.png"),
            require("@/assets/images/attendance-track.1b38c6da.png"),
            require("@/assets/images/login.d31e196e.png"),
          ],
        },
      ],
    };
  },
  mounted() {
    AOS.init({
      duration: 1200,
      once: true,
    });
  },
  methods: {
    viewProject(id) {
      this.$router.push({ name: "ProjectDetails", params: { id } });
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
  font-family: "Pacifico", cursive;
}

.projects-container {
  display: flex;
  justify-content: space-between;
}

.project-card {
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.project-card:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
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
  color: #ffd600;
}

.project-description {
  color: #666;
  font-size: 1rem;
}
</style>
