import WebSocket, { WebSocketServer } from 'ws';
import { v4 as uuidv4 } from 'uuid';
import consola from 'consola';
import { IncomingMessage } from 'http';
import ArduinoPort from '../lib/serial';

function createNewConnection(address: string | undefined) {
  return {
    id: uuidv4(),
    address: address || 'unknown',
  };
}

export default async function serve(port: number): Promise<void> {
  const server = new WebSocketServer({ port });

  let activeConnections: Record<string, any> = {};

  server.on('connection', (socket: WebSocket, request: IncomingMessage) => {
    const connection = createNewConnection(request.socket.remoteAddress);

    activeConnections[connection.id] = { address: connection.address, socket };

    consola.info(`New connection: ${connection.id} from ${connection.address}`);

    socket.send(JSON.stringify({ type: 'success', code: 'successfull-connection', payload: { id: connection.id } }));

    if (Object.keys(activeConnections).length > 1) {
      consola.warn('More than one connection detected!');
      server.clients.forEach((socket: WebSocket) => {
        socket.send(
          JSON.stringify({
            type: 'warning',
            code: 'more-than-one-connection',
          })
        );
      });
    }

    socket.on('message', (data: any) => {
      const message = JSON.parse(data);
      const { type, payload } = message;
      const command = type.split('/')[0];
      const subCommand = type.split('/')[1];

      if (command == 'cmd') {
        switch (subCommand) {
          case 'drive':
            consola.info('Drive command received.', payload);
            ArduinoPort.write('d', (error) => {
              if (error) {
                consola.error(error);
              }
              consola.info('Drive command sent to Arduino.');
            });
            break;
          case 'arpo':
            consola.info('Arpo command received.', payload);
            break;
          case 'alpo':
            consola.info('Alpo command received.', payload);
            break;
          case 'head':
            consola.info('Head command received.', payload);
            break;
        }
      } else if (command == 'kick') {
        const id = payload.id;
        if (activeConnections[id]) {
          activeConnections[id].socket.send(
            JSON.stringify({
              type: 'kick',
              code: 'kicked-by-server',
            })
          );
          activeConnections[id].socket.close();
        }
      } else if (command == 'connections') {
        consola.info(`[${connection.address}] Requested active connections.`);
        socket.send(
          JSON.stringify({
            type: 'connections/response',
            payload: Object.keys(activeConnections).map((connection) => {
              return {
                id: connection,
                address: activeConnections[connection].address,
              };
            }),
          })
        );
      } else {
        consola.warn(`[${connection.address}] Sent unknown command: ${command}`);
        socket.send(JSON.stringify({ type: 'error', code: 'unknown-command' }));
      }
    });

    socket.on('close', () => {
      delete activeConnections[connection.id];
      consola.info(`Connection closed: ${connection.id}`);
    });
  });
}
