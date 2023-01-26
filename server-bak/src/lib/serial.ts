import { SerialPort } from 'serialport';
import consola from 'consola';

let path: string;
let ArduinoPort: SerialPort;

SerialPort.list().then((ports) => {
  let done = false;
  let count = 0;
  let allPorts = ports.length;

  ports.forEach((port) => {
    count++;
    const pm = port.manufacturer;

    if (typeof pm !== 'undefined' && pm.includes('arduino')) {
      path = port.path;
      ArduinoPort = new SerialPort({ path, baudRate: 9600 });
      ArduinoPort.on('open', () => {
        consola.success(`Connected! Arduino is now connected at port ${path}`);
      });
      done = true;
    }

    if (count === allPorts && done === false) {
      consola.error(`Can't find any Arduino!`);
      throw new Error("Can't find any Arduino!");
    }
  });
});

export default ArduinoPort;
