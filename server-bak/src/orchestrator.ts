import consola from 'consola';
import fastify, { FastifyReply, FastifyRequest } from 'fastify';

import generateRandomNumber from './lib/random';
import ServeWebsocket from './servers/websocket';

const ORCHESTRATOR_PORT = 1606;
const HLS_PORT = generateRandomNumber(5000, 6000);
const WS_PORT = generateRandomNumber(7000, 8000);

const orchestrator = fastify({ logger: false });

orchestrator.get('/', async (_: FastifyRequest, reply: FastifyReply) => {
  reply.header('Access-Control-Allow-Origin', '*');
  reply.header('Access-Control-Allow-Methods', '*');
  reply.header('Access-Control-Allow-Headers', '*');

  reply
    .type('application/json')
    .code(200)
    .send({
      status: 200,
      message: 'Orchestrator is running!',
      servers: {
        hls_port: HLS_PORT,
        ws_port: WS_PORT,
      },
    });
});

(async () => {
  consola.info('Starting orchestrator...');

  orchestrator.listen({ port: ORCHESTRATOR_PORT }, (err) => {
    if (err) {
      consola.error(err);
      process.exit(1);
    }
    consola.info(`Orchestrator: ${ORCHESTRATOR_PORT}`);
  });

  consola.info(`WebSocket: ${WS_PORT}...`);
  ServeWebsocket(WS_PORT);
})();
