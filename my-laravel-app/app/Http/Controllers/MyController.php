<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use BaconQrCode\Renderer\Image\Png;
use BaconQrCode\Writer;
use App\Exports\UsersExport;
use Maatwebsite\Excel\Facades\Excel;


class MyController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        //
    }
    public function profilepage(){
        return view('Profile/profile');
    }
    


    public function generateQRCode($id)
    {
        $url = 'https://chart.googleapis.com/chart';
        $params = [
            'chs' => '300x300',
            'cht' => 'qr',
            'chl' => $id,
        ];
        $qrCodeUrl = $url . '?' . http_build_query($params);
        
        // Return the view with QR code URL
        return view('qrcode', ['qrCodeUrl' => $qrCodeUrl]);
    }
    

    /**
     * Show the form for creating a new resource.
     */
    public function export()
    {
        return Excel::download(new UsersExport, 'users.xlsx');
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(string $id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
