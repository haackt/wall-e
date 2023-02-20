<script lang="ts">
  import { onMount } from 'svelte';
  import { socket } from '../../../stores/websocket';

  let currentSpeed = 50;
  let currentDirection = 50;

  onMount(() => {
    const canvas = document.getElementById('joystick') as HTMLCanvasElement;
    const context = canvas.getContext('2d') as CanvasRenderingContext2D;
    
    // Variable to store the position of the joystick
    const joystickPosition = {
      x: canvas.width / 2,
      y: canvas.height / 2,
    };

    // Variable to store the current position of the joystick
    const currentPositon = {
      x: 0,
      y: 0,
    };

    // Variable to store the last translated position of the joystick
    const lastTranslatedPosition = {
      speed: 0,
      degrees: 0,
    };

    // Variable to store, whether the joystick is being dragged
    let isDragging = false;

    // Create a new image object for the joystick handle
    const handleImage = new Image();
    
    // Set the source of the handle image
    handleImage.src = '/logo.svg';

    // Set the width and height of the handle image to upscale it
    handleImage.width = 80;
    handleImage.height = 80;

    // Draw the handle image at the specified coordinates
    function drawHandle(x: number, y: number) {
      // Draw the handle image
      context.drawImage(
        handleImage,
        x - handleImage.width / 2, // Center the handle image horizontally
        y - handleImage.height / 2, // Center the handle image vertically
        handleImage.width, // Scale the handle image to the specified width
        handleImage.height // Scale the handle image to the specified height
      );
    }

    // Draw the handle image once the image has loaded
    handleImage.onload = function () {
      requestAnimationFrame(draw); // Request first animation frame
    };

    // Function to draw the joystick
    function draw() {
      // Clear the canvas
      context.clearRect(0, 0, canvas.width, canvas.height);

      // Draw the handle image
      drawHandle(joystickPosition.x, joystickPosition.y);

      // Request the next animation frame
      requestAnimationFrame(draw);
    }

    // Function to handle the start of the drag event
    function startDrag(e) {
      isDragging = true; // Set the dragging state to true

      // Change the cursor to the grabbing cursor
      canvas.style.cursor = 'grab';

      // Set current position to the position of the touch or mouse event
      if (e.type === 'touchstart') {
        currentPositon.x = e.touches[0].clientX - canvas.offsetLeft;
        currentPositon.y = e.touches[0].clientY - canvas.offsetTop;
      } else if (e.type === 'mousedown') {
        currentPositon.x = e.clientX - canvas.offsetLeft;
        currentPositon.y = e.clientY - canvas.offsetTop;
      }
    }

    // Function to handle the drag event
    function handleDrag(e) {
      // Check if the joystick is being dragged
      if (!isDragging) {
        return;
      }

      // Prevent the default behavior of the event
      e.preventDefault();

      // Check if is a touch or mouse event
      if (e.type === 'touchmove') {
        // Get the touch coordinates
        currentPositon.x = e.touches[0].pageX - canvas.offsetLeft;
        currentPositon.y = e.touches[0].pageY - canvas.offsetTop;
      } else if (e.type === 'mousemove') {
        // Get the mouse coordinates
        currentPositon.x = e.pageX - canvas.offsetLeft;
        currentPositon.y = e.pageY - canvas.offsetTop;
      }

      // Check if joystick is outside the canvas
      // Reset the distance to 0, if the joystick is outside the canvas
      const EDGE_THRESHOLD = 25; // Threshold to prevent the joystick from going outside the canvas

      if (currentPositon.x < EDGE_THRESHOLD) {
        currentPositon.x = EDGE_THRESHOLD;
      } else if (currentPositon.x > canvas.width - EDGE_THRESHOLD) {
        currentPositon.x = canvas.width - EDGE_THRESHOLD;
      }

      if (currentPositon.y < EDGE_THRESHOLD) {
        currentPositon.y = EDGE_THRESHOLD;
      } else if (currentPositon.y > canvas.height - EDGE_THRESHOLD) {
        currentPositon.y = canvas.height - EDGE_THRESHOLD;
      }

      // Set the joystick position to the current position
      joystickPosition.x = currentPositon.x;
      joystickPosition.y = currentPositon.y;

      // Translate the joystick position to a value pair
      const speed = translateJoystickPosition(joystickPosition.y, 0, 100);
      const degrees = translateJoystickPosition(joystickPosition.x, 0, 100);
      
      // Check if the speed and degrees have changed
      if (speed === lastTranslatedPosition.speed && degrees === lastTranslatedPosition.degrees) {
        return;
      }

      currentSpeed = speed;
      currentDirection = degrees;

      // Set the last translated position to the current position
      lastTranslatedPosition.speed = speed;
      lastTranslatedPosition.degrees = degrees;
    }

    // Function to handle the end of the drag event
    function endDrag() {
      // Reset the joystick position to the center of the canvas
      joystickPosition.x = canvas.width / 2;
      joystickPosition.y = canvas.height / 2;

      // Reset the current position to the center of the canvas
      currentPositon.x = canvas.width / 2;
      currentPositon.y = canvas.height / 2;

      // Set the dragging state to false
      isDragging = false;

      // Set the cursor to the default cursor
      canvas.style.cursor = 'auto';

      currentSpeed = 0;
      currentDirection = 0;
    }

    /**
     * Translates the joystick position to a value pair between -50 and 50
     * X determines the speed, Y determines the direction
     * @param {Number} x
     * @param {Number} y
     * @returns {Object} { speed: Number, degrees: Number }
     */
    function translateJoystickPosition(input: number, outMin: number, outMax: number): number {
      // The inputMin and inputMax constants define the minimum and maximum values that x and y can take,
      // respectively. These values are used to normalize the joystick position.
      // The outputMin and outputMax constants define the minimum and maximum values that the output speed
      // and degrees can take. These values are used to scale the normalized joystick position to the desired range.
      const inputMin = 25,
        inputMax = 325,
        outputMin = outMin,
        outputMax = outMax;

      // The variables are calculated by normalizing the values using the inputMin and
      // inputMax constants, and then scaling it using the outputMin and outputMax constants.
      let output = outputMin + ((outputMax - outputMin) * (input - inputMin)) / (inputMax - inputMin);

      return Math.round(output);
    }

    // Add event listeners for the start of the drag event
    canvas.addEventListener('touchstart', startDrag);
    canvas.addEventListener('mousedown', startDrag);

    // Add event listeners for the drag event
    canvas.addEventListener('touchmove', handleDrag);
    canvas.addEventListener('mousemove', handleDrag);

    // Add event listeners for the end of the drag event
    canvas.addEventListener('touchend', endDrag);
    canvas.addEventListener('touchcancel', endDrag);
    canvas.addEventListener('mouseup', endDrag);
    canvas.addEventListener('mouseleave', endDrag);
    
    setInterval(() => {
      // Send the speed and degrees to the server
      $socket.emit('driv', { speed: currentSpeed, degrees: currentDirection });
    }, 1000);
  });
</script>

<div class="flex justify-center flex-col text-center gap-4">
  <canvas width="350px" height="350px" class="bg-mb-darker aspect-square rounded-md" id="joystick" />
  <div class="flex justify-between text-sm">
    <label for="joystick" class="text-mb-text-muted"
      >Geschwindigkeit: <span class="text-mb-text">{currentSpeed == 49 ? 50 : currentSpeed}</span></label
    >
    <label for="joystick" class="text-mb-text-muted"
      >Richtung: <span class="text-mb-text">{currentDirection == 49 ? 50 : currentDirection}</span></label
    >
  </div>
</div>
