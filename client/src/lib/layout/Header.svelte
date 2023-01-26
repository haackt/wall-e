<script lang="ts">
  import { isConnected } from '../../stores/websocket';
  import Logo from '../../assets/logo.svg';
  import MenuDialog from '../components/Dialogs/MenuDialog.svelte';
  import Bars_3 from '../components/Icons/bars-3.svelte';

  let menuDialog;
</script>

{#if $isConnected}
  <MenuDialog bind:this={menuDialog} />
{/if}

<header class="bg-mb-darker text-mb-text py-4 px-4 flex justify-between items-center">
  <div>
    <img src={Logo} class="h-12" alt="Mercedes-Benz Logo" />
  </div>
  <div>
    <button class="align-middle hover:text-mb-blue" on:click={() => menuDialog.show()}>
      <Bars_3 />
    </button>
  </div>
</header>
