<script lang="ts">
  export let onClick;
</script>

<button
  class="bg-mb-darker py-1 px-2 lg:px-3 lg:py-2 rounded-md flex whitespace-nowrap items-center gap-1 border border-mb-darker hover:text-mb-blue hover:border-mb-blue"
  on:click={() => onClick()}
>
  <slot />
</button>
