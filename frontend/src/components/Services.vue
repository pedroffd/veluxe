<script setup lang="ts">
const services = [
  {
    title: "Polimento Técnico",
    description:
      "Correção de pintura em múltiplos estágios para atingir o brilho máximo.",
    icon: "✨",
  },
  {
    title: "Vitrificação",
    description:
      "Proteção cerâmica de alta durabilidade contra riscos e intempéries.",
    icon: "🛡️",
  },
  {
    title: "Higienização Interna",
    description:
      "Limpeza profunda e hidratação de couros com produtos premium.",
    icon: "🛋️",
  },
];
</script>

<template>
  <section id="services" class="py-20 bg-premium-black relative">
    <div class="container mx-auto px-6">
      <div class="text-center mb-16">
        <h3 class="text-premium-gold text-sm font-bold tracking-[0.2em] uppercase mb-4">O que fazemos</h3>
        <h2 class="text-4xl md:text-5xl font-display font-bold text-white">Nossos Serviços</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div 
          v-for="service in services" 
          :key="service.title"
          class="group p-8 border border-white/10 bg-white/5 hover:bg-white/10 transition-all duration-300 hover:-translate-y-2"
        >
          <div class="text-4xl mb-6">{{ service.icon }}</div>
          <h3 class="text-2xl font-display font-bold mb-4 text-white group-hover:text-premium-gold transition-colors">
            {{ service.title }}
          </h3>
          <p class="text-gray-400 leading-relaxed">
            {{ service.description }}
          </p>
        </div>
      </div>
    </div>
  </section>
</template>
