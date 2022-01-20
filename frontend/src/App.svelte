
<script>
	import "chota";
	import NavBar from "./components/NavBar.svelte"
	import MusicApp from "./components/MusicApp.svelte"
	import MusicPlayer from "./components/MusicPlayer.svelte"
	import AboutPage from "./components/AboutPage.svelte"
	import AboutMePage from "./components/AboutMePage.svelte"
	import {musicPlayer, currentPage} from "./stores"
</script>

<main>
	<div class="container">
		<NavBar/>
	</div>
	{#if $currentPage === 'index'}
		<MusicApp/>
	{:else if $currentPage === 'about'}
		<AboutPage/>
	{:else if $currentPage === 'aboutAuthor'}
		<AboutMePage/>

	{/if}
	<MusicPlayer/>
</main>

<style>
	.main-padding {
		padding-bottom: 9em;
		/*height: 100%;*/
	}
</style>
