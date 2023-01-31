import './app.postcss';
import App from './App.svelte';

// Initialize the app and mount it to the DOM
const app = new App({
  target: document.getElementById('app'),
});

export default app;
