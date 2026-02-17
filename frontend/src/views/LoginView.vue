<script setup lang="ts">
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const username = ref("");
const password = ref("");
const loading = ref(false);
const error = ref<string | null>(null);

const handleLogin = async () => {
  loading.value = true;
  error.value = null;
  try {
    const response = await axios.post("/api/login/", {
      username: username.value,
      password: password.value,
    });
    localStorage.setItem("token", response.data.token);
    router.push({ name: "dashboard" });
  } catch (err) {
    error.value = "Credenciais inválidas. Tente novamente.";
    console.error(err);
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div class="min-h-screen bg-premium-black flex items-center justify-center px-6">
    <div class="max-w-md w-full">
      <!-- Logo / Header -->
      <div class="text-center mb-12">
        <h1 class="text-5xl font-bold text-white font-display tracking-tight mb-2">
          VELUXE<span class="text-premium-gold">.</span>
        </h1>
        <p class="text-gray-400 uppercase tracking-[0.3em] text-xs font-bold">Manager Access</p>
      </div>

      <div class="bg-[#111] border border-white/5 p-10 shadow-2xl">
        <form @submit.prevent="handleLogin" class="space-y-6">
          <div v-if="error" class="bg-red-500/10 border border-red-500/20 text-red-500 p-4 text-sm text-center">
            {{ error }}
          </div>

          <div>
            <label class="block text-xs font-bold uppercase tracking-widest text-gray-500 mb-2">Usuário</label>
            <input 
              v-model="username"
              type="text" 
              required
              class="w-full bg-[#161616] border border-white/10 text-white px-4 py-3 focus:border-premium-gold focus:outline-none transition-colors"
              placeholder="admin"
            />
          </div>

          <div>
            <label class="block text-xs font-bold uppercase tracking-widest text-gray-500 mb-2">Senha</label>
            <input 
              v-model="password"
              type="password" 
              required
              class="w-full bg-[#161616] border border-white/10 text-white px-4 py-3 focus:border-premium-gold focus:outline-none transition-colors"
              placeholder="••••••••"
            />
          </div>

          <button 
            type="submit"
            :disabled="loading"
            class="w-full bg-premium-gold hover:bg-[#C5A028] text-black font-bold py-4 transition-all duration-300 disabled:opacity-50 flex items-center justify-center gap-2"
          >
            <span v-if="loading" class="animate-spin border-2 border-black border-t-transparent rounded-full w-4 h-4"></span>
            {{ loading ? 'EXPERIÊNCIA DE ACESSO...' : 'ENTRAR NO PAINEL' }}
          </button>
        </form>
        
        <div class="mt-8 text-center">
          <router-link to="/" class="text-gray-600 text-xs hover:text-white transition-colors uppercase tracking-widest font-bold">
            ← Voltar para o site
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.font-display {
  font-family: 'Outfit', sans-serif;
}
</style>
