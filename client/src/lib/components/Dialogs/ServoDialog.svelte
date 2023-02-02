<script lang="ts">
  import DialogContainer from './DialogContainer.svelte';
  import { socket } from '../../../stores/websocket';
  import { hext } from '../../../stores/servo';

  let dialog: DialogContainer;
  let arm_left_height: HTMLInputElement;
  let arm_right_height: HTMLInputElement;
  let head_height: HTMLInputElement;
  let head_rotation: HTMLInputElement;

  export function show() {
    dialog.show();
  }
  export function hide() {
    dialog.hide();
  }

  function resetServos() {
    arm_left_height.value = DEFAULT_ALPO.toString();
    arm_right_height.value = DEFAULT_ARPO.toString();
    head_height.value = DEFAULT_HEXT.toString();
    head_rotation.value = DEFAULT_HROT.toString();

    $socket?.emit('alpo', { value: arm_left_height.value });
    $socket?.emit('arpo', { value: arm_right_height.value });
    $socket?.emit('hext', { value: head_height.value });
    $socket?.emit('hrot', { value: head_rotation.value });
  }

  const DEFAULT_ALPO = 100;
  const DEFAULT_ARPO = 0;
  const DEFAULT_HEXT = 50;
  const DEFAULT_HROT = 50;
</script>

<DialogContainer bind:this={dialog}>
  <h1 class="font-serif text-mb-text text-3xl mb-12">Servo-Steuerung</h1>
  <div class="flex flex-col lg:flex-row justify-around items-center">
    <div class="flex text-center flex-col-reverse gap-2 text-mb-text-muted">
      <label for="">Arm-Links</label>
      <input
        value={DEFAULT_ALPO}
        type="range"
        min="0"
        max="100"
        class="vertical rotate-180"
        orient="vertical"
        bind:this={arm_left_height}
        on:input={() => {
          $socket?.emit('alpo', { value: arm_left_height.value });
        }}
      />
    </div>
    <div class="flex text-center flex-col-reverse gap-2 text-mb-text-muted">
      <label for="">Arm-Rechts</label>
      <input
        value={DEFAULT_ARPO}
        type="range"
        min="0"
        max="100"
        class="vertical"
        orient="vertical"
        bind:this={arm_right_height}
        on:input={() => {
          $socket?.emit('arpo', { value: arm_right_height.value });
        }}
      />
    </div>
    <div class="flex text-center flex-col-reverse gap-2 text-mb-text-muted">
      <label for="">Kopfhöhe</label>
      <input
        value={DEFAULT_HEXT}
        type="range"
        min="0"
        max="100"
        class="vertical"
        orient="vertical"
        bind:this={head_height}
        on:input={() => {
          $hext = head_height.value;
          $socket?.emit('hext', { value: head_height.value });
        }}
      />
    </div>
    <div class="flex text-center flex-col-reverse gap-2 text-mb-text-muted">
      <label for="">Kopfdrehung</label>
      <input
        value={DEFAULT_HEXT}
        type="range"
        min="0"
        max="100"
        class="rotate-180"
        bind:this={head_rotation}
        on:input={() => {
          $socket?.emit('hrot', { value: head_rotation.value });
        }}
      />
    </div>
  </div>
  <div class="flex justify-center items-center align-middle mt-5">
    <button
      class="border border-mb-darker hover:border-red-500 px-4 py-2 rounded-md hover:text-red-500"
      on:click={() => resetServos()}
    >
      Alle Servos zurücksetzen
    </button>
  </div>
</DialogContainer>

<style>
  .vertical {
    writing-mode: bt-lr;
    -webkit-appearance: slider-vertical;
  }
</style>
