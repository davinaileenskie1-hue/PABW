<div class="card">
    <h3>{{ $student['name'] }}</h3>
    <p><strong>Jurusan: </strong> {{ $student['major'] }}</p>
    <p><strong>Umur: </strong> {{ $student['age'] }} Tahun</p>

    @if ($student['age'] >= 22)
    <p>Status: <span style="color:green;">Senior</span></p>
    @else
    <p>Status: <span style="color:blue;">Junior</span></p>
    @endif

    <h4>Mata Kuliah:</h4>
    @forelse ($student['courses'] as $course)
    <span class="course">{{ $course }}</span>
    @empty
    <p>Tidak ada mata kuliah terdaftar.</p>
@endforelse
</div>