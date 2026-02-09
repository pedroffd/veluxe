<template>
  <section id="about" class="py-20 bg-premium-black relative overflow-hidden">
    <!-- Decorative background elements -->
    <div class="absolute top-0 right-0 w-1/2 h-full bg-gradient-to-l from-premium-gold/5 to-transparent"></div>
    
    <div class="container mx-auto px-6 relative z-10">
      <div class="flex flex-col lg:flex-row items-center gap-16">
        
        <!-- Text Content -->
        <div class="w-full lg:w-1/2">
          <div class="mb-8">
            <h3 class="text-premium-gold text-sm font-bold tracking-[0.2em] uppercase mb-4">Quem Somos</h3>
            <h2 class="text-4xl md:text-5xl font-display font-bold text-white mb-6 leading-tight">
              Mais que estética, <br />
              um <span class="text-transparent bg-clip-text bg-gradient-to-r from-premium-gold to-yellow-200">estilo de vida</span>.
            </h2>
            <div class="h-1 w-20 bg-premium-gold rounded-full"></div>
          </div>

          <div class="space-y-6 text-gray-400 leading-relaxed text-lg">
            <p>
              A <strong class="text-white">Veluxe</strong> nasceu para representar quem exige a perfeição. 
              Não somos apenas uma estética automotiva; somos um ponto de encontro para apaixonados por carros 
              que não aceitam nada menos que o extraordinário.
            </p>
            <p>
              Nosso espaço foi projetado para ser uma extensão da sua garagem. Aqui, cada veículo é tratado 
              como uma obra de arte, recebendo cuidados minuciosos que devolvem o brilho de fábrica e 
              protegem seu patrimônio.
            </p>
            <p>
              Acreditamos que cuidar do carro é uma terapia. Por isso, criamos um ambiente onde você pode 
              vivenciar essa cultura, trocar experiências e ver a mágica acontecer de perto.
            </p>
          </div>

          <div class="mt-10">
            <a 
              href="#contact" 
              class="inline-block px-8 py-4 bg-transparent border border-premium-gold text-premium-gold font-bold uppercase tracking-wider hover:bg-premium-gold hover:text-black transition-all duration-300"
            >
              Conheça Nosso Espaço
            </a>
          </div>
        </div>

        <!-- Image/Visual Content -->
        <div class="w-full lg:w-1/2 relative">
          <div class="relative rounded-sm overflow-hidden border border-white/10 shadow-2xl group">
             <!-- Placeholder for a real shop image. Using a colored block/gradient for now if no image is available, 
                  but ideally this would be a photo of the shop floor. -->
            <div class="aspect-[4/5] bg-neutral-900 relative">
               <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1601362840469-51e4d8d58785?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80')] bg-cover bg-center opacity-60 group-hover:opacity-80 transition-opacity duration-700"></div>
               <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
               
               <div class="absolute bottom-8 left-8 right-8">
                 <div class="text-5xl text-white/10 font-display font-bold mb-2">01</div>
                 <h4 class="text-2xl text-white font-bold mb-2">Excelência Técnica</h4>
                 <p class="text-sm text-gray-300">Profissionais certificados e produtos de elite mundial.</p>
               </div>
            </div>
          </div>
          
          <!-- Decorative square -->
          <div class="absolute -bottom-6 -right-6 w-24 h-24 bg-premium-gold/10 border border-premium-gold/20 -z-10"></div>
          <div class="absolute -top-6 -left-6 w-32 h-32 border border-white/5 -z-10"></div>
        </div>

      </div>
    </div>
  </section>
</template>
