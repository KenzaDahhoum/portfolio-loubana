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
            <router-link to="/#home" class="nav-link-item">Home</router-link>
            <router-link to="/#about" class="nav-link-item">About Me</router-link>
            <router-link to="/#projects" class="nav-link-item">My Brand</router-link>
            <router-link to="/#contact" class="nav-link-item">Contact</router-link>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-container>
  </b-navbar>
</template>

<script>
export default {
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeUnmount() {
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
  font-family: 'Pacifico', cursive !important;
  font-size: 1.8rem;
  color: #ffd600;
}

.main-navbar {
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1000;
  background-color: #0d1330 !important;
  padding: 10px 20px;
  transition: background-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.main-navbar.scrolled {
  background-color: #0d1330 !important;
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.3);
}

.nav-link-item {
  font-size: 1.1rem;
  color: #e0e0e0;
  margin: 0 15px;
  padding: 8px 15px;
  text-decoration: none;
  transition: color 0.3s ease, background-color 0.3s ease;
}

.nav-link-item:hover {
  color: #ffd600;
}

.nav-link-item.active {
  color: #ffd600;
  font-weight: bold;
}

@media (max-width: 768px) {
  .navbar-title {
    font-size: 1.5rem;
  }

  .nav-link-item {
    font-size: 1rem;
    margin: 0 10px;
  }

  .b-navbar-toggle {
    display: block;
  }
}
</style>
