# Catalog Master Search

Welcome to the **Master Search Database**. Use the search bar in the top right of this table to instantly filter through all computed geometric spaces, or sort by dimension, Fano index, and rank. You can type freely (e.g., "Gr", "Fano Index 2", "15") to find exactly what you are looking for.

<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.css">
<script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.js"></script>
<script>
$(document).ready( function () {
    $('table').DataTable({
        "pageLength": 25,
        "order": [[ 2, "desc" ]]
    });
} );
</script>

| Geometry | Ambient Space | Dimension | Fano Index | Basis Rank |
|---|---|---|---|---|
| [P3  Fano index 4](projective.md#p3fanoindex4) | A3 | 3 | 4 | 4 |
| [P2 Fano index 3](projective.md#p2fanoindex3) | A2 | 2 | 3 | 3 |
| [P2  Fano index 3](projective.md#p2fanoindex3) | A2 | 2 | 3 | 3 |
| [P2 / O(2)](projective.md#p2o2) | A2 | 1 | 1 | 3 |
| [P4  Fano index 5](projective.md#p4fanoindex5) | A4 | 4 | 5 | 5 |
| [P3 / O(2)](projective.md#p3o2) | A3 | 2 | 2 | 4 |
| [P4 / O(2)](projective.md#p4o2) | A4 | 3 | 3 | 5 |
| [P4 / O(3)](projective.md#p4o3) | A4 | 3 | 2 | 5 |
| [P5  Fano index 6](projective.md#p5fanoindex6) | A5 | 5 | 6 | 6 |
| [P5 / O(2)](projective.md#p5o2) | A5 | 4 | 4 | 6 |
| [P5 / O(2)+O(2)](projective.md#p5o2o2) | A5 | 3 | 2 | 6 |
| [P3 / O(3)](projective.md#p3o3) | A3 | 2 | 1 | 4 |
| [P5 / O(3)](projective.md#p5o3) | A5 | 4 | 3 | 6 |
| [P5 / O(4)](projective.md#p5o4) | A5 | 4 | 2 | 6 |
| [P4 / O(2)+O(2)](projective.md#p4o2o2) | A4 | 2 | 1 | 5 |
| [P6 / O(2)+O(2)](projective.md#p6o2o2) | A6 | 4 | 3 | 7 |
| [P6  Fano index 7](projective.md#p6fanoindex7) | A6 | 6 | 7 | 7 |
| [P6 / O(2)+O(3)](projective.md#p6o2o3) | A6 | 4 | 2 | 7 |
| [P6 / O(2)](projective.md#p6o2) | A6 | 5 | 5 | 7 |
| [P6 / O(4)](projective.md#p6o4) | A6 | 5 | 3 | 7 |
| [P6 / O(3)](projective.md#p6o3) | A6 | 5 | 4 | 7 |
| [P6 / O(5)](projective.md#p6o5) | A6 | 5 | 2 | 7 |
| [P4 / O(4)](projective.md#p4o4) | A4 | 3 | 1 | 5 |
| [P5 / O(2)+O(3)](projective.md#p5o2o3) | A5 | 3 | 1 | 6 |
| [P7 / O(2)](projective.md#p7o2) | A7 | 6 | 6 | 8 |
| [P7 / O(2)+O(2)](projective.md#p7o2o2) | A7 | 5 | 4 | 8 |
| [P7 / O(2)+O(2)+O(2)](projective.md#p7o2o2o2) | A7 | 4 | 2 | 8 |
| [P7 / O(2)+O(3)](projective.md#p7o2o3) | A7 | 5 | 3 | 8 |
| [P7  Fano index 8](projective.md#p7fanoindex8) | A7 | 7 | 8 | 8 |
| [P7 / O(2)+O(4)](projective.md#p7o2o4) | A7 | 5 | 2 | 8 |
| [P7 / O(3)](projective.md#p7o3) | A7 | 6 | 5 | 8 |
| [P7 / O(5)](projective.md#p7o5) | A7 | 6 | 3 | 8 |
| [P7 / O(4)](projective.md#p7o4) | A7 | 6 | 4 | 8 |
| [P7 / O(3)+O(3)](projective.md#p7o3o3) | A7 | 5 | 2 | 8 |
| [P7 / O(6)](projective.md#p7o6) | A7 | 6 | 2 | 8 |
| [P6 / O(2)+O(2)+O(2)](projective.md#p6o2o2o2) | A6 | 3 | 1 | 7 |
| [P5 / O(5)](projective.md#p5o5) | A5 | 4 | 1 | 6 |
| [P8 / O(2)](projective.md#p8o2) | A8 | 7 | 7 | 9 |
| [P8  Fano index 9](projective.md#p8fanoindex9) | A8 | 8 | 9 | 9 |
| [P8 / O(2)+O(2)+O(2)](projective.md#p8o2o2o2) | A8 | 5 | 3 | 9 |
| [P8 / O(2)+O(2)](projective.md#p8o2o2) | A8 | 6 | 5 | 9 |
| [P8 / O(2)+O(2)+O(3)](projective.md#p8o2o2o3) | A8 | 5 | 2 | 9 |
| [P8 / O(2)+O(3)](projective.md#p8o2o3) | A8 | 6 | 4 | 9 |
| [P8 / O(2)+O(4)](projective.md#p8o2o4) | A8 | 6 | 3 | 9 |
| [P8 / O(2)+O(5)](projective.md#p8o2o5) | A8 | 6 | 2 | 9 |
| [P6 / O(3)+O(3)](projective.md#p6o3o3) | A6 | 4 | 1 | 7 |
| [P6 / O(2)+O(4)](projective.md#p6o2o4) | A6 | 4 | 1 | 7 |
| [P8 / O(3)](projective.md#p8o3) | A8 | 7 | 6 | 9 |
| [P8 / O(3)+O(3)](projective.md#p8o3o3) | A8 | 6 | 3 | 9 |
| [P8 / O(4)](projective.md#p8o4) | A8 | 7 | 5 | 9 |
| [P8 / O(3)+O(4)](projective.md#p8o3o4) | A8 | 6 | 2 | 9 |
| [P8 / O(5)](projective.md#p8o5) | A8 | 7 | 4 | 9 |
| [P8 / O(6)](projective.md#p8o6) | A8 | 7 | 3 | 9 |
| [Gr(2,4)](grassmannians.md#gr24) | A3 | 4 | 4 | 6 |
| [Gr(2,4) / O(1)](grassmannians.md#gr24o1) | A3 | 3 | 3 | 6 |
| [Gr(2,4) / O(1)+O(1)](grassmannians.md#gr24o1o1) | A3 | 2 | 2 | 6 |
| [Gr(2,4) / O(1)+O(1)+O(1)](grassmannians.md#gr24o1o1o1) | A3 | 1 | 1 | 6 |
| [Gr(2,4) / O(1)+O(2)](grassmannians.md#gr24o1o2) | A3 | 2 | 1 | 6 |
| [Gr(2,4) / O(2)](grassmannians.md#gr24o2) | A3 | 3 | 2 | 6 |
| [Gr(2,4) / O(3)](grassmannians.md#gr24o3) | A3 | 3 | 1 | 6 |
| [Gr(3,4)](grassmannians.md#gr34) | A3 | 3 | 4 | 4 |
| [Gr(3,4) / O(1)](grassmannians.md#gr34o1) | A3 | 2 | 3 | 4 |
| [Gr(3,4) / O(1)+O(1)](grassmannians.md#gr34o1o1) | A3 | 1 | 2 | 4 |
| [Gr(3,4) / O(1)+O(1)+O(1)](grassmannians.md#gr34o1o1o1) | A3 | 0 | 1 | 4 |
| [Gr(3,4) / O(1)+O(2)](grassmannians.md#gr34o1o2) | A3 | 1 | 1 | 4 |
| [Gr(3,4) / O(2)](grassmannians.md#gr34o2) | A3 | 2 | 2 | 4 |
| [Gr(3,4) / O(3)](grassmannians.md#gr34o3) | A3 | 2 | 1 | 4 |
| [Gr(2,5)](grassmannians.md#gr25) | A4 | 6 | 5 | 10 |
| [Gr(2,5) / O(1)](grassmannians.md#gr25o1) | A4 | 5 | 4 | 10 |
| [Gr(2,5) / O(1)+O(1)](grassmannians.md#gr25o1o1) | A4 | 4 | 3 | 10 |
| [Gr(2,5) / O(1)+O(1)+O(1)](grassmannians.md#gr25o1o1o1) | A4 | 3 | 2 | 10 |
| [Gr(2,5) / O(1)+O(1)+O(2)](grassmannians.md#gr25o1o1o2) | A4 | 3 | 1 | 10 |
| [Gr(2,5) / O(1)+O(2)](grassmannians.md#gr25o1o2) | A4 | 4 | 2 | 10 |
| [P8 / O(7)](projective.md#p8o7) | A8 | 7 | 2 | 9 |
| [Gr(2,5) / O(2)](grassmannians.md#gr25o2) | A4 | 5 | 3 | 10 |
| [Gr(2,5) / O(1)+O(3)](grassmannians.md#gr25o1o3) | A4 | 4 | 1 | 10 |
| [Gr(2,5) / O(3)](grassmannians.md#gr25o3) | A4 | 5 | 2 | 10 |
| [Gr(2,5) / O(2)+O(2)](grassmannians.md#gr25o2o2) | A4 | 4 | 1 | 10 |
| [Gr(3,5)](grassmannians.md#gr35) | A4 | 6 | 5 | 10 |
| [Gr(3,5) / O(1)](grassmannians.md#gr35o1) | A4 | 5 | 4 | 10 |
| [Gr(3,5) / O(1)+O(1)](grassmannians.md#gr35o1o1) | A4 | 4 | 3 | 10 |
| [Gr(3,5) / O(1)+O(1)+O(1)](grassmannians.md#gr35o1o1o1) | A4 | 3 | 2 | 10 |
| [Gr(3,5) / O(1)+O(1)+O(2)](grassmannians.md#gr35o1o1o2) | A4 | 3 | 1 | 10 |
| [Gr(3,5) / O(1)+O(2)](grassmannians.md#gr35o1o2) | A4 | 4 | 2 | 10 |
| [P7 / O(2)+O(2)+O(3)](projective.md#p7o2o2o3) | A7 | 4 | 1 | 8 |
| [Gr(3,5) / O(2)](grassmannians.md#gr35o2) | A4 | 5 | 3 | 10 |
| [Gr(3,5) / O(1)+O(3)](grassmannians.md#gr35o1o3) | A4 | 4 | 1 | 10 |
| [Gr(3,5) / O(3)](grassmannians.md#gr35o3) | A4 | 5 | 2 | 10 |
| [Gr(4,5)](grassmannians.md#gr45) | A4 | 4 | 5 | 5 |
| [Gr(4,5) / O(1)](grassmannians.md#gr45o1) | A4 | 3 | 4 | 4 |
| [Gr(4,5) / O(1)+O(1)](grassmannians.md#gr45o1o1) | A4 | 2 | 3 | 3 |
| [Gr(4,5) / O(1)+O(1)+O(1)](grassmannians.md#gr45o1o1o1) | A4 | 1 | 2 | 2 |
| [Gr(4,5) / O(1)+O(1)+O(2)](grassmannians.md#gr45o1o1o2) | A4 | 1 | 1 | 2 |
| [Gr(4,5) / O(1)+O(2)](grassmannians.md#gr45o1o2) | A4 | 2 | 2 | 3 |
| [Gr(4,5) / O(1)+O(3)](grassmannians.md#gr45o1o3) | A4 | 2 | 1 | 3 |
| [Gr(4,5) / O(2)](grassmannians.md#gr45o2) | A4 | 3 | 3 | 4 |
| [Gr(4,5) / O(2)+O(2)](grassmannians.md#gr45o2o2) | A4 | 2 | 1 | 3 |
| [Gr(4,5) / O(3)](grassmannians.md#gr45o3) | A4 | 3 | 2 | 4 |
| [Gr(4,5) / O(4)](grassmannians.md#gr45o4) | A4 | 3 | 1 | 4 |
| [Gr(2,6)](grassmannians.md#gr26) | A5 | 8 | 6 | 15 |
| [Gr(2,6) / O(1)](grassmannians.md#gr26o1) | A5 | 7 | 5 | 12 |
| [Gr(2,6) / O(1)+O(1)](grassmannians.md#gr26o1o1) | A5 | 6 | 4 | 10 |
| [Gr(2,6) / O(1)+O(1)+O(1)](grassmannians.md#gr26o1o1o1) | A5 | 5 | 3 | 8 |
| [Gr(2,6) / O(1)+O(1)+O(2)](grassmannians.md#gr26o1o1o2) | A5 | 5 | 2 | 8 |
| [Gr(3,5) / O(2)+O(2)](grassmannians.md#gr35o2o2) | A4 | 4 | 1 | 6 |
| [Gr(2,6) / O(1)+O(2)](grassmannians.md#gr26o1o2) | A5 | 6 | 3 | 10 |