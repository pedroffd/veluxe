/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        premium: {
          black: "#0a0a0a",
          dark: "#121212",
          gray: "#1e1e1e",
          gold: "#d4af37",
          silver: "#c0c0c0",
          red: "#8b0000", // Deep automotive red
        },
      },
      fontFamily: {
        sans: ["Inter", "sans-serif"],
        display: ["Outfit", "sans-serif"],
      },
      backgroundImage: {
        "hero-pattern": "url('/hero-car.jpg')", // Placeholder
      },
    },
  },
  plugins: [],
};
