/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        legal: {
          50: '#f8fafc',
          100: '#f1f5f9',
          600: '#1e3a8a',
          700: '#1d4ed8',
          800: '#1e293b',
          900: '#0f172a'
        }
      }
    },
  },
  plugins: [],
}
