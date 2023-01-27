<script lang="ts">
  import toast from 'svelte-french-toast';
  import { socket as wsocket, isConnected, ipAddress } from '../../../stores/websocket';
  import io from 'socket.io-client';
  import { ToastOptions } from '../../toast';
  import DialogContainer from './DialogContainer.svelte';

  function connect() {
    const ip_address = document.getElementById('ip-address') as HTMLInputElement;
    const connection_button = document.getElementById('connection-button') as HTMLButtonElement;

    connection_button.disabled = true;

    if (ip_address.value == '') {
      toast.error('Bitte gib eine IP-Adresse an.', ToastOptions);

      connection_button.disabled = false;
      ip_address.focus();
      return;
    }

    toast('Verbinde...', {
      style: ToastOptions.style,
      icon: '⏳',
    });

    const socket = io(`http://${ip_address.value}:1606/`, {
      reconnectionAttempts: 0,
    });

    socket.on('disconnect', () => {
      toast.error('Verbindung verloren.', ToastOptions);
      $isConnected = false;
      $ipAddress = null;
      $wsocket = null;

      dialog.show();
    });

    socket.on('connect', () => {
      $wsocket = socket;
      connection_button.disabled = false;
      $ipAddress = ip_address.value;
      $isConnected = true;
      dialog.hide();

      toast.success('Erfolgreich verbunden!', ToastOptions);
    });

    socket.on('message', (message) => {
      toast(message, {
        style: ToastOptions.style,
      });
    });

    socket.on('connect_error', () => {
      toast.error('Verbindung konnte nicht hergestellt werden.', ToastOptions);

      connection_button.disabled = false;
    });
  }

  let dialog;
  let networkName = 'Wall_E_Klasse_TBA';
  let isConnectedToNetwork = false;
  let currentStep = 1;
</script>

<svelte:window
  on:keydown={(event) => {
    if (event.key === 'Enter') {
      connect();
    }
  }}
/>

<DialogContainer bind:this={dialog} showDialog={true} showCloseButton={false}>
  <h1 class="font-serif text-white text-2xl">Verbindung herstellen</h1>
  <ol
    class="flex items-center my-6 mx-auto w-1/2 text-sm font-medium text-center text-gray-500 dark:text-gray-400 sm:text-base"
  >
    <li
      class="flex md:w-full items-center text-mb-blue sm:after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700"
    >
      <span
        class="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:font-light after:text-gray-200 dark:after:text-gray-500"
      >
        {#if currentStep >= 1}
          <svg
            aria-hidden="true"
            class="w-4 h-4 mr-2 sm:w-5 sm:h-5"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
            ><path
              fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clip-rule="evenodd"
            /></svg
          >
        {:else}
          <span class="mr-2">1</span>
        {/if}
        Wifi <span class="hidden sm:inline-flex sm:ml-2">Verbindung</span>
      </span>
    </li>
    <li class="flex items-center {currentStep == 2 ? 'text-mb-blue' : ''}">
      {#if currentStep == 2}
        <svg
          aria-hidden="true"
          class="w-4 h-4 mr-2 sm:w-5 sm:h-5"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
          ><path
            fill-rule="evenodd"
            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
            clip-rule="evenodd"
          /></svg
        >
      {:else}
        <span class="mr-2">2</span>
      {/if}
      Verbinden
    </li>
  </ol>
  <div class="flex flex-col justify-start">
    <p class="text-gray-500">
      Verbinde dich mit dem WLAN <span class="font-bold text-mb-blue">{networkName}</span> und gib anschließend die IP-Adresse
      deiner Wall-E Einheit an.
    </p>
    <div class="flex flex-row-reverse justify-end gap-2 text-mb-text my-2">
      <label for="is-connected-to-network">Ich habe mich mit dem Netzwerk verbunden.</label>
      <input
        type="checkbox"
        id="is-connected-to-network"
        bind:checked={isConnectedToNetwork}
        on:change={() => (isConnectedToNetwork ? currentStep++ : currentStep--)}
      />
    </div>
  </div>
  <div class="mt-4 flex flex-grow gap-3 {isConnectedToNetwork ? 'opacity-100 cursor-not-allowed' : 'opacity-20'}">
    <input
      type="text"
      placeholder="IP-Adresse"
      id="ip-address"
      class="h-8 px-2 flex-1 bg-gray-10 outline-none focus:outline-mb-blue font-mono rounded-sm"
      disabled={!isConnectedToNetwork}
    />
    <button
      class="bg-mb-blue disabled:bg-mb-blue/50 w-24 h-8 rounded-sm"
      on:click={() => isConnectedToNetwork && connect()}
      id="connection-button"
      disabled={!isConnectedToNetwork}>Verbinden</button
    >
  </div>
</DialogContainer>
