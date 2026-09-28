<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
class StudentController extends Controller
{
    public function index()
    {
        $students = [[
            'name' => 'Davin Aileenskie S',
            'major' => 'sistem informasi kota cerdas',
            'age' => 19,
            'courses' => [
                'Pemrograman Web Lanjut',
                'Pemrograman Mobile',
                'Pemrograman Berbasis Framework',
                'Pemrograman Berbasis Framework Lanjut'],
        ],
        [
            'name' => 'siti',
            'major' => 'sistem informasi',
            'age' => 25,
            'courses' => [
                'UI/UX Design',
                'Pemrograman Mobile',
                'Pemrograman Berbasis Framework',
                'Manajemen Proyek'],
        ],
    ];
        return view('students.index', compact('students'));
        }
}
