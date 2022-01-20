<script>
    import { fade } from 'svelte/transition';
</script>

<div class="container" in:fade={{duration: 100, delay: 50}}>
    <table border="5" bgcolor=#f0ffff>
        <tr>
            <th>Автор приложения</th>
            <th>Плетнёв Антон Сергеевич</th>
        </tr>
        <tr>
            <th>Группа</th>
            <th>ПИ18-1</th>
        </tr>
        <tr>
            <th>Вид работы</th>
            <th>Курсовая</th>
        </tr>
        <tr>
            <th>Год</th>
            <th>2020</th>
        </tr>
    </table>
</div>