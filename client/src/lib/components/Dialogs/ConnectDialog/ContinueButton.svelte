<script lang="ts">
  export let disabled: boolean;
  export let onClick: () => void;
</script>

<button {disabled} class="bg-mb-blue disabled:bg-mb-blue/50 w-24 h-8 rounded-sm" on:click={() => onClick()}
  >Weiter &rarr;</button
>
