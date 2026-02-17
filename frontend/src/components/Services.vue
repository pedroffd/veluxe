<script setup lang="ts">
import { computed, onMounted, ref } from "vue";

interface ServiceFeature {
  description: string;
  order: number;
}

interface Service {
  id: number;
  name: string;
  category: "combo" | "individual";
  description: string;
  price_start: string;
  price_cash: string;
  installment_max: number;
  warranty_time: string;
  delivery_time: string;
  icon_name: string;
  features: ServiceFeature[];
  is_featured: boolean;
}

const services = ref<Service[]>([]);
const loading = ref(true);
const error = ref<string | null>(null);

const combos = computed(() =>
  services.value.filter((s) => s.category === "combo"),
);
const individuals = computed(() =>
  services.value.filter((s) => s.category === "individual"),
);

const fetchServices = async () => {
  try {
    const response = await fetch("/api/services/");
    if (!response.ok) throw new Error("Falha ao carregar serviços");
    services.value = await response.json();
  } catch (err) {
    error.value = "Erro ao conectar com o servidor.";
    console.error(err);
  } finally {
    loading.value = false;
  }
};

const formatCurrency = (value: string | number) => {
  const val = Number(value);
  if (isNaN(val)) return "R$ 0,00";
  return (
    "R$ " +
    val.toLocaleString("pt-BR", {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    })
  );
};

onMounted(() => {
  fetchServices();
});
</script>

<template>
  <section id="services" class="py-24 bg-premium-black relative">
    <div class="container mx-auto px-6">
      
      <!-- Combos Section (Sequência Diamante Style) -->
      <div v-if="combos.length" class="mb-24">
        <div class="text-center mb-16">
          <h3 class="text-premium-gold text-sm font-bold tracking-[0.3em] uppercase mb-4">Experiência Signature</h3>
          <h2 class="text-5xl font-display font-bold text-white uppercase tracking-tight">Programas Exclusivos</h2>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 items-stretch">
          <div v-for="combo in combos" :key="combo.id" 
               class="bg-[#111] border border-white/5 shadow-2xl relative overflow-hidden group flex flex-col items-stretch">
            
            <!-- Header -->
            <div class="bg-premium-black pt-12 pb-8 text-center border-b border-white/5">
              <h3 class="text-3xl font-display font-bold text-white mb-2 tracking-tight uppercase">{{ combo.name }}</h3>
              <div class="w-16 h-1 bg-premium-gold mx-auto"></div>
            </div>

            <!-- Features Area -->
            <div class="p-10 bg-[#161616] flex-1">
              <ul class="space-y-5">
                <li v-for="feat in combo.features" :key="feat.order" 
                    class="flex items-start text-gray-300 text-lg text-left">
                  <span class="mr-4 text-premium-gold bg-premium-gold/10 p-1 mt-1 rounded-full flex-shrink-0">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
                  </span>
                  <span class="leading-tight">{{ feat.description }}</span>
                </li>
              </ul>
            </div>

            <!-- Warranty/Time Banner -->
            <div class="bg-premium-black py-4 px-10 flex flex-col gap-2 border-y border-white/5">
              <div class="flex items-center text-gray-400 text-xs font-bold uppercase tracking-widest">
                <span class="text-xl mr-3 leading-none opacity-50">🛡️</span> Garantia de {{ combo.warranty_time }}
              </div>
              <div class="flex items-center text-gray-400 text-xs font-bold uppercase tracking-widest">
                <span class="text-xl mr-3 leading-none opacity-50">🕙</span> Entregue em {{ combo.delivery_time }}
              </div>
            </div>

            <!-- Pricing -->
            <div class="p-12 text-center bg-[#EAEAEA]">
              <p class="text-gray-600 font-medium mb-1">
                Parcelado em <span class="text-black font-bold">até {{ combo.installment_max }}x</span> no cartão
              </p>
              <p class="text-gray-600 font-medium mb-8">
                ou <span class="text-black font-bold">à vista com 5% de desconto</span>.
              </p>
              
              <div class="text-5xl font-display font-bold text-black mb-10">
                {{ formatCurrency(combo.price_start) }}
              </div>

              <button class="w-full bg-black hover:bg-zinc-800 text-white py-5 px-10 text-xl font-bold transition-all duration-300 flex items-center justify-center gap-3 rounded-none">
                <span class="text-2xl text-premium-gold">📱</span> Agendar
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Individual Treatments Section -->
      <div v-if="individuals.length" class="mt-20">
        <div class="text-center mb-16">
          <h2 class="text-4xl font-display font-bold text-white uppercase tracking-tight">Tratamentos Individuais</h2>
          <div class="mt-4 h-1 w-24 bg-premium-gold mx-auto"></div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 items-stretch">
          <div v-for="item in individuals" :key="item.id" 
               class="bg-premium-gold overflow-hidden flex flex-col group hover:-translate-y-2 transition-transform duration-300 shadow-xl">
            
            <!-- Icon/Title Area -->
            <div class="p-8 pb-4">
               <h3 class="text-3xl font-display font-bold text-black leading-tight mb-4 min-h-[4.5rem] uppercase tracking-tight line-clamp-2 text-left">{{ item.name }}</h3>
               <div class="h-[2px] bg-black w-full mb-6 opacity-30"></div>
            </div>

            <!-- Feature list -->
            <div class="px-8 pb-8 flex-1">
               <ul class="space-y-4">
                 <li v-for="feat in item.features" :key="feat.order" class="flex items-start text-black font-medium text-sm text-left">
                   <span class="mr-2 text-base leading-none opacity-50">🔘</span> 
                   <span class="leading-tight">{{ feat.description }}</span>
                 </li>
               </ul>
            </div>

            <!-- Footer Details -->
            <div class="bg-[#D1D1D1] p-0 mt-auto">
               <div class="p-4 px-8 border-b border-black/5 flex flex-col gap-1 min-h-[80px] justify-center">
                 <div class="flex items-center text-[10px] text-black/60 font-bold uppercase tracking-wider">
                   🛡️ Garantia de {{ item.warranty_time }}
                 </div>
                 <div class="flex items-center text-[10px] text-black/60 font-bold uppercase tracking-wider">
                   🕙 Entregue em {{ item.delivery_time }}
                 </div>
               </div>

               <div class="flex h-20">
                 <div class="flex-grow flex flex-col justify-center items-center bg-[#E5E5E5] px-4">
                   <span class="text-[10px] text-black/50 font-bold uppercase leading-none mb-1">A partir de</span>
                   <span class="text-2xl font-black text-black leading-none">{{ formatCurrency(item.price_start) }}</span>
                 </div>
                 <button class="bg-[#222] hover:bg-black text-white px-8 flex items-center justify-center gap-2 group-hover:bg-premium-gold group-hover:text-black transition-colors whitespace-nowrap border-none">
                   <span class="text-lg">💬</span>
                   <span class="text-xs font-bold uppercase">Agendar</span>
                 </button>
               </div>
            </div>
          </div>
        </div>
      </div>



      <!-- Empty State -->
      <div v-if="!loading && !services.length" class="text-center text-gray-500 py-10">
        Nenhum serviço disponível no momento.
      </div>

    </div>
  </section>
</template>

<style scoped>
.font-display {
  font-family: 'Outfit', sans-serif;
}
</style>
