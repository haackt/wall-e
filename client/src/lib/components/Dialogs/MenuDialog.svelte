<script lang="ts">
  import DialogContainer from './DialogContainer.svelte';

  export function show() {
    dialog.show();
  }
  export function hide() {
    dialog.hide();
  }

  let dialog;
  let compileTime = new Date(__COMPILE_TIME__);
</script>

<DialogContainer bind:this={dialog}>
  <h2 class="font-serif text-3xl mt-4 mb-4 border-b border-mb-dark">Wall-E Projekt</h2>
  <p class="text-mb-text-muted">
    Das Wall-E Projekt ist ein Projekt, welches von dem Ausbildungsjahrgang FI 22 (Mercedes-Benz Werk Berlin-Marienfelde)
    realisiert wurde.
  </p>
  <div class="text-sm flex justify-center my-2 text-mb-text-muted">Version: {compileTime.toLocaleString()}</div>
</DialogContainer>
