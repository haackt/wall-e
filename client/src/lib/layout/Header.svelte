<script lang="ts">
  import { isConnected } from '../../stores/websocket';
  import MenuDialog from '../components/Dialogs/MenuDialog.svelte';
  import Bars_3 from '../components/Icons/bars-3.svelte';

  let menuDialog;
</script>

{#if $isConnected}
  <MenuDialog bind:this={menuDialog} />
{/if}

<header class="bg-mb-darker text-mb-text py-2 lg:py-4 px-4 flex justify-between items-center">
  <div>
    <img src="/logo.svg" class="h-5 lg:h-12" alt="Mercedes-Benz Logo" />
  </div>
  <div>
    <button class="align-middle hover:text-mb-blue" on:click={() => menuDialog.show()}>
      <Bars_3 width="w-5 lg:w-8" />
    </button>
  </div>
</header>
