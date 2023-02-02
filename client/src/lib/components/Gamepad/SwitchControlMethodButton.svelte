<script lang="ts">
  import { useGamepad } from '../../../stores/gamepad';
  import FingerPrint from '../Icons/finger-print.svelte';
  import SquarePlus from '../Icons/square-plus.svelte';

  export let onClick: () => void = () => {};
</script>

<button on:click={() => onClick()} class="bg-black py-3 px-6 w-full flex gap-2 justify-center items-center">
  {#if $useGamepad}
    <FingerPrint />
  {:else}
    <SquarePlus />
  {/if}
  <span><slot /></span>
</button>
