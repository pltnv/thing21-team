<script>
    import {Container, Row, Col, Card} from 'svelte-chota';
    import MusicCard from "./MusicCard.svelte"
    import MusicSearch from "./MusicSearch.svelte"
    import { fade } from 'svelte/transition';
    import {musics, musicPlayer} from "../stores"
    import {serverURL} from "../constans"

    async function getMusics() {
        const res = await fetch(serverURL + 'musics');
        const json = await res.json();
        await musics.set(json)
    }

</script>

<div class="container" transition:fade={{duration: 100}} >
    <Row>
        <Col>
            <h3>Случайная музыка</h3>
        </Col>
    </Row>
    <Row>
        <Col>
            <div class="music-card-block">
                {#await getMusics()}
                {:then object}
                    {#each $musics as music}
                        <MusicCard music={music}/>
                    {/each}
                {/await}
            </div>
        </Col>
    </Row>
    <Row>
        <Col>
            <h3>Поиск</h3>
        </Col>
    </Row>
    <Row>
        <Col>
            <MusicSearch/>
        </Col>
    </Row>
</div>

<style>

    .title-container-right {
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        margin: 0;
    }

    h3 {
        font-size: 2.1em;
        font-weight: 700;
        margin: 0;
    }
    .music-card-block {
        display: flex;
        flex-wrap: wrap;
    }
</style>

