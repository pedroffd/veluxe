<script setup lang="ts">
import axios from "axios";
import { onMounted, ref } from "vue";

interface Service {
  id: number;
  name: string;
  category: string;
  price_start: string;
}

const services = ref<Service[]>([]);
const loading = ref(true);

const fetchServices = async () => {
  try {
    const token = localStorage.getItem("token");
    const response = await axios.get("/api/services/", {
      headers: { Authorization: `Token ${token}` },
    });
    services.value = response.data;
  } catch (err) {
    console.error("Erro ao buscar serviços:", err);
  } finally {
    loading.value = false;
  }
};

const deleteService = async (id: number) => {
  if (!confirm("Tem certeza que deseja excluir este serviço?")) return;

  try {
    const token = localStorage.getItem("token");
    await axios.delete(`/api/services/${id}/`, {
      headers: { Authorization: `Token ${token}` },
    });
    services.value = services.value.filter((s) => s.id !== id);
  } catch (err) {
    alert("Erro ao excluir serviço.");
  }
};

onMounted(fetchServices);
</script>

<template>
  <div class="space-y-10">
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-6">
      <div>
        <h1 class="text-4xl font-bold text-white mb-2 tracking-tight">Gestão de Serviços</h1>
        <p class="text-gray-500 text-sm font-bold uppercase tracking-widest">Controle o catálogo de experiências Veluxe</p>
      </div>
      <router-link 
        :to="{ name: 'service-new' }"
        class="bg-premium-gold hover:bg-[#C5A028] text-black font-bold px-8 py-3 transition-colors flex items-center justify-center gap-2"
      >
        <span class="text-xl">+</span> NOVO SERVIÇO
      </router-link>
    </div>

    <!-- Loading -->
    <div v-if="loading" class="text-center py-20">
      <div class="animate-spin inline-block w-8 h-8 border-4 border-premium-gold border-t-transparent rounded-full mb-4"></div>
      <p class="text-gray-500 font-bold tracking-widest text-xs">CARREGANDO DADOS...</p>
    </div>

    <!-- Table -->
    <div v-else class="bg-[#111] border border-white/5 overflow-hidden">
      <table class="w-full text-left border-collapse">
        <thead class="bg-black border-b border-white/5">
          <tr>
            <th class="p-6 text-[10px] text-gray-500 font-bold uppercase tracking-widest">Serviço</th>
            <th class="p-6 text-[10px] text-gray-500 font-bold uppercase tracking-widest">Categoria</th>
            <th class="p-6 text-[10px] text-gray-500 font-bold uppercase tracking-widest">Preço Inicial</th>
            <th class="p-6 text-[10px] text-gray-500 font-bold uppercase tracking-widest text-right">Ações</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-white/5">
          <tr v-for="service in services" :key="service.id" class="hover:bg-white/[0.02] transition-colors group">
            <td class="p-6">
              <span class="text-white font-bold block">{{ service.name }}</span>
            </td>
            <td class="p-6">
              <span class="px-2 py-1 text-[9px] font-bold uppercase tracking-tighter border"
                    :class="service.category === 'combo' ? 'border-premium-gold text-premium-gold' : 'border-gray-600 text-gray-500'">
                {{ service.category === 'combo' ? 'Signature Combo' : 'Individual' }}
              </span>
            </td>
            <td class="p-6 text-gray-300 font-medium">
              R$ {{ Number(service.price_start).toLocaleString('pt-BR') }}
            </td>
            <td class="p-6 text-right">
              <div class="flex justify-end gap-3">
                <router-link 
                  :to="{ name: 'service-edit', params: { id: service.id } }"
                  class="bg-white/5 hover:bg-white/10 text-white text-xs font-bold px-4 py-2 border border-white/5 transition-colors"
                >
                  EDITAR
                </router-link>
                <button 
                  @click="deleteService(service.id)"
                  class="bg-red-500/5 hover:bg-red-500/20 text-red-500 text-xs font-bold px-4 py-2 border border-red-500/10 transition-colors"
                >
                  EXCLUIR
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
      
      <div v-if="!services.length" class="p-20 text-center text-gray-600 font-bold uppercase tracking-widest text-xs">
        Nenhum serviço cadastrado.
      </div>
    </div>
  </div>
</template>
