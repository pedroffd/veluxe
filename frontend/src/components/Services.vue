<script setup lang="ts">
import { onMounted, ref } from "vue";

interface Service {
  id: number;
  name: string;
  description: string;
  price_start: string;
  icon_name: string;
}

const services = ref<Service[]>([]);
const loading = ref(true);
const error = ref<string | null>(null);

const fetchServices = async () => {
  try {
    const response = await fetch("http://localhost:8000/api/services/");
    if (!response.ok) throw new Error("Falha ao carregar serviços");
    services.value = await response.json();
  } catch (err) {
    error.value = "Erro ao conectar com o servidor.";
    console.error(err);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchServices();
});
</script>

<template>
  <section id="services" class="py-20 bg-premium-black relative">
    <div class="container mx-auto px-6">
      <div class="text-center mb-16">
        <h3 class="text-premium-gold text-sm font-bold tracking-[0.2em] uppercase mb-4">O que fazemos</h3>
        <h2 class="text-4xl md:text-5xl font-display font-bold text-white">Nossos Serviços</h2>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="text-center text-gray-400">
        <div class="animate-spin inline-block w-8 h-8 border-4 border-current border-t-transparent rounded-full text-premium-gold mb-4" role="status"></div>
        <p>Carregando experiências...</p>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="text-center text-red-500 bg-red-500/10 p-4 rounded border border-red-500/20 max-w-md mx-auto">
        {{ error }}
      </div>

      <!-- Data Display -->
      <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div 
          v-for="service in services" 
          :key="service.id"
          class="group p-8 border border-white/10 bg-white/5 hover:bg-white/10 transition-all duration-300 hover:-translate-y-2 flex flex-col"
        >
          <!-- Icon fallback logic -->
          <div class="text-4xl mb-6 text-premium-gold">
            {{ service.icon_name && service.icon_name.length < 5 ? service.icon_name : '✨' }}
          </div>
          
          <h3 class="text-2xl font-display font-bold mb-4 text-white group-hover:text-premium-gold transition-colors">
            {{ service.name }}
          </h3>
          
          <p class="text-gray-400 leading-relaxed mb-6 flex-grow">
            {{ service.description }}
          </p>

          <div class="border-t border-white/10 pt-4 mt-auto">
            <span class="text-xs text-gray-500 uppercase tracking-widest">A partir de</span>
            <p class="text-xl font-bold text-white">R$ {{ Number(service.price_start).toFixed(2).replace('.', ',') }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
