<script lang="ts">
  import { Content } from "carbon-components-svelte";
</script>
<svelte:head>
  <title>Health Insight
  </title> 
</svelte:head>
<style>
.dot-pattern {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(#27212e, #221530);
  background-position: 0 0, 25px 25px, 0 0;
  background-size: 50px 50px, 50px 50px, 50px 50px;
  z-index: -1;
}

body {
  font-family: 'Quicksand', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background: radial-gradient(#27212e, #221530);
  background-size: cover;
  background-repeat: no-repeat;
  min-height: 100vh;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.header {
  padding: 0 2rem 2rem 2rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 3rem;
  text-align: center;
}
.header img {
  width: 7rem;
}


.header p {
  padding-top: 20px;
  margin: 0;
  color: #ffffff;
}
  .title {
    color: #d9c9ee;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 10px;
    border-bottom: 2px solid #393939;
    padding-bottom: 8px;
  }

    #card {
    max-width: 80rem;
    margin: 2rem auto;
    display: flex;
    justify-content: center;
    gap: 1.5rem;
  }
  .card {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    gap: 1rem;
    background: linear-gradient(#250358, #440c66);
    padding: 1.5rem;
    border-radius: 6px;
    box-shadow: 0 2px 20px rgba(234, 78, 240, 0.2);
    width: 33%;
    transition: all 0.2s
  }

  .card:hover {
    transform: translateY(-2px);
    transition: transform 0.2s;
    box-shadow: 0 2px 30px rgba(234, 78, 240, 0.4);
  }

  .card h2 {
  margin: 0;
  font-size: 1rem;
  text-transform: uppercase;
  }

  .card img {
  width: 6rem;
  height: 5rem;
  object-fit: contain;
}

  .card p {
  color: #fff;
  margin: 0;
  text-align: center;
  font-size: 0.85rem;
}

</style>

<Content>
  <div class="dot-pattern"></div>
  <div class="header">
    <h1 class="text-3xl font-bold title mb-4">Welcome to Health Insight</h1>
    <div class="card-content">
      <p class="text-lg">
        Health Insight is a comprehensive platform designed to revolutionize the way healthcare professionals and patients interact. With our innovative features, doctors can easily manage patient records, schedule appointments, and securely exchange medical information. Patients can conveniently access their health data, receive personalized notifications, and engage in virtual consultations. Our goal is to provide a seamless experience that enhances communication and promotes better health outcomes.
      </p>
    </div>
  </div>
  <div class="container mx-auto px-4">
    <ul id="card">
    <div class="card">
      <img src="/rocket.png" alt="getting started" />
      <h2 class="text-2xl font-bold title mb-4">Getting Started</h2>
      <div class="card-content">
        <p class="text-lg">
          Getting started with Health Insight is easy! Simply sign up for an account and complete your profile. Once logged in, you'll have access to all our features tailored to your needs. Explore the dashboard to manage your appointments, view your health records, and communicate with your healthcare provider. Need assistance? Our support team is available 24/7 to help you get the most out of Health Insight. Let's embark on a journey towards better health together!
        </p>
      </div>
    </div>

    <div class="card">
      <img src="/components.png" alt="project" />
      <h2 class="text-2xl font-bold title mb-4">About the Project</h2>
      <div class="card-content">
        <p class="text-lg">
          Health Insight is an innovative platform designed to facilitate seamless communication and collaboration between healthcare professionals and patients. It offers features such as managing patient records, scheduling appointments, securely exchanging medical information, accessing health data, receiving personalized notifications, and engaging in virtual consultations. With its user-friendly interface and robust security measures, Health Insight aims to enhance the healthcare experience and promote better health outcomes.
        </p>
      </div>
    </div>

    <div class="card">
      <img src="/team.png" alt="team" />
      <h2 class="text-2xl font-bold title mb-4">Our Team</h2>
      <div class="card-content">
        <p class="text-lg">
          Our team consists of talented and dedicated individuals passionate about creating innovative solutions for the healthcare industry. Committed to delivering high-quality products meeting clients' needs, we contribute to healthcare technology advancement. With diverse expertise and collaborative approach, we develop cutting-edge solutions driving positive change and improving patient care. Dedicated to excellence, we're proud to lead healthcare innovation.
        </p>
      </div>
    </div>
  </ul>
  </div>
</Content>
