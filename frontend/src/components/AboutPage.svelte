<script>
    import { fade } from 'svelte/transition';
</script>

<div class="container" in:fade={{duration: 100, delay: 50}}>
    <table border="5" bgcolor="#f0ffff">
        <tr>
            <th>Название</th>
            <th>ESHAR</th>
        </tr>
        <tr>
            <td>Описание</td>
            <td>Информационно-справочная система "Музыкальный сервис"</td>
        </tr>
        <tr>
            <td>Frontend</td>
            <td>JavaScript-библиотека Svelte</td>
        </tr>
        <tr>
            <td>Backend</td>
            <td>Python-библиотека Flask</td>
        </tr>
        <tr>
            <td>БД</td>
            <td>SQLite</td>
        </tr>
        <tr>
            <td>Версия</td>
            <td>0.0.1</td>
        </tr>
    </table>
</div>
