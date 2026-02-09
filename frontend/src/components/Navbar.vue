<script setup lang="ts">
import { onMounted, onUnmounted, ref } from "vue";

const isScrolled = ref(false);

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50;
};

onMounted(() => window.addEventListener("scroll", handleScroll));
onUnmounted(() => window.removeEventListener("scroll", handleScroll));

const navLinks = [
  { name: "Início", href: "#" },
  { name: "Serviços", href: "#services" },
  { name: "Sobre", href: "#about" },
  { name: "Contato", href: "#contact" },
];
</script>

<template>
  <nav 
    class="fixed w-full z-50 transition-all duration-300"
    :class="[isScrolled ? 'bg-premium-black/90 backdrop-blur-md py-4 border-b border-white/5' : 'bg-transparent py-6']"
  >
    <div class="container mx-auto px-6 flex justify-between items-center">
      <a href="#" class="text-2xl font-display font-bold tracking-wider">
        VELUXE<span class="text-premium-gold">.</span>
      </a>
      
      <div class="hidden md:flex gap-8 items-center">
        <a 
          v-for="link in navLinks" 
          :key="link.name" 
          :href="link.href"
          class="text-gray-300 hover:text-premium-gold transition-colors text-sm uppercase tracking-widest font-medium"
        >
          {{ link.name }}
        </a>
        
        <a 
          href="https://wa.me/5511999999999" 
          target="_blank"
          class="px-6 py-2 bg-premium-gold text-black font-bold uppercase tracking-wide text-xs hover:bg-yellow-400 transition-colors rounded-sm"
        >
          Agendar
        </a>
      </div>
    </div>
  </nav>
</template>
