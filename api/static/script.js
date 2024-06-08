document.addEventListener('DOMContentLoaded', (event) => {
    const button = document.getElementById('btn');
    button.addEventListener('click', () => {
        alert('Button clicked!');
    });

    const data = {
        Filemoon: "{{ data['Filemoon'] }}",
        Streamsb: "{{ data['Streamsb'] }}",
        Streamhd: "{{ data['Streamhd'] }}",
        Gohost: "{{ data['Gohost'] }}",
        Host5: "{{ data['Host5'] }}",
        Abyss: "{{ data['Abyss'] }}"
    };

    const listOfServers = document.getElementById('listOfServers');
    const links = listOfServers.getElementsByTagName('a');

    for (let i = links.length - 1; i >= 0; i--) {
        const link = links[i];
        const href = link.getAttribute('href');
        if (!href || href === '#' || href === 'null' || href === '{{ data[\'\' ] }}') {
            link.parentNode.remove();
        }
    }
});
