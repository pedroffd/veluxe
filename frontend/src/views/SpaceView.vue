<script setup lang="ts">
import Contact from "../components/Contact.vue";
import Footer from "../components/Footer.vue";
import Navbar from "../components/Navbar.vue";

const equipments = [
  {
    name: "Iluminação Scangrip",
    desc: "Sistemas de luz que revelam até a menor imperfeição na pintura.",
  },
  {
    name: "Polidores Rupes",
    desc: "A tecnologia italiana líder mundial em correção de pintura.",
  },
  {
    name: "Ambiente Climatizado",
    desc: "Temperatura e umidade controladas para cura perfeita de vitrificadores.",
  },
  {
    name: "Limpeza Técnica",
    desc: "Uso exclusivo de água deionizada e produtos pH neutro biodegradáveis.",
  },
];
</script>

<template>
  <div class="min-h-screen bg-premium-black text-white font-display">
    <Navbar />

    <!-- Hero Section -->
    <section class="relative h-[80vh] flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0 z-0">
        <img 
          src="/Users/pedroffd/.gemini/antigravity/brain/7f025176-572b-4633-8adb-44d0c0809815/veluxe_atelier_hero_1771351699443.png" 
          alt="Veluxe Atelier" 
          class="w-full h-full object-cover opacity-60 scale-105"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-premium-black via-transparent to-premium-black/50"></div>
      </div>
      
      <div class="container mx-auto px-6 relative z-10 text-center">
        <h1 class="text-7xl md:text-9xl font-bold tracking-tighter mb-4">
          NOSSO <span class="text-premium-gold">ESPAÇO</span>
        </h1>
        <p class="text-gray-400 uppercase tracking-[0.5em] text-sm font-bold">The Automotive Atelier</p>
      </div>
    </section>

    <!-- Content Breakdown -->
    <section class="py-32 border-b border-white/5">
      <div class="container mx-auto px-6">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-20 items-center">
          <div>
            <h2 class="text-xs font-bold text-premium-gold uppercase tracking-[0.3em] mb-4">O Conceito</h2>
            <h3 class="text-5xl font-bold mb-8 leading-tight">Um ambiente projetado para quem é <span class="italic font-light">chato</span> com carro.</h3>
            <p class="text-xl text-gray-400 leading-relaxed mb-10">
              Sustentado no princípio de fazer o que ninguém faz para chegar onde ninguém chegou, o Veluxe Atelier é um retrato da estética automotiva em seu estado mais puro. Não é apenas sobre limpar; é sobre preservar um patrimônio e elevar a alma de cada máquina que atravessa nossas portas.
            </p>
            <div class="grid grid-cols-2 gap-8">
              <div v-for="eq in equipments" :key="eq.name">
                <h4 class="text-white font-bold mb-2 uppercase tracking-widest text-xs">{{ eq.name }}</h4>
                <p class="text-gray-500 text-sm">{{ eq.desc }}</p>
              </div>
            </div>
          </div>
          <div class="relative group">
            <div class="absolute -inset-4 border border-premium-gold/30 translate-x-4 translate-y-4 group-hover:translate-x-2 group-hover:translate-y-2 transition-transform duration-700"></div>
            <img 
              src="/Users/pedroffd/.gemini/antigravity/brain/7f025176-572b-4633-8adb-44d0c0809815/veluxe_atelier_detail_polisher_1771351822751.png" 
              class="relative z-10 grayscale hover:grayscale-0 transition-all duration-1000" 
              alt="Detailing Detail" 
            />

          </div>
        </div>
      </div>
    </section>

    <!-- Experience Quote -->
    <section class="py-40 bg-white/[0.02] text-center px-6">
      <div class="max-w-4xl mx-auto">
        <span class="text-premium-gold text-4xl mb-8 block leading-none">“</span>
        <blockquote class="text-3xl md:text-4xl font-light italic text-gray-300 leading-tight mb-8">
          A iluminação não é para beleza, é para a verdade. Se conseguimos ver o defeito, conseguimos corrigi-lo. Se o ambiente é sujo, o resultado nunca será limpo.
        </blockquote>
        <cite class="text-xs font-bold uppercase tracking-[0.4em] text-gray-500 not-italic">— Filossofia Veluxe</cite>
      </div>
    </section>

    <!-- Contact & Footer -->
    <Contact />
    <Footer />
  </div>
</template>

<style scoped>
.font-display {
  font-family: 'Outfit', sans-serif;
}
</style>
