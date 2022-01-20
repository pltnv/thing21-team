<script>
    import {Input} from 'svelte-chota';
    import {Container, Row, Col, Card} from 'svelte-chota';
    import {musicPlayer} from "../stores"
    import { fade } from 'svelte/transition';
    import AudioPlayer from "../components/AudioPlayer.svelte"

    let music = {}

    let audio;
    let paused = true;
    let volume = 1;
    let src = '';

    $: if ($musicPlayer) {
        src = $musicPlayer.src
    }

    $: if (volume && audio) {
        audio.volume = volume
    }

</script>

{#if $musicPlayer}
    <div transition:fade={{duration: 100}} class:playing={!paused} class="music-player">
        <div class="container">
            <Row>
                <Col size="4">
                    <div class="music-information">
                        <img class="music-cover" src="{$musicPlayer.cover}" alt="{music.label}">
                        <div class="labels">
                            <h3>{$musicPlayer.label}</h3>
                            <p>
                                {$musicPlayer.author}
                            </p>
                        </div>
                    </div>
                </Col>
                    {#if $musicPlayer.src}
                        <div class="music-control">
                            <!--        on:play={stopOthers}-->
                            <AudioPlayer
                                    {src}
                                    bind:paused
                                    bind:this={audio}
                                    display={true}
                            />
                        </div>
                    {/if}
            </Row>
        </div>
    </div>
{/if}




<style>
    .music-box {
        display: flex;
        flex-wrap: wrap;
    }

    .music-cover {
        height: 5em;
        margin: 1em;
        margin-left: 0;
        border-radius: 10px;
        box-shadow: 0 1px 6px rgba(0, 0, 0, 0.42);
    }

    .music-player {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: white;
        box-shadow: 0 6px 24px rgba(0,0,0,.3);
    }

    .music-information {
        display: flex;
    }

    .music-control {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        display: flex;
        justify-content: center;
        flex-direction: column-reverse;
        align-items: center;
    }

    .labels {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .labels h3 {
        font-weight: 600;
        margin: 0;
    }

    .labels p {
        font-size: 0.8em;
        color: rgb(99, 99, 99);
        margin: 0;
    }

</style>
