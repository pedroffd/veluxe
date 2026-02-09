<template>
  <section id="contact" class="py-20 bg-black relative border-t border-white/10">
    <div class="container mx-auto px-6">
      <div class="flex flex-col md:flex-row gap-16">
        
        <!-- Contact Info -->
        <div class="w-full md:w-1/2">
          <h3 class="text-premium-gold text-sm font-bold tracking-[0.2em] uppercase mb-4">Contato</h3>
          <h2 class="text-4xl md:text-5xl font-display font-bold text-white mb-8">
            Agende sua <br />
            experiência.
          </h2>
          
          <div class="space-y-8">
            <div class="flex items-start gap-4">
              <div class="p-3 bg-white/5 rounded text-premium-gold">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              </div>
              <div>
                <h4 class="text-white font-bold mb-1">Telefone / WhatsApp</h4>
                <p class="text-gray-400">+55 (11) 99999-9999</p>
                <a href="#" class="text-premium-gold text-sm hover:underline mt-1 inline-block">Enviar mensagem</a>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <div class="p-3 bg-white/5 rounded text-premium-gold">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              </div>
              <div>
                <h4 class="text-white font-bold mb-1">Localização</h4>
                <p class="text-gray-400">Av. Europa, 123 - Jardins</p>
                <p class="text-gray-400">São Paulo - SP</p>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <div class="p-3 bg-white/5 rounded text-premium-gold">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect><line x1="16" x2="16" y1="2" y2="6"></line><line x1="8" x2="8" y1="2" y2="6"></line><line x1="3" x2="21" y1="10" y2="10"></line></svg>
              </div>
              <div>
                <h4 class="text-white font-bold mb-1">Horário</h4>
                <p class="text-gray-400">Seg - Sex: 09:00 - 18:00</p>
                <p class="text-gray-400">Sáb: 09:00 - 13:00</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Form -->
        <div class="w-full md:w-1/2">
          <form class="bg-white/5 p-8 border border-white/10 rounded-sm space-y-6">
            <div>
              <label class="block text-gray-400 text-sm mb-2">Nome Completo</label>
              <input type="text" class="w-full bg-black/50 border border-white/10 p-3 text-white focus:border-premium-gold focus:outline-none transition-colors" placeholder="Seu nome">
            </div>
            
            <div class="grid grid-cols-2 gap-6">
              <div>
                <label class="block text-gray-400 text-sm mb-2">Telefone</label>
                <input type="tel" class="w-full bg-black/50 border border-white/10 p-3 text-white focus:border-premium-gold focus:outline-none transition-colors" placeholder="(00) 00000-0000">
              </div>
              <div>
                <label class="block text-gray-400 text-sm mb-2">Carro / Modelo</label>
                <input type="text" class="w-full bg-black/50 border border-white/10 p-3 text-white focus:border-premium-gold focus:outline-none transition-colors" placeholder="Ex: Porsche 911">
              </div>
            </div>

            <div>
              <label class="block text-gray-400 text-sm mb-2">Mensagem</label>
              <textarea rows="4" class="w-full bg-black/50 border border-white/10 p-3 text-white focus:border-premium-gold focus:outline-none transition-colors" placeholder="Como podemos ajudar?"></textarea>
            </div>

            <button type="submit" class="w-full bg-premium-gold text-black font-bold py-4 hover:bg-white transition-colors uppercase tracking-widest text-sm">
              Solicitar Orçamento
            </button>
          </form>
        </div>

      </div>
    </div>
  </section>
</template>
