import { writable } from 'svelte/store';

export const socket = writable(null);
export const isConnected = writable(false);
