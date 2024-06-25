<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Users</title>
    <style>
        table {
            width: 50%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 18px;
            text-align: left;
        }
        th, td {
            padding: 12px;
            border: 1px solid #dddddd;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Age</th>
                <th>City</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>John Doe</td>
                <td>28</td>
                <td>New York</td>
            </tr>
            <tr>
                <td>Jane Smith</td>
                <td>34</td>
                <td>Los Angeles</td>
            </tr>
            <tr>
                <td>Sam Brown</td>
                <td>22</td>
                <td>Chicago</td>
            </tr>
        </tbody>
    </table>
    <a href="{{ route('export') }}">
        <button>Download Excel</button>
    </a>
</body>
</html>
