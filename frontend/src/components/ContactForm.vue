<template>
  <section id="contact" class="contact-section">
    <h2>Contact</h2>
    <p class="friendly-paragraph">
      I'm excited to connect! Whether you have a question, a business
      opportunity, or just want to say hi, feel free to reach out. Let's build
      something amazing together!
    </p>
    <div class="contact-container">
      <!-- Left Side: Contact Info -->
      <div class="contact-info">
        <ul>
          <li>
            <i class="fa fa-envelope"></i> Email:
            <strong>kenza.dahhoum@gmail.com</strong>
          </li>
          <li>
            <i class="fa fa-phone"></i> Phone: <strong>+212 6.00.00.00</strong>
          </li>
          <li>
            <i class="fa fa-map-marker"></i> Address:
            <strong>Bir Rami Sud Knitra, Morocco</strong>
          </li>
        </ul>
      </div>

      <!-- Right Side: Contact Form -->
      <div class="contact-form">
        <h3>Get in Touch</h3>
        <form @submit="sendEmail">
            <input v-model="form.name" name="from_name" type="text" placeholder="Your Name" required />
            <input v-model="form.email" name="reply_to" type="email" placeholder="Your Email" required />
            <textarea v-model="form.message" name="message" placeholder="Your Message" required></textarea>
            <button type="submit">Send Message</button>
        </form> 


      </div>
    </div>
  </section>
</template>

<script>
import emailjs from "@emailjs/browser";
import Swal from "sweetalert2";

export default {
  name: "ContactSection",
  data() {
    return {
      form: {
        name: "",
        email: "",
        message: "",
      },
    };
  },
  methods: {
    sendEmail(e) {
      e.preventDefault();
      emailjs
        .sendForm(
          "service_mmf4oad",
          "template_jhggtge",
          e.target,
          "0Cg-CfkBA6Hnhup6u"
        )
        .then(() => {
          Swal.fire(
            "Success!",
            "Your message has been sent successfully!",
            "success"
          );
          this.form.name = "";
          this.form.email = "";
          this.form.message = "";
        })
        .catch(() => {
          Swal.fire(
            "Error",
            "Something went wrong. Please try again later.",
            "error"
          );
        });
    },
  },
};
</script>

<style scoped>
.contact-section {
  padding: 30px 0;
  background-color: #f4f4f4;
  text-align: center;
  color: #0d1330;
}

.contact-section h2 {
  color: #0d1330;
  font-size: 2.2rem;
  font-family: "Pacifico", cursive;
  text-align: center;
  margin-bottom: 20px;
}

.contact-container {
  display: flex;
  justify-content: space-between;
  max-width: 1200px;
  margin: 0 auto;
  padding: 30px;
  flex-wrap: wrap;
}

.friendly-paragraph {
  font-size: 1.2rem;
  color: #333;
  margin-bottom: 20px;
}

.contact-info {
  width: 100%;
  margin-bottom: 20px;
}

.contact-info ul {
  list-style: none;
  padding: 0;
}

.contact-info li {
  margin: 10px 0;
  font-size: 1rem;
  color: #1a237e;
  display: flex;
  align-items: center;
}

.contact-info i {
  margin-right: 10px;
  color: #ffd600;
}

.contact-form {
  background-color: #fff;
  padding: 30px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  width: 100%;
}

.contact-form h3 {
  font-family: "Pacifico", cursive;
  font-size: 1.8rem;
  margin-bottom: 20px;
  color: #1a237e;
}

.contact-form input,
.contact-form textarea {
  width: 100%;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 5px;
  border: 1px solid #ddd;
}

.contact-form button {
    display: inline-block;
    margin-top: 25px;
    padding: 10px 20px;
    background-color: #ffd600;
    color: #1a237e;
    font-weight: bold;
    border: none;
    border-radius: 25px;
    cursor: pointer;
    text-decoration: none;
    transition: background-color 0.3s ease, transform 0.3s ease;
}

.contact-form button:hover {
  background-color: #f5f5dc;
}

/* Media query for larger screens */
@media (min-width: 768px) {
  .contact-info {
    width: 40%;
  }

  .contact-form {
    width: 50%;
  }
}
</style>
