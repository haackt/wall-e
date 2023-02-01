<script lang="ts">
  export let onClick: () => void;
</script>

<button class="bg-mb-dark disabled:bg-mb-blue/50 w-24 h-8 rounded-sm hover:text-mb-blue" on:click={() => onClick()}
  >&larr; Zurück</button
>
