<script setup lang="ts">
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";

const props = defineProps<{
  id?: string;
}>();

const router = useRouter();
const loading = ref(false);
const saving = ref(false);

const form = ref({
  name: "",
  category: "individual",
  description: "",
  price_start: "",
  price_cash: "",
  installment_max: 3,
  warranty_time: "",
  delivery_time: "",
  icon_name: "✨",
  is_featured: false,
  features: [] as { description: string; order: number }[],
});

const fetchService = async () => {
  if (!props.id) return;
  loading.value = true;
  try {
    const token = localStorage.getItem("token");
    const response = await axios.get(`/api/services/${props.id}/`, {
      headers: { Authorization: `Token ${token}` },
    });
    form.value = response.data;
  } catch (err) {
    alert("Erro ao carregar serviço.");
    router.push({ name: "dashboard" });
  } finally {
    loading.value = false;
  }
};

const addFeature = () => {
  form.value.features.push({
    description: "",
    order: form.value.features.length,
  });
};

const removeFeature = (index: number) => {
  form.value.features.splice(index, 1);
};

const save = async () => {
  saving.value = true;
  try {
    const token = localStorage.getItem("token");
    const config = { headers: { Authorization: `Token ${token}` } };

    if (props.id) {
      await axios.put(`/api/services/${props.id}/`, form.value, config);
    } else {
      await axios.post("/api/services/", form.value, config);
    }
    router.push({ name: "dashboard" });
  } catch (err) {
    alert("Erro ao salvar serviço. Verifique os campos.");
    console.error(err);
  } finally {
    saving.value = false;
  }
};

onMounted(fetchService);
</script>

<template>
  <div class="max-w-4xl mx-auto py-10">
    <div class="mb-10 flex items-center justify-between">
      <div>
        <h1 class="text-4xl font-bold text-white mb-2 tracking-tight">
          {{ id ? 'Editar Serviço' : 'Novo Serviço' }}
        </h1>
        <p class="text-gray-500 text-sm font-bold uppercase tracking-widest">Configure os detalhes da experiência</p>
      </div>
      <router-link to="/manager" class="text-gray-500 hover:text-white transition-colors font-bold text-xs uppercase tracking-widest">
        Cancelar
      </router-link>
    </div>

    <form @submit.prevent="save" class="space-y-8">
      <!-- Loading Placeholder -->
      <div v-if="loading" class="animate-pulse space-y-8">
        <div class="h-20 bg-white/5 rounded"></div>
        <div class="h-64 bg-white/5 rounded"></div>
      </div>

      <div v-else class="space-y-8">
        <!-- Basic Info -->
        <div class="bg-[#111] border border-white/5 p-8">
          <h2 class="text-xl font-bold text-white mb-6 flex items-center gap-3">
             <span class="w-1.5 h-6 bg-premium-gold block"></span>
             Informações Básicas
          </h2>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="md:col-span-2">
              <label class="block text-xs font-bold uppercase tracking-widest text-gray-500 mb-2">Nome do Serviço</label>
              <input v-model="form.name" type="text" required class="form-input" placeholder="Ex: Sequência Diamante" />
            </div>

            <div>
              <label class="block text-xs font-bold uppercase tracking-widest text-gray-500 mb-2">Categoria</label>
              <select v-model="form.category" class="form-input">
                <option value="individual">Tratamento Individual</option>
                <option value="combo">Signature Combo</option>
              </select>
            </div>

            <div>
              <label class="block text-xs font-bold uppercase tracking-widest text-gray-500 mb-2">Preço Inicial (R$)</label>
              <input v-model="form.price_start" type="number" step="0.01" required class="form-input" placeholder="0.00" />
            </div>

            <div class="md:col-span-2">
              <label class="block text-xs font-bold uppercase tracking-widest text-gray-500 mb-2">Descrição Curta</label>
              <textarea v-model="form.description" class="form-input h-24" placeholder="Breve resumo atraente..."></textarea>
            </div>
          </div>
        </div>

        <!-- Premium Details -->
        <div class="bg-[#111] border border-white/5 p-8">
          <h2 class="text-xl font-bold text-white mb-6 flex items-center gap-3">
             <span class="w-1.5 h-6 bg-premium-gold block"></span>
             Detalhes Premium
          </h2>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-xs font-bold uppercase tracking-widest text-gray-500 mb-2">Garantia (Texto)</label>
              <input v-model="form.warranty_time" type="text" class="form-input" placeholder="Ex: 6 meses" />
            </div>
            <div>
              <label class="block text-xs font-bold uppercase tracking-widest text-gray-500 mb-2">Prazo de Entrega</label>
              <input v-model="form.delivery_time" type="text" class="form-input" placeholder="Ex: 2 dias" />
            </div>
            <div>
              <label class="block text-xs font-bold uppercase tracking-widest text-gray-500 mb-2">Máximo Parcelas</label>
              <input v-model="form.installment_max" type="number" class="form-input" />
            </div>
            <div>
              <label class="block text-xs font-bold uppercase tracking-widest text-gray-500 mb-2">Preço à Vista (Opcional)</label>
              <input v-model="form.price_cash" type="number" step="0.01" class="form-input" placeholder="0.00" />
            </div>
          </div>
        </div>

        <!-- Features -->
        <div class="bg-[#111] border border-white/5 p-8">
           <div class="flex items-center justify-between mb-6">
             <h2 class="text-xl font-bold text-white flex items-center gap-3">
                <span class="w-1.5 h-6 bg-premium-gold block"></span>
                Itens Inclusos (Features)
             </h2>
             <button type="button" @click="addFeature" class="text-premium-gold text-xs font-bold uppercase tracking-widest hover:text-white transition-colors">
               + Adicionar Item
             </button>
           </div>

           <div class="space-y-4">
             <div v-for="(feat, index) in form.features" :key="index" class="flex gap-4 items-center">
               <input v-model="feat.description" type="text" class="form-input flex-grow" placeholder="Ex: Lavagem técnica detalhada" />
               <button type="button" @click="removeFeature(index)" class="text-red-500 hover:text-red-400 p-2">
                 &times;
               </button>
             </div>
             <div v-if="!form.features.length" class="text-center py-6 border border-dashed border-white/10 text-gray-600 text-xs italic uppercase tracking-widest">
               Nenhum item adicionado
             </div>
           </div>
        </div>

        <!-- Meta -->
        <div class="bg-[#111] border border-white/5 p-8 flex items-center gap-4">
          <input v-model="form.is_featured" type="checkbox" id="featured" class="w-5 h-5 accent-premium-gold" />
          <label for="featured" class="text-white font-bold cursor-pointer">Destaque na página principal</label>
        </div>

        <!-- Actions -->
        <div class="flex justify-end pt-6">
          <button 
            type="submit" 
            :disabled="saving"
            class="bg-premium-gold hover:bg-[#C5A028] text-black font-bold px-12 py-4 transition-all disabled:opacity-50 flex items-center gap-3"
          >
            <span v-if="saving" class="animate-spin border-2 border-black border-t-transparent rounded-full w-4 h-4"></span>
            {{ saving ? 'SALVANDO...' : 'SALVAR ALTERAÇÕES' }}
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<style scoped>
.form-input {
  @apply w-full bg-[#161616] border border-white/10 text-white px-4 py-3 focus:border-premium-gold focus:outline-none transition-colors;
}
</style>
