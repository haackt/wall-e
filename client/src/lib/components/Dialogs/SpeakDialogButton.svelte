<script lang="ts">
  export let onClick;
</script>

<button
  on:click={() => onClick()}
  class="px-4 py-2 flex flex-row gap-2 justify-center align-middle items-center bg-mb-dark rounded-md border border-mb-darker hover:border-mb-blue hover:text-mb-blue"
>
  <slot />
</button>
