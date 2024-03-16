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
    background-image: radial-gradient(#D1D5DB 1px, transparent 1px),
                      radial-gradient(#D1D5DB 1px, transparent 1px);
    background-position: 0 0, 25px 25px;
    background-size: 50px 50px;
    z-index: -1;
  }

  body {
    background: linear-gradient(135deg, #9fb8ad, #c0d6df);
    background-size: cover;
    background-repeat: no-repeat;
    min-height: 100vh;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .title {
    color: #393939;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 10px;
    border-bottom: 2px solid #393939;
    padding-bottom: 8px;
  }

  .card {
    background-color: #f7f7f7;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
    transition: box-shadow 0.3s ease;
  }

  .card:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  .card-content {
    text-align: justify;
    padding: 20px;
    border-radius: 10px;
    background-color: #eaeaea;
    text-align: left; /* Align text to left within the card */
  }
</style>

<Content>
  <div class="dot-pattern"></div>
  <div class="container mx-auto px-4 py-8">
    <div class="card">
      <h1 class="text-3xl font-bold title mb-4">Welcome to Health Insight</h1>
      <div class="card-content">
        <p class="text-gray-700 text-lg">
          Health Insight is a comprehensive platform designed to revolutionize the way healthcare professionals and patients interact. With our innovative features, doctors can easily manage patient records, schedule appointments, and securely exchange medical information. Patients can conveniently access their health data, receive personalized notifications, and engage in virtual consultations. Our goal is to provide a seamless experience that enhances communication and promotes better health outcomes.
        </p>
      </div>
    </div>

    <div class="card">
      <h2 class="text-2xl font-bold title mb-4">Getting Started</h2>
      <div class="card-content">
        <p class="text-gray-700 text-lg">
          Getting started with Health Insight is easy! Simply sign up for an account and complete your profile. Once logged in, you'll have access to all our features tailored to your needs. Explore the dashboard to manage your appointments, view your health records, and communicate with your healthcare provider. Need assistance? Our support team is available 24/7 to help you get the most out of Health Insight. Let's embark on a journey towards better health together!
        </p>
      </div>
    </div>

    <div class="card">
      <h2 class="text-2xl font-bold title mb-4">About the Project</h2>
      <div class="card-content">
        <p class="text-gray-700 text-lg">
          Health Insight is an innovative platform designed to facilitate seamless communication and collaboration between healthcare professionals and patients. It offers features such as managing patient records, scheduling appointments, securely exchanging medical information, accessing health data, receiving personalized notifications, and engaging in virtual consultations. With its user-friendly interface and robust security measures, Health Insight aims to enhance the healthcare experience and promote better health outcomes.
        </p>
      </div>
    </div>

    <div class="card">
      <h2 class="text-2xl font-bold title mb-4">Our Team</h2>
      <div class="card-content">
        <p class="text-gray-700 text-lg">
          Our team consists of talented and dedicated individuals passionate about creating innovative solutions for the healthcare industry. Committed to delivering high-quality products meeting clients' needs, we contribute to healthcare technology advancement. With diverse expertise and collaborative approach, we develop cutting-edge solutions driving positive change and improving patient care. Dedicated to excellence, we're proud to lead healthcare innovation.
        </p>
      </div>
    </div>
  </div>
</Content>
