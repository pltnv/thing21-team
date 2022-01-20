<script>
    import {Input, Field, Button} from 'svelte-chota';
    import {serverURL} from "../constans";
    import MusicCard from "./MusicCard.svelte";
    import {Radio} from 'svelte-chota';

    let value = '';
    let musics = [];
    let radiovalue = "1";


    async function searchTrack() {
        if (value) {
            const res = await fetch(serverURL + 'music/filter/' + value + '/');
            const json = await res.json();
            musics = json;
            console.log(json)
        }

    }

    $: if (value) {
        searchTrack()
    }

    $: filtredMusics = musics.sort((a, b) => ((radiovalue === '1' ? a.duration > b.duration : a.duration < b.duration) ? 1 : -1))

</script>


<Field gapless>
    <Input placeholder="Введите название трека" bind:value/>
</Field>

<Radio value="1" bind:group={radiovalue}>Сортировка: меньшая длительность</Radio>
<Radio value="0" bind:group={radiovalue}>Сортировка: большая длительность</Radio>

<div class="music-card-block">
    {#each filtredMusics as music}
        <MusicCard music={music}/>
    {:else}
        {#if value}
            <p>Ни одного трека не найдено</p>
        {:else}
            <p>Напишите название трека или автора</p>
        {/if}
    {/each}
</div>

<style>
    .music-card-block {
        display: flex;
        flex-wrap: wrap;
    }
</style>