<script lang="ts">
  export let onClick;
</script>

<button
  class="bg-mb-darker px-3 py-2 rounded-md flex items-center gap-1 border border-mb-darker hover:text-mb-blue hover:border-mb-blue"
  on:click={() => onClick()}
>
  <slot />
</button>
