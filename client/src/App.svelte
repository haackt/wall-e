<script lang="ts">
  import { Toaster } from 'svelte-french-toast';

  import { isConnected } from './stores/websocket';

  import ConnectDialog from './lib/components/Dialogs/ConnectDialog.svelte';
  import Footer from './lib/layout/Footer.svelte';
  import Header from './lib/layout/Header.svelte';

  import Dashboard from './lib/components/Dashboard.svelte';
</script>

<Toaster />

<div class="flex flex-col h-full">
  <Header />
  <main class="flex-1 bg-mb-dark text-gray-300 p-12">
    {#if $isConnected}
      <Dashboard />
    {:else}
      <ConnectDialog />
    {/if}
  </main>
  <Footer />
</div>
