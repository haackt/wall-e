<script lang="ts">
  import DialogContainer from './DialogContainer.svelte';

  export function show() {
    dialog.show();
  }
  export function hide() {
    dialog.hide();
  }

  let dialog;
</script>

<DialogContainer bind:this={dialog}>
  <h2 class="font-serif text-3xl mt-4 mb-4 border-b border-mb-dark">Wall-E Projekt</h2>
  <p class="text-mb-text">
    Das Wall-E Projekt ist ein Projekt, welches von dem Ausbildungsjahrgang FI 22 (Mercedes-Benz Werk Berlin-Marienfelde)
    realisiert wurde.
  </p>
  <h3 class="font-serif text-lg mt-4 mb-4 border-b border-mb-dark">Ausführliche Informationen</h3>
  <p>
    Ausführliche Informationen inklusive einer Dokumentation lässt sich unter folgendem <a href="https://google.com">Link</a
    > abrufen.
  </p>
  <h3 class="font-serif text-lg mt-4 mb-4 border-b border-mb-dark">Arbeitsgruppen</h3>
  <table class="table-fixed w-full text-left">
    <tr>
      <th>Azubi</th>
      <th>Gruppe</th>
      <th>Aufgabenbereich</th>
    </tr>
    <tr>
      <td>Til Sander</td>
      <td>Gruppe Dokumentation</td>
      <td>Dokumentation</td>
    </tr>
    <tr>
      <td>Danny Muschiol</td>
      <td>Gruppe 3D-Druck</td>
      <td>3D Druck, ...?</td>
    </tr>
    <tr>
      <td>Klara Müller</td>
      <td>Gruppe 3D-Druck</td>
      <td>3D Druck, ...</td>
    </tr>
    <tr>
      <td>Nadine Tobies</td>
      <td>Gruppe 3D-Druck</td>
      <td>3D Druck, Dokumentation</td>
    </tr>
    <tr>
      <td>Till Tomczak</td>
      <td>Gruppe Hardware</td>
      <td>Administration RPi</td>
    </tr>
    <tr>
      <td>Janik Leibold</td>
      <td>Gruppe Hardware</td>
      <td>Administration RPi, Zusammenbau</td>
    </tr>
    <tr>
      <td>Jan Dalke</td>
      <td>Gruppe Software</td>
      <td>Kalibrierung der Servos, ...</td>
    </tr>
    <tr>
      <td>Mika Egerland</td>
      <td>Gruppe Software</td>
      <td>Kalibrierung der Servos, ...</td>
    </tr>
    <tr>
      <td>Kira Neumann</td>
      <td>Gruppe Software</td>
      <td>Arduino-Entwicklung, ...</td>
    </tr>
    <tr>
      <td>Torben Haack</td>
      <td>Gruppe Software</td>
      <td>Web-Entwicklung</td>
    </tr>
  </table>
</DialogContainer>
