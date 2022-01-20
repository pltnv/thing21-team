<script>
    import {Nav} from 'svelte-chota';
    import {Input,Field,Button} from 'svelte-chota';
    import {currentPage} from "../stores"

</script>

<Nav>
    <a slot="left">
        ESHAR
    </a>

    <a slot="right" class="cursor-pointer" on:click={() => (currentPage.changePage('about'))}>О программе</a>
    <a slot="right" class="cursor-pointer" on:click={() => (currentPage.changePage('aboutAuthor'))}>Об авторе</a>
    <a slot="right" class="cursor-pointer" on:click={() => (currentPage.reset())}>Библиотека</a>
</Nav>

<style>
    .cursor-pointer {
        cursor: pointer;
    }
</style>
