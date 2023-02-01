<script lang="ts">
  import StepperIcon from './StepperIcon.svelte';
  import StepperText from './StepperText.svelte';

  export let currentStep;
  export let steps: string[];
</script>

<ol
  class="flex items-center my-6 mx-auto w-full text-sm font-medium text-center text-gray-500 dark:text-gray-400 sm:text-base"
>
  {#each steps as step, index}
    {#if index == 0}
      <li
        class="flex md:w-full items-center text-mb-blue sm:after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700"
      >
        <span
          class="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:font-light after:text-gray-200 dark:after:text-gray-500"
        >
          <StepperIcon {index} {currentStep} />
          <StepperText {step} />
        </span>
      </li>
    {:else if index + 1 == steps.length}
      <li class="flex items-center {currentStep >= index + 1 ? 'text-mb-blue' : ''}">
        <span
          class="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:font-light after:text-gray-200 dark:after:text-gray-500"
        >
          <StepperIcon {index} {currentStep} />
          <StepperText {step} />
        </span>
      </li>
    {:else}
      <li
        class="flex md:w-full items-center after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700 {currentStep >=
        index + 1
          ? 'text-mb-blue'
          : ''}"
      >
        <span
          class="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:font-light after:text-gray-200 dark:after:text-gray-500"
        >
          <StepperIcon {index} {currentStep} />
          <StepperText {step} />
        </span>
      </li>{/if}
  {/each}
</ol>
