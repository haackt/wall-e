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
  <p class="text-gray-500">Stelle eine Verbindung zu deiner Wall-E Einheit her, um das Web-Interface nutzen zu können.</p>
  <div class="mt-4 flex flex-grow gap-3">
    <input
      type="text"
      placeholder="IP-Adresse"
      id="ip-address"
      class="h-8 px-2 flex-1 bg-mb-dark outline-none focus:outline-mb-blue font-mono rounded-sm"
    />
    <button
      class="bg-mb-blue disabled:bg-mb-blue/50 disabled:cursor-progress w-24 h-8 rounded-sm"
      on:click={() => connect()}
      id="connection-button">Verbinden</button
    >
  </div>
</DialogContainer>
