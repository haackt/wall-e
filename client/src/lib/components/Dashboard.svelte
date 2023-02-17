<script lang="ts">
  import DashboardButton from './Dashboard/DashboardButton.svelte';
  import Joystick from './Dashboard/Joystick.svelte';
  import ServoDialog from './Dialogs/ServoDialog.svelte';
  import { socket, ipAddress } from '../../stores/websocket';
  import Cog from './Icons/cog.svelte';
  import Laser from './Icons/laser.svelte';
  import SpeakDialog from './Dialogs/SpeakDialog.svelte';
  import Speaker from './Icons/speaker.svelte';
  import toast from 'svelte-french-toast';
  import { ToastOptions } from '../toast';
  import { hext } from '../../stores/servo';
  import { hasGamepad, useGamepad } from '../../stores/gamepad';
  import SwitchControlMethodButton from './Gamepad/SwitchControlMethodButton.svelte';

  function toggleLaser() {
    $socket?.emit('laser', { value: !isLaserActive });
    if (!isLaserActive) {
      $socket?.emit('hext', { value: $hext });
    }
    toast.success(`Laser ${isLaserActive ? 'de' : ''}aktiviert`, ToastOptions);
    isLaserActive = !isLaserActive;
  }

  /**
   * 
    🚧 Controller Support - WIP 🚧

   import 'joypad.js';

  let driveValues = {
    speed: 0,
    degrees: 0,
  };


  const BUTTON_MAP = {
    0: 'A',
    1: 'B',
    2: 'X',
    3: 'Y',
    4: 'LB',
    5: 'RB',
    6: 'LT',
    7: 'RT',
    8: 'BACK',
    9: 'START',
    10: 'L3',
    11: 'R3',
    12: 'UP',
    13: 'DOWN',
    14: 'LEFT',
    15: 'RIGHT',
  };

  function driveForward() {
    driveValues.speed = 50;
  }
  function driveBackwards() {
    driveValues.speed = -50;
  }

  function setDirection(value) {}

  function moveHead(type, value) {}

  function playSound(soundTag: string) {
    toast.success(`Erfolgreich '${soundTag}' abgespielt.`, {
      style: ToastOptions.style,
      icon: '🔊',
    });
    $socket?.emit(`speak/${soundTag}`);
  }

  //@ts-ignore
  const joypad = window.joypad;

  joypad.on('connect', () => {
    $hasGamepad = true;
    $useGamepad = true;
  });

  joypad.on('button_press', (e) => {
    if (!$useGamepad) return;

    const buttonName = BUTTON_MAP[e.detail.index];

    switch (buttonName) {
      case 'X':
        toggleLaser();
        break;
      case 'RT':
        driveForward();
        break;
      case 'LT':
        driveBackwards();
        break;
      case 'Y':
        playSound('slogan');
        break;
      case 'B':
        playSound('way');
        break;
      case 'A':
        playSound('story');
        break;
      case 'RB':
        playSound('follow');
        break;
      case 'LB':
        playSound('follow');
        break;
      case 'L3':
        playSound('thanks');
        break;
      case 'R3':
        playSound('language');
        break;
      case 'START':
        playSound('welcome');
        break;
    }
  });

  joypad.on('axis_move', (e) => {
    const { stickMoved, axisMovementValue, directionOfMovement } = e.detail;
    if (stickMoved == 'left_stick') {
      const inputMin = -100,
        inputMax = 100,
        outputMin = -49,
        outputMax = 49;
      driveValues.degrees =
        outputMin + ((outputMax - outputMin) * (axisMovementValue * 100 - inputMin)) / (inputMax - inputMin);
    } else {
      moveHead(directionOfMovement, axisMovementValue);
    }
  });
*/
  let servoDialog;
  let speakDialog;
  let isLaserActive = false;
</script>

<ServoDialog bind:this={servoDialog} />
<SpeakDialog bind:this={speakDialog} />

<div class="h-full flex flex-col justify-around gap-12 lg:flex-row lg:gap-8">
  <div class="flex flex-col justify-center gap-2 lg:gap-4">
    <h1 class="font-serif text-white text-3xl">Video</h1>
    <img
      src={`https://${$ipAddress}:1507/`}
      alt="Wall-E Live Video Feed"
      class="aspect-4/3 w-[740px] h-[480px] bg-black rounded-md"
    />
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
        <DashboardButton onClick={() => toggleLaser()}>
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
  <div class="flex flex-col gap-4 justify-center items-center">
    {#if !$hasGamepad || !$useGamepad}
      <div>
        <Joystick />
      </div>
      {#if $hasGamepad}
        <SwitchControlMethodButton onClick={() => ($useGamepad = true)}>Gamepad benutzen</SwitchControlMethodButton>
      {/if}
    {:else if $hasGamepad && $useGamepad}
      <SwitchControlMethodButton onClick={() => ($useGamepad = false)}>Joystick benutzen</SwitchControlMethodButton>
    {/if}
  </div>
</div>
