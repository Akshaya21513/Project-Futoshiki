# Futoshiki
<!DOCTYPE html>
<html>
<head>
    
</head>
<body>
<p>Futoshiki Puzzle Game is an intriguing Japanese-origin puzzle where "futoshiki" translates to "inequality." The aim of the game is to position numbers within the grid, ensuring that every row and column contains unique digits. Additionally, players must adhere to specified inequality rules while placing the numbers. This desktop application is developed using Python.
</p>
<h2>Futoshiki Puzzle Rules</h2>

<h3>1. Unique Numbers:</h3>
<p>Every row and every column must contain unique numbers from 1 to the size of the grid (in this case, 4).</p>

<h3>2. Inequality Constraints:</h3>
<p>
    Inequality signs (< and >) are placed between certain cells to indicate the relative order of the numbers in those cells.
    <ul>
        <li>A less-than sign (<) between two cells means the number in the left cell must be less than the number in the right cell.</li>
        <li>A greater-than sign (>) between two cells means the number in the left cell must be greater than the number in the right cell.</li>
    </ul>
</p>

<h3>Example 4x4 Futoshiki Grid:</h3>

<table>
    <tr>
        <td>1</td>
        <td>&lt;</td>
        <td>3</td>
        <td>&lt;</td>
        <td>2</td>
    </tr>
    <tr>
        <td>&uarr;</td>
        <td></td>
        <td>&darr;</td>
        <td></td>
        <td>&uarr;</td>
    </tr>
    <tr>
        <td>3</td>
        <td>&gt;</td>
        <td>1</td>
        <td>&lt;</td>
        <td>4</td>
    </tr>
    <tr>
        <td>|</td>
        <td></td>
        <td>|</td>
        <td></td>
        <td>|</td>
    </tr>
    <tr>
        <td>2</td>
        <td>&lt;</td>
        <td>4</td>
        <td>&gt;</td>
        <td>1</td>
    </tr>
    <tr>
        <td>&uarr;</td>
        <td></td>
        <td>&uarr;</td>
        <td></td>
        <td>&uarr;</td>
    </tr>
    <tr>
        <td>4</td>
        <td>&gt;</td>
        <td>2</td>
        <td>&gt;</td>
        <td>3</td>
    </tr>
</table>
<p>In this example:<br>

The numbers 1, 2, 3, and 4 must be placed in the grid.<br>
The < and > signs indicate the relative order of the adjacent numbers.<br>
To solve the puzzle, you need to fill in the grid with numbers that satisfy the uniqueness rule and the specified inequality constraints.</p>
</body>
</html>
