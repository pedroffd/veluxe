<script setup lang="ts">
import Footer from "./components/Footer.vue";
import Hero from "./components/Hero.vue";
import Navbar from "./components/Navbar.vue";
import Services from "./components/Services.vue";
</script>

<template>
  <div class="min-h-screen bg-premium-black text-white selection:bg-premium-gold selection:text-black">
    <Navbar />
    <main>
      <Hero />
      <Services />
    </main>
    <Footer />
  </div>
</template>
