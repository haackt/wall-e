<script lang="ts">
  import { onMount } from 'svelte';
  import toast from 'svelte-french-toast';
  import { socket as wsocket, isConnected, ipAddress } from '../../../stores/websocket';
  import io from 'socket.io-client';
  import { ToastOptions } from '../../toast';
  import DialogContainer from './DialogContainer.svelte';
  import Stepper from '../Stepper/Stepper.svelte';
  import ContinueButton from './ConnectDialog/ContinueButton.svelte';
  import ConnectStepContainer from './ConnectDialog/ConnectStepContainer.svelte';
  import BackButton from './ConnectDialog/BackButton.svelte';

  function connect() {
    toast('Verbinde...', {
      style: ToastOptions.style,
      icon: '⏳',
    });

    const socket = io(`https://${ipAddressValue}:1606/`, {
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
      $ipAddress = ipAddressValue;
      $isConnected = true;
      dialog.hide();

      $wsocket.emit('init');

      toast.success('Erfolgreich verbunden!', ToastOptions);
    });

    socket.on('message', (message) => {
      toast(message, {
        style: ToastOptions.style,
      });
    });

    socket.on('connect_error', () => {
      toast.error('Verbindung konnte nicht hergestellt werden.', ToastOptions);
    });
  }

  onMount(() => {
    window.addEventListener('message', (event) => {
      if (event.data == 'success') {
        hasInstalledCertificate = true;
      }
    });
  });

  let dialog;
  let currentStep = 1;

  let isChrome = window.chrome;
  let compileTime = new Date(__COMPILE_TIME__);
  
  let networkName = 'Wall_E_Klasse_TBA';
  let isConnectedToNetwork = false;

  let ipAddressValue = '';
  let isValidIPAddress = false;
  $: isValidIPAddress =
    ipAddressValue.match(/^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/) != null;

  let hasInstalledCertificate = false;
</script>

<DialogContainer bind:this={dialog} showDialog={true} showCloseButton={false}>
  {#if isChrome}
    <div class="w-full bg-red-500/40 rounded-md px-2 py-4 mb-4">
      <h1 class="font-serif text-xl font-bold flex items-center gap-2 text-red-50 mb-2">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-6 h-6"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z"
          />
        </svg>
        Hinweis
      </h1>
      <div class="flex flex-col gap-2">
        <p>
          Um die Web-Benutzeroberfläche optimal nutzen zu können, empfehlen wir die Verwendung von einem Nicht-Chromium
          basierten Browser.
        </p>
        <p>
          Bitte beziehen Sie in betracht zu <a
            rel="noreferrer"
            href="https://www.mozilla.org/de/firefox/new/"
            target="_blank"
            class="text-mb-blue font-serif font-bold">Firefox</a
          >
          oder
          <a rel="noreferrer" href="https://www.apple.com/de/safari/" target="_blank" class="text-mb-blue font-serif font-bold"
            >Safari</a
          > zu wechseln.
        </p>
      </div>
    </div>
  {/if}
  <h1 class="font-serif text-white text-2xl">Verbindung herstellen</h1>
  <Stepper bind:currentStep steps={['Wi-Fi', 'IP-Adresse', 'SSL Zertifikat', 'Fertig']} />
  {#if currentStep == 1}
    <ConnectStepContainer>
      <div slot="content">
        <p class="text-gray-500">
          Deine Wall-E Einheit besitzt ein eigenes WLAN-Netzwerk. Bitte verbinde dich mit diesem Netzwerk.
        </p>
        <p class="text-gray-500">
          Das Netzwerk sollte unter dem Namen <strong class="font-bold text-mb-blue">{networkName}</strong> erscheinen.
        </p>
        <div class="flex flex-row-reverse justify-end gap-2 text-mb-text my-2">
          <label for="is-connected-to-network">Ich habe mich mit dem Netzwerk verbunden.</label>
          <input type="checkbox" id="is-connected-to-network" bind:checked={isConnectedToNetwork} />
        </div>
      </div>
      <div slot="action" class="flex justify-between">
        <div>&nbsp;</div>
        <ContinueButton onClick={() => currentStep++} disabled={!isConnectedToNetwork} />
      </div>
    </ConnectStepContainer>
  {:else if currentStep == 2}
    <ConnectStepContainer>
      <div slot="content" class="flex flex-col gap-2">
        <p class="text-mb-text-muted">Um den Wall-E steuern zu können, musst du seine IP-Adresse angeben.</p>
        <input
          type="text"
          placeholder="IP-Adresse"
          id="ip-address"
          bind:value={ipAddressValue}
          class="h-8 p-2 flex-1 bg-gray-10 outline-none {!isValidIPAddress
            ? 'text-red-500 focus:outline-red-500'
            : 'focus:outline-mb-blue'}  text-mb-darker font-mono rounded-sm"
        />
        {#if !isValidIPAddress}
          <label for="ip-address" class="text-red-500"> Das ist keine gültige IP-Adresse. </label>
        {/if}
      </div>
      <div slot="action" class="flex justify-between">
        <BackButton onClick={() => currentStep--} />
        <ContinueButton
          disabled={!isValidIPAddress}
          onClick={() => {
            if (ipAddressValue == '') {
              toast.error('Bitte gib eine IP-Adresse an.', ToastOptions);
            } else {
              currentStep++;
            }
          }}
        />
      </div>
    </ConnectStepContainer>
  {:else if currentStep == 3}
    <ConnectStepContainer>
      <div slot="content" class="text-mb-text-muted">
        <p>Um eine sichere Verbindung herzustellen, musst du das SSL Zertifikat auf deinem Gerät installieren.</p>
        <p>Öffne dazu die folgende URL in deinem Browser:</p>
        <p class="font-mono my-2 text-mb-blue">
          &rarr; <button
            on:click={() => {
              const popup = window.open(`https://${ipAddressValue}:1606/trust`, '_blank', 'width=600,height=600');
              window.addEventListener('message', (event) => {
                if (event.data == 'wall-e-cert-success') {
                  popup.close();
                  hasInstalledCertificate = true;
                }
              });
            }}>https://{ipAddressValue}:1606/trust</button
          >
        </p>
        <p>
          Folge anschließend den Anweisungen auf dem Bildschirm. Wenn du fertig bist, kannst du mit dem nächsten Schritt
          fortfahren.
        </p>
        <div class="flex flex-row-reverse justify-end gap-2 text-mb-text mt-4">
          <label for="is-connected-to-network">Ich habe das SSL-Zertifikat installiert.</label>
          <input type="checkbox" id="is-connected-to-network" bind:checked={hasInstalledCertificate} />
        </div>
      </div>
      <div slot="action" class="flex justify-between">
        <BackButton onClick={() => currentStep--} />
        <ContinueButton
          disabled={!hasInstalledCertificate}
          onClick={() => {
            if (hasInstalledCertificate) {
              currentStep++;
            }
          }}
        />
      </div>
    </ConnectStepContainer>
  {:else if currentStep == 4}
    <ConnectStepContainer>
      <div slot="content" class="text-mb-text-muted">
        <p>Du kannst nun die Verbindung herstellen.</p>
        <button
          class="bg-mb-blue disabled:bg-mb-blue/50 px-4 py-2 rounded-sm text-mb-text my-3"
          on:click={() => {
            connect();
          }}>&rarr; Verbinden</button
        >
        <p>
          Sollten Probleme auftreten, kannst du den Prozess jederzeit erneut starten. Dazu klickst du auf den Button unten.
        </p>
        <button
          class="bg-red-500 px-4 py-2  rounded-sm text-mb-text my-3"
          on:click={() => {
            currentStep = 1;
            isValidIPAddress = false;
            ipAddressValue = '';
            isConnectedToNetwork = false;
            hasInstalledCertificate = false;
          }}>&orarr; Neustarten</button
        >
      </div>
      <div slot="action" class="flex justify-between">
        <BackButton onClick={() => currentStep--} />
        <ContinueButton disabled={true} onClick={() => {}} />
      </div>
    </ConnectStepContainer>
  {/if}
 <div class="text-sm flex justify-center my-2">Letzte Version: {compileTime.toLocaleString()}</div>
</DialogContainer>
