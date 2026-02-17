<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();

const handleLogout = () => {
  localStorage.removeItem("token");
  router.push({ name: "login" });
};
</script>

<template>
  <div class="min-h-screen bg-[#0F0F0F] flex flex-col font-display">
    <!-- Top Nav -->
    <header class="bg-black border-b border-white/5 px-8 h-20 flex items-center justify-between sticky top-0 z-50">
      <div class="flex items-center gap-20">
        <router-link to="/manager" class="text-2xl font-bold text-white tracking-tighter">
          VELUXE<span class="text-premium-gold">.</span> MANAGER
        </router-link>
        
        <nav class="hidden md:flex items-center gap-8">
          <router-link to="/manager" class="text-xs font-bold uppercase tracking-widest hover:text-premium-gold transition-colors text-white">Serviços</router-link>
        </nav>
      </div>

      <div class="flex items-center gap-6">
        <div class="text-right hidden sm:block">
          <p class="text-[10px] text-gray-500 font-bold uppercase tracking-widest mb-1">Logado como</p>
          <p class="text-sm text-white font-bold leading-none">Administrador</p>
        </div>
        <button 
          @click="handleLogout"
          class="bg-white/5 hover:bg-red-500/10 hover:text-red-500 text-white p-2 transition-all border border-white/5"
          title="Sair"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
        </button>
      </div>
    </header>

    <!-- Main Content -->
    <main class="flex-grow p-8">
      <div class="container mx-auto">
        <router-view />
      </div>
    </main>

    <!-- Footer -->
    <footer class="p-8 text-center text-[10px] text-gray-600 uppercase tracking-widest font-bold border-t border-white/5">
      &copy; 2024 Veluxe Automotive Aesthetics &bull; Internal Management System
    </footer>
  </div>
</template>

<style>
.font-display {
  font-family: 'Outfit', sans-serif;
}

.router-link-active {
  color: #D4AF37 !important;
}
</style>
