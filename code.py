<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <title>Кнопка Клик и Балик</title>
</head>
<body>
  <button id="clickBtn">Клик</button>
  <button id="balikBtn" style="display:none;">Балик</button>

  <script>
    const clickBtn = document.getElementById('clickBtn');
    const balikBtn = document.getElementById('balikBtn');

    clickBtn.addEventListener('click', () => {
      // Показать кнопку Балик при клике на Клик
      balikBtn.style.display = 'inline-block';
    });

    balikBtn.addEventListener('click', () => {
      alert('Нажата кнопка Балик!');
    });
  </script>
</body>
</html>
