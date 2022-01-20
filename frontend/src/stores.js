import { writable } from 'svelte/store';

function musicsCreate() {
    const { subscribe, set } = writable({});

    return {
        subscribe,
        set: async (object) => set(object),
    };
}

function musicPayerCreate() {
    const { subscribe, set, update } = writable(undefined);

    return {
        subscribe,
        set: async (object) => set(object),
        changeStatus: (status) => update(n => n.status = status),
        reset: () => set(undefined)
    };
}

function currentPageCreate() {
    const { subscribe, set, update } = writable('index');

    return {
        subscribe,
        set: async (object) => set(object),
        changePage: async (page) => set(page),
        reset: () => set('index')
    };
}

export const currentPage = currentPageCreate();

export const musics = musicsCreate();
export const musicPlayer = musicPayerCreate();
