<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@yield('title') | Praktikum </title>
    <style>
        body {font-family: arial, sans-serif; margin: 20px;}
        header, footer {background: #f5f5f5; padding: 10px; text-align: center;}
        nav a {margin: 0 10 px; text-decoration: none;}
        .card {border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 6px;}
        .course {background: #eef; margin: 3px; padding: 5px; display: inline-block; border-radius: 4px;}
    </style>
</head>
<body>
    <header>
        <h1>Praktikum Laravel</h1>
        <nav>
            <a href="{{ route('students.index') }}">Mahasiswa</a>
        </nav>
    </header>

    <main>
        @yield('content')
    </main>
    <footer>
        <p>&copy; 2026 Praktikum Laravel - Davin A.S</p>
    </footer>
</body>
</html>