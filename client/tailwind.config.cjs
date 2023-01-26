const defaultTheme = require('tailwindcss/defaultTheme');

const config = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', ...defaultTheme.fontFamily.sans],
        serif: ['Playfair Display', ...defaultTheme.fontFamily.serif],
      },
      aspectRatio: {
        '4/3': '4 / 3',
      },
      colors: {
        'mb-blue': '#00afec',
        'mb-dark': '#1f2022',
        'mb-darker': '#121516',
        'mb-text': '#fefefe',
        'mb-text-muted': '#4e5152',
      },
    },
  },
  plugins: [],
};

module.exports = config;
