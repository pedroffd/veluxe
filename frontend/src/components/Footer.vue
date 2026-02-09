<template>
  <footer class="bg-black text-white py-12 border-t border-white/10">
    <div class="container mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-6">
      <div class="text-center md:text-left">
        <h2 class="text-2xl font-display font-bold tracking-wider mb-2">
          VELUXE<span class="text-premium-gold">.</span>
        </h2>
        <p class="text-gray-500 text-sm"> Excellence in Automotive Aesthetics </p>
      </div>
      
      <div class="flex gap-6">
        <a href="#" class="text-gray-400 hover:text-premium-gold transition-colors">Instagram</a>
        <a href="#" class="text-gray-400 hover:text-premium-gold transition-colors">Facebook</a>
        <a href="#" class="text-gray-400 hover:text-premium-gold transition-colors">WhatsApp</a>
      </div>
      
      <div class="text-gray-600 text-sm">
        &copy; {{ new Date().getFullYear() }} Veluxe. All rights reserved.
      </div>
    </div>
  </footer>
</template>
