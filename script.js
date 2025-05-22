fetch('data/predictions.json')
  .then(res => res.json())
  .then(data => {
    document.getElementById('time').textContent = "Обновлено: " + data.updated;
    const table = document.createElement('table');
    table.innerHTML = `<tr><th>Матч</th><th>Победитель</th><th>Вероятность</th></tr>`;
    data.predictions.forEach(p => {
      table.innerHTML += `<tr><td>${p.match}</td><td>${p.winner}</td><td>${p.probability}</td></tr>`;
    });
    document.getElementById('predictions').appendChild(table);
  });