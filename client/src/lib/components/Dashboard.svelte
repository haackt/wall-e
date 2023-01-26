<script lang="ts">
  import DashboardButton from './Dashboard/DashboardButton.svelte';
  import Joystick from './Dashboard/Joystick.svelte';
  import ServoDialog from './Dialogs/ServoDialog.svelte';
  import CPUChip from './Icons/cpu-chip.svelte';
  import Microphone from './Icons/microphone.svelte';
  import { ipAddress } from '../../stores/websocket';
  import Cog from './Icons/cog.svelte';
  import Laser from './Icons/laser.svelte';
  import SpeakDialog from './Dialogs/SpeakDialog.svelte';
  import Speaker from './Icons/speaker.svelte';

  let servoDialog;
  let speakDialog;
  let isLaserActive = false;
</script>

<ServoDialog bind:this={servoDialog} />
<SpeakDialog bind:this={speakDialog} />

<div class="h-full flex flex-col gap-12 lg:flex-row lg:gap-8">
  <div class="flex-1 flex flex-col gap-2 lg:gap-4">
    <h1 class="font-serif text-white text-3xl">Video</h1>
    <img src={`http://${$ipAddress}:1507/`} alt="" class="lg:w-[700px] lg:h-[540px] aspect-4/3 bg-black rounded-md" />
    <ul class="flex flex-nowrap items-center overflow-x-auto text-sm md:text-base gap-4 mt-2 text-mb-text">
      <li>
        <DashboardButton onClick={() => servoDialog.show()}>
          <Cog tooths={8} width="w-5" height="h-5" />
          <span>Servo-Steuerung</span>
        </DashboardButton>
      </li>
      <li>
        <DashboardButton onClick={() => speakDialog.show()}>
          <Speaker width="w-5" height="h-5" />
          <span>Sprechen</span>
        </DashboardButton>
      </li>
      <li>
        <DashboardButton onClick={() => (isLaserActive = !isLaserActive)}>
          <Laser width="w-5" height="h-5" />
          <span
            >Laser
            {#if isLaserActive}
              deaktivieren
            {:else}
              aktivieren
            {/if}
          </span>
        </DashboardButton>
      </li>
    </ul>
  </div>
  <div class="flex flex-1 justify-center items-center">
    <Joystick />
  </div>
</div>
