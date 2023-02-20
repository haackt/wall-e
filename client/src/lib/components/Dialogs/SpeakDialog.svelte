<script lang="ts">
  import ArrowsUpDown from '../Icons/arrows-up-down.svelte';
  import Film from '../Icons/film.svelte';
  import HandRaised from '../Icons/hand-raised.svelte';
  import PaperPlane from '../Icons/paper-plane.svelte';
  import ThumbsUp from '../Icons/thumbs-up.svelte';
  import DialogContainer from './DialogContainer.svelte';
  import SpeakDialogButton from './SpeakDialogButton.svelte';
  import { socket } from '../../../stores/websocket';
  import toast from 'svelte-french-toast';
  import Star from '../Icons/star.svelte';
  import { ToastOptions } from '../../toast';

  export function show() {
    dialog.show();
  }

  export function hide() {
    dialog.hide();
  }

  function play(soundTag: string) {
    if (playLocally) {
      const audio = new Audio(`/sounds/${soundTag}.wav`);
      audio.play();
    } else {
      $socket?.emit(`speak/${soundTag}`);
    }
    toast.success(`Erfolgreich '${soundTag}' auf ${playLocally ? 'Endgerät' : 'Wall-E'} abgespielt.`, {
      style: ToastOptions.style,
      icon: '🔊',
    });
  }

  let dialog;
  let playLocally = false;
</script>

<DialogContainer bind:this={dialog}>
  <h1 class="font-serif text-4xl mb-6">Sprechen</h1>
  <div class="flex gap-4 flex-col">
    <div class="flex justify-between flex-col lg:flex-row">
      <SpeakDialogButton onClick={() => play('welcome')}><HandRaised />Begrüßung</SpeakDialogButton>
      <SpeakDialogButton onClick={() => play('follow')}><PaperPlane /> Bitte Folgen</SpeakDialogButton>
      <SpeakDialogButton onClick={() => play('way')}><ArrowsUpDown /> Platz machen</SpeakDialogButton>
      <!--<SpeakDialogButton onClick={() => play('bye')}><HandRaised rotate="rotate-12" />Verabschiedung</SpeakDialogButton>-->
    </div>
    <div class="flex justify-between lg:gap-16 flex-col lg:flex-row">
      <SpeakDialogButton onClick={() => play('thanks')}>
        <ThumbsUp />
        Dankeschön
      </SpeakDialogButton>
      <SpeakDialogButton onClick={() => play('story')}>
        <Film />
        Self-Story
      </SpeakDialogButton>
      <SpeakDialogButton onClick={() => play('slogan')}>
        <Star />
        Slogan
      </SpeakDialogButton>
      <!--<SpeakDialogButton onClick={() => play('language')}>
        <Language width="w-5" height="h-5" />
        Beleidigen
      </SpeakDialogButton>-->
    </div>
    <hr class="bg-mb-dark" />
    <div class="text-mb-text-muted flex items-center gap-2">
      <input
        type="button"
        id="play-locally"
        class="w-5 h-5 border text-xs text-mb-dark border-slate-800 rounded focus:ring-3 hover:cursor-pointer focus:ring-mb-blue {playLocally
          ? 'bg-mb-blue'
          : 'bg-mb-dark'}"
        on:click={() => (playLocally = !playLocally)}
        value="✓"
      />
      <label for="play-locally" class="hover:cursor-pointer">Audio auf Endgerät wiedergeben</label>
    </div>
  </div>
</DialogContainer>
