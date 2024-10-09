<template>
  <b-navbar toggleable="lg" class="main-navbar fixed-top">
    <b-container>
      <div class="navbar-wrapper mx-auto d-flex justify-content-between align-items-center">
        <b-navbar-brand href="#" class="navbar-title">
          Kenza's Portfolio
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class="d-flex justify-content-center">
            <a href="#home" class="nav-link-item">Home</a>
            <a href="#about" class="nav-link-item">About Me</a>
            <a href="#projects" class="nav-link-item">Projects</a>
            <a href="#contact" class="nav-link-item">Contact</a>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-container>
  </b-navbar>
</template>

<script>
export default {
  mounted() {
    // Add a scroll event listener for navbar background
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeUnmount() {
    // Clean up the event listener
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      const navbar = document.querySelector(".main-navbar");
      if (window.scrollY > 50) {
        navbar.classList.add("scrolled");
      } else {
        navbar.classList.remove("scrolled");
      }
    },
  },
};
</script>

<style scoped>
.navbar-title {
  font-family: 'Pacifico', cursive;
  font-size: 1.8rem;
  font-weight: bold;
  color: #607d8b;
}
.main-navbar {
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  z-index: 1000;
  background-color: #1a237e !important; /* Navy Blue background */
  padding: 10px 20px;
  transition: background-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Remove underlines from links and use Slate Gray for text */
.nav-link-item {
  font-size: 1.1rem;
  color: #607d8b; /* Slate Gray color for the links */
  margin: 0 15px;
  padding: 8px 15px;
  text-decoration: none; /* Remove underline */
  transition: color 0.3s ease, background-color 0.3s ease;
}

/* Hover effect for the links */
.nav-link-item:hover {
  color: #e2e0d6; /* Accent Yellow on hover */
  background-color: #1a237e; /* Slight yellow tint on hover */
}

/* Active link style */
.nav-link-item.active {
  color: #c8c6bf; /* Accent Yellow for the active link */
  font-weight: bold;
}
</style>
