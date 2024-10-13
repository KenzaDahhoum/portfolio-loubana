<template>
    <div class="section experience-section">
      <h2>Experience</h2>
      <ul>
        <li 
          v-for="(experience, index) in sortedExperiences" 
          :key="experience.id" 
          class="experience-card"
          :data-aos="index % 2 === 0 ? 'zoom-in-left' : 'zoom-in-right'"
          data-aos-duration="1000"
        >
          <div class="header">
            <div class="company-position">
              <i class="fas fa-building company-icon"></i>
              <strong class="company">{{ experience.company }}</strong>
              <span class="position"> - {{ experience.position }}</span>
            </div>
            <div class="duration">
              <i class="fas fa-calendar-alt"></i>
              <span>{{ formatDuration(experience.start_date, experience.end_date) }}</span>
            </div>
          </div>
          <div class="details">
            <div class="location">
              <i class="fas fa-map-marker-alt"></i>
              <strong>Location:</strong> {{ experience.location }}
            </div>
            <div class="description">
              <i class="fas fa-info-circle"></i>
              <strong>Description:</strong> {{ experience.description }}
            </div>
          </div>
        </li>
      </ul>
    </div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';
import AOS from 'aos';
import 'aos/dist/aos.css';

export default {
  data() {
    return {
      experiences: [],
    };
  },
  computed: {
    sortedExperiences() {
      return [...this.experiences].sort((a, b) => {
        if (a.end_date === 'Present') return -1;
        if (b.end_date === 'Present') return 1;
        return new Date(b.end_date) - new Date(a.end_date);
      });
    },
  },
  mounted() {
    this.fetchExperience();
    AOS.init({
      duration: 1000, // Global duration for animations
      easing: 'ease',
      once: true,
    });
  },
  updated() {
    AOS.refresh();
  },
  methods: {
    async fetchExperience() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/experience');
        this.experiences = response.data;
      } catch (error) {
        console.error('Error fetching experience data', error);
      }
    },
    formatDuration(startDate, endDate) {
      if (endDate === 'Present') {
        return `${startDate} - ${endDate}`;
      }
      const start = moment(startDate).format('MMM YYYY');
      const end = moment(endDate).format('MMM YYYY');
      return `${start} - ${end}`;
    },
  },
};
</script>

<style scoped>
/* Experience Section Styles */
.section h2 {
  color: #0d1330;
  font-size: 2.2rem;
  font-family: 'Pacifico', cursive;
  margin-bottom: 20px;
  text-align: center;
}

.experience-section {
  margin-bottom: 2rem;
}

ul {
  list-style: none;
  padding: 0;
}

.experience-card {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
  padding: 15px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

.experience-card:hover {
  background-color: #f9f9f9;
  box-shadow: 0 6px 25px rgba(0, 0, 0, 0.2);
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  border-bottom: 1px solid #eee;
  padding-bottom: 10px;
}

.company-position {
  display: flex;
  align-items: center;
}

.company {
  font-size: 1.2rem;
  color: #ffd600;
  font-weight: bold;
}

.position {
  font-size: 1.1rem;
  color: #333;
  margin-left: 5px;
}

.duration {
  font-size: 1.1rem;
  color: #888;
  font-style: italic;
}

.location,
.description {
  margin-bottom: 5px;
}

.details {
  margin-top: 10px;
}

.location strong,
.description strong {
  color: #333;
  font-weight: bold;
}

/* Icons styling */
.company-icon,
.fa-calendar-alt,
.fa-map-marker-alt,
.fa-info-circle {
  margin-right: 10px;
  color: #ffd600;
}

.company-position i {
  font-size: 1.2rem;
}

.duration i,
.location i,
.description i {
  font-size: 1rem;
}

/* Responsive layout */
@media (max-width: 768px) {
  .experience-card {
    flex-direction: column;
  }

  .header {
    flex-direction: column;
    align-items: flex-start;
  }

  .company-position {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
