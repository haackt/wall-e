<script lang="ts">
  export let step: string;
</script>

<span class="whitespace-nowrap">
  {#each step.split(' ') as word, index}
    {#if index == 0}
      {word}
    {:else}
      <span class="hidden sm:inline-flex sm:ml-2">{word}</span>
    {/if}
  {/each}
</span>
