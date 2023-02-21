import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import { VitePWA } from 'vite-plugin-pwa';

// https://vitejs.dev/config/
export default defineConfig({
  define: {
    __COMPILE_TIME__: Date.now()
  },
  plugins: [
    svelte(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.png', 'favicon.svg', 'logo.svg', 'sounds/*.wav'],
      manifest: {
        short_name: 'Wall-E',
        name: 'Wall-E WebUI',
        description: 'Web-UI for the Wall-E bot',
        lang: 'de',
        icons: [
          {
            src: '/favicon.svg',
            sizes: '512x512',
            type: 'image/svg+xml',
          },
          {
            src: '/favicon.png',
            sizes: '512x512',
            type: 'image/png',
          },
        ],
        id: 'mb.walle.webui',
        start_url: '/',
        background_color: '#121516',
        display: 'standalone',
        scope: '/',
        theme_color: '#121516',
        orientation: 'portrait',
      },
    }),
  ],
});
