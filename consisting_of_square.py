<!DOCTYPE html>
<html>
<head>
    <title>Student Marks Table</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            text-align: center;
        }

        h2 {
            color: #333;
        }

        table {
            margin: 20px auto;
            border-collapse: collapse;
            width: 60%;
            background-color: #ffffff;
        }

        th, td {
            border: 1px solid black;
            padding: 10px;
            text-align: center;
        }

        th {
            background-color: #4CAF50;
            color: white;
        }

        tr:nth-child(even) {
            background-color: #f9f9f9;
        }

        tr:hover {
            background-color: #ddd;
        }
    </style>
</head>

<body>

    <h2>Student Marks Table</h2>

    <table>
        <tr>
            <th>Student Name</th>
            <th>Maths</th>
            <th>Physics</th>
            <th>Chemistry</th>
            <th>Total</th>
        </tr>

        <tr>
            <td>Rahul</td>
            <td>85</td>
            <td>78</td>
            <td>90</td>
            <td>253</td>
        </tr>

        <tr>
            <td>Anjali</td>
            <td>92</td>
            <td>88</td>
            <td>95</td>
            <td>275</td>
        </tr>

        <tr>
            <td>Vikram</td>
            <td>70</td>
            <td>75</td>
            <td>80</td>
            <td>225</td>
        </tr>

    </table>

</body>
</html>