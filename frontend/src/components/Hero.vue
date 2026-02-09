<script setup lang="ts">
// Using a placeholder image for now, but configured for easy replacement
const heroImage =
  "https://images.unsplash.com/photo-1601362840469-51e4d8d58785?q=80&w=2670&auto=format&fit=crop";
</script>

<template>
  <section class="relative h-screen flex items-center justify-center overflow-hidden">
    <!-- Background Image with Overlay -->
    <div class="absolute inset-0 z-0">
      <img :src="heroImage" alt="Carro de luxo" class="w-full h-full object-cover opacity-60" />
      <div class="absolute inset-0 bg-gradient-to-t from-premium-black via-premium-black/50 to-transparent"></div>
      <div class="absolute inset-0 bg-gradient-to-r from-premium-black/80 to-transparent"></div>
    </div>

    <!-- Content -->
    <div class="container mx-auto px-6 relative z-10 pt-20">
      <div class="max-w-3xl">
        <h2 class="text-premium-gold text-sm font-bold tracking-[0.2em] uppercase mb-4 animate-fade-in-up">
          Estética Automotiva de Alta Performance
        </h2>
        <h1 class="text-5xl md:text-7xl font-display font-bold leading-tight mb-6 animate-fade-in-up delay-100">
          Eleve o padrão do <br />
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-400">seu veículo.</span>
        </h1>
        <p class="text-gray-300 text-lg md:text-xl mb-10 max-w-xl leading-relaxed animate-fade-in-up delay-200">
          Cuidado meticuloso, produtos de elite e acabamento impecável. 
          Transformamos carros em obras de arte.
        </p>
        
        <div class="flex flex-col sm:flex-row gap-4 animate-fade-in-up delay-300">
          <a href="#services" class="px-8 py-4 bg-premium-gold text-black font-bold uppercase tracking-wider hover:bg-yellow-400 transition-all transform hover:-translate-y-1 text-center">
            Nossos Serviços
          </a>
          <a href="https://wa.me/5511999999999" target="_blank" class="px-8 py-4 border border-white/20 hover:border-premium-gold hover:text-premium-gold transition-all uppercase tracking-wider text-center backdrop-blur-sm">
            Falar no WhatsApp
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.delay-100 { animation-delay: 100ms; }
.delay-200 { animation-delay: 200ms; }
.delay-300 { animation-delay: 300ms; }

.animate-fade-in-up {
  animation: fadeInUp 0.8s ease-out forwards;
  opacity: 0;
  transform: translateY(20px);
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
