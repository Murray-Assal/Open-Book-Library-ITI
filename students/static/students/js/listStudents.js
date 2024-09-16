function filterStudent() {
    const studentId = parseInt(document.getElementById('student-id').value);
    const rows = document.querySelectorAll('#student-table tr');

    rows.forEach(row => {
        const id = parseInt(row.getAttribute('data-id'));
        if (id === studentId || isNaN(studentId)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}