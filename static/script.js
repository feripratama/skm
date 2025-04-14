document.addEventListener('DOMContentLoaded', function() {
    const pekerjaanSelect = document.querySelector('select[name="pekerjaan"]');
    const lainnyaContainer = document.getElementById('lainnya-container');

    pekerjaanSelect.addEventListener('change', function() {
        if (this.value === 'Lainnya') {
            lainnyaContainer.classList.remove('hidden');
        } else {
            lainnyaContainer.classList.add('hidden');
        }
    });
});
