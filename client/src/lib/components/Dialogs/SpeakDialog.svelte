<script lang="ts">
  import ArrowsUpDown from '../Icons/arrows-up-down.svelte';
  import Film from '../Icons/film.svelte';
  import HandRaised from '../Icons/hand-raised.svelte';
  import Laser from '../Icons/laser.svelte';
  import PaperPlane from '../Icons/paper-plane.svelte';
  import ThumbsUp from '../Icons/thumbs-up.svelte';
  import DialogContainer from './DialogContainer.svelte';
  import SpeakDialogButton from './SpeakDialogButton.svelte';
  import { socket } from '../../../stores/websocket';
  import toast from 'svelte-french-toast';
  import Star from '../Icons/star.svelte';

  export function show() {
    dialog.show();
  }

  export function hide() {
    dialog.hide();
  }

  function play(soundTag: string) {
    toast.success(`Successfully played ${soundTag}`);
    $socket?.emit(`speak/${soundTag}`);
  }

  let dialog;
</script>

<DialogContainer bind:this={dialog}>
  <h1 class="font-serif text-4xl mb-6">Sprechen</h1>
  <div class="flex gap-4 flex-col">
    <div class="flex justify-between flex-col lg:flex-row">
      <SpeakDialogButton onClick={() => play('welcome')}><HandRaised />Begrüßung</SpeakDialogButton>
      <SpeakDialogButton onClick={() => play('follow')}><PaperPlane /> Bitte Folgen</SpeakDialogButton>
      <SpeakDialogButton onClick={() => play('way')}><ArrowsUpDown /> Platz machen</SpeakDialogButton>
      <SpeakDialogButton onClick={() => play('laser')}>
        <Laser width="w-5" height="h-5" />
        Laser
      </SpeakDialogButton>
      <SpeakDialogButton onClick={() => play('bye')}><HandRaised rotate="rotate-12" />Verabschiedung</SpeakDialogButton>
    </div>
    <div class="flex justify-center lg:gap-16 flex-col lg:flex-row">
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
    </div>
  </div>
</DialogContainer>
