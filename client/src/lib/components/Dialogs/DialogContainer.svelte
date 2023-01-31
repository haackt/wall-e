<script src="ts">
  import XCircle from '../Icons/x-circle.svelte';

  export let showDialog = false;
  export let showCloseButton = true;
  export let mayClose = true;

  export function show() {
    showDialog = true;
  }
  export function hide() {
    if (mayClose) {
      showDialog = false;
    }
  }
</script>

<svelte:window
  on:keydown={(event) => {
    if (event.key === 'Escape') {
      hide();
    }
  }}
/>

{#if showDialog}
  <div class="fixed w-screen h-screen backdrop-blur-sm top-0 left-0 flex justify-center items-center">
    <div
      class="bg-mb-darker w-full max-w-4xl lg:max-w-4xl max-h-screen px-4 py-4 relative drop-shadow-lg rounded-lg text-mb-text overflow-y-auto"
    >
      <header class="width-full absolute right-4">
        {#if showCloseButton}
          <button on:click={() => hide()}>
            <XCircle />
          </button>
        {/if}
      </header>
      <slot />
    </div>
  </div>
{/if}
