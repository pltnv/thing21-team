<script>
    import {Col, Card} from 'svelte-chota';
    import {musicPlayer} from "../stores"
    import { fade } from 'svelte/transition';

    import PlayIcon from "../icons/PlayIcon.svelte"
    import PauseIcon from "../icons/PauseIcon.svelte"
    import HeartIcon from "../icons/HeartIcon.svelte"

    export let music = {
        "label": "",
        "author": "",
        "cover": "",
        "src": "",
        "duration": 0,
        "liked": false,
        "status": false
    }

    $: minutes = Math.floor(music.duration / 60);
    $: seconds = music.duration - minutes * 60;

    async function updateMusicPlayer() {
        music.status = true;
        if ($musicPlayer) musicPlayer.changeStatus(false)
        await musicPlayer.set(music);
    }

</script>

<div class="music-card" transition:fade={{duration: 100}}>
    <div class="is-left">
        <div class="play-button" on:click={updateMusicPlayer}>
            {#if music.status}
                <PauseIcon/>
            {:else}
                <PlayIcon/>
            {/if}
        </div>
        <img src="{music.cover}" alt="">
        <div class="labels">
            <p>{music.label}</p>
            <span>{music.author}</span>
        </div>
    </div>
    <div class="is-right">
        <div class="time">
            {minutes}:{seconds}
        </div>
<!--        <HeartIcon/>-->
    </div>
</div>

<style>

    .play-button {
        margin-right: 14px;
    }

    .music-card {
        display: flex;
        justify-content: space-between;
        flex: 1 0 25%;
        margin: 5px;
        padding: 1rem 2rem;
        border-radius: 10px;
        background: #fff;
        box-shadow: 0 1px 3px rgba(0,0,0,.3);
    }

    img {
        height: 50px;
        border-radius: 4px;
    }

    p {
        margin: 0;
    }

    .labels {
        margin-left: 1em;
        display: flex;
        flex-direction: column;
        justify-content: center;
        height: 100%;
    }

    .labels span {
        font-size: 0.8em;
        color: rgb(99, 99, 99);
    }

    .labels p {
        font-weight: 600;
    }

    .time {
        font-size: 0.8em;
        color: rgb(99, 99, 99);
        margin-right: 10px;
    }
</style>
