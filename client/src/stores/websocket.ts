import { writable } from 'svelte/store';

export const socket = writable(null); // Stores the websocket object
export const isConnected = writable(false); // Stores whether the websocket is connected or not
export const ipAddress = writable(null); // Stores the IP address of the server (used for the Livestream)
